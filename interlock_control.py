import csv
import random
import time
from datetime import datetime

from CoolProp.CoolProp import PropsSI


class ThermalInterlockSystem:
    """
    Sistema Instrumentado de Segurança (SIS) para Frigoríficos operando com Amônia (R717).
    Gera relatórios auditáveis (CSV) em conformidade com as normas de segurança (NR-13).
    """

    def __init__(self, fluid="Ammonia"):
        self.fluid = fluid
        self.log_file = "safety_audit_log.csv"

        # Setpoints OFICIAIS baseados no Manual Bitzer OS.53 a OS.105 (R717)
        self.MAX_P_DISCHARGE_PA = 2500000  # 25 Bar (Aprox. saturação a 60°C)
        self.MAX_T_DISCHARGE_K = (
            100 + 273.15
        )  # 100 °C (Limite máximo permitido para óleo Reniso KC68)
        self.MIN_SUPERHEAT_K = (
            10.0  # 10 K (Exigência Δtoh = 10 K nos limites de aplicação)
        )

        self.setup_logger()

    def setup_logger(self):
        with open(self.log_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Timestamp",
                    "P_Suc(Bar)",
                    "T_Suc(C)",
                    "Superheat(K)",
                    "Status_Valvula",
                    "Motivo_Intertravamento",
                ]
            )

    def get_superheat(self, p_suc_pa, t_suc_k):
        try:
            t_sat = PropsSI("T", "P", p_suc_pa, "Q", 1, self.fluid)
            return t_suc_k - t_sat
        except Exception:
            return None

    def evaluate_safety(self, p_suc_pa, t_suc_k, p_dis_pa, t_dis_k):
        sh = self.get_superheat(p_suc_pa, t_suc_k)
        if sh is None:
            return False, "Erro de Leitura Termodinâmica"

        # Avaliação com base no limite oficial de 10K
        if sh < self.MIN_SUPERHEAT_K:
            return False, f"Risco de Golpe de Líquido (SH={sh:.2f}K < 10K)"

        if p_dis_pa > self.MAX_P_DISCHARGE_PA:
            return False, "Risco NR-13: Sobrepressão de Descarga"

        if t_dis_k > self.MAX_T_DISCHARGE_K:
            return False, "Risco de Carbonização do Óleo (> 100 C)"

        return True, "Operação Segura"

    def run_monitoring_cycle(self):
        print("Iniciando monitoramento de segurança térmico (SIS)...")
        print(
            "Pressione 'Ctrl + C' no terminal a qualquer momento para encerrar o sistema.\n"
        )

        try:
            while True:
                # Simulando flutuação de sensores reais em um frigorífico
                p_suc = 300000 + random.uniform(-10000, 10000)  # ~3 Bar
                t_suc = 273.15 + random.uniform(-10, 5)  # Varia de -10C a +5C
                p_dis = 1200000 + random.uniform(-50000, 50000)  # ~12 Bar
                t_dis = 350.15 + random.uniform(-5, 5)  # ~77 C

                is_safe, reason = self.evaluate_safety(p_suc, t_suc, p_dis, t_dis)

                # Log auditável
                with open(self.log_file, mode="a", newline="") as file:
                    writer = csv.writer(file)
                    superheat_val = self.get_superheat(p_suc, t_suc)
                    writer.writerow(
                        [
                            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            round(p_suc / 100000, 2),
                            round(t_suc - 273.15, 2),
                            round(superheat_val, 2) if superheat_val else "ERR",
                            "ABERTA" if is_safe else "FECHADA (0%)",
                            reason,
                        ]
                    )

                if not is_safe:
                    print(f"[!] INTERTRAVAMENTO ATUADO: {reason}")
                else:
                    superheat_val = self.get_superheat(p_suc, t_suc)
                    print(
                        f"[*] Sistema Estável. Superaquecimento: {superheat_val:.2f}K"
                    )

                time.sleep(2)  # Lê a cada 2 segundos

        except KeyboardInterrupt:
            # Isso captura o Ctrl + C e encerra o programa graciosamente
            print(
                f"\n[INFO] Desligamento manual acionado. Relatório de auditoria salvo em '{self.log_file}'."
            )


if __name__ == "__main__":
    system = ThermalInterlockSystem()
    system.run_monitoring_cycle()
