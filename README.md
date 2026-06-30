Markdown
# Sistema Instrumentado de Segurança (SIS) para Refrigeração Industrial à Amônia (R717)

Projeto de extensão desenvolvido por acadêmicos de Engenharia Mecânica para controle lógico e proteção termodinâmica de compressores industriais, atuando de forma automatizada na prevenção de falhas catastróficas.

## 📋 Resumo do Projeto

### Problema e Forma de Contribuição
O projeto aborda o alto índice de quebras de compressores e falhas operacionais em sistemas de refrigeração industrial e frigoríficos, especificamente aqueles operando com amônia (R717). O problema central mitigado é o risco de danos críticos, como o golpe de líquido e a sobrepressão em vasos, causados por anomalias térmicas. A contribuição realizada consiste no desenvolvimento de um Sistema Instrumentado de Segurança (SIS), codificado em Python. O algoritmo utiliza a biblioteca termodinâmica `CoolProp` para calcular o superaquecimento em tempo real e automatizar o intertravamento lógico de válvulas, garantindo a proteção do sistema em condições críticas, conforme estabelecido pelas normativas de segurança NR-13 e NBR 16069.

### Estratégia de Desenvolvimento
O projeto foi estruturado com foco na segurança de fluidos tóxicos (Amônia) na indústria frigorífica. A modelagem matemática baseou-se no levantamento técnico em catálogos de compressores de referência (série OS da Bitzer), definindo o limite de superaquecimento de segurança (Δtoh) em 10 K e identificando os limites absolutos de temperatura e pressão do óleo lubrificante. O código foi desenvolvido para operar em um ciclo de varredura contínua (loop), simulando a resposta de um Controlador Lógico Programável (CLP) industrial. A validação técnica ocorreu através de testes de estresse mimetizando flutuações de sensores e gerando relatórios invioláveis de auditoria operacional em formato CSV.

### Relevância e Impacto
A disponibilização desta ferramenta open-source beneficia diretamente instituições frigoríficas, empresas de manutenção e, indiretamente, dezenas de técnicos de campo, mecânicos e instrumentistas. O impacto promovido é a democratização de uma lógica de controle avançada para proteção de ativos, reduzindo custos imprevistos com manutenções corretivas severas, além de mitigar agressivamente o risco de vazamentos tóxicos e acidentes industriais.

---

## ⚙️ Pré-requisitos e Como Executar

Instale as bibliotecas necessárias para o processamento termodinâmico e estruturação dos dados:

Bash
pip install CoolProp pandas
Execute o motor de cálculo:

Bash
python interlock_control.py
🎥 Demonstração Prática (Validação)
[Assista à demonstração em vídeo clicando aqui](https://drive.google.com/file/d/1PfNCPYAlRAlJiC7iJs2vlZL2EOlEjDdY/view?usp=drivesdk)

Assista à demonstração em vídeo do terminal executando o ciclo de varredura contínua, analisando as propriedades termofísicas do fluido R717 e realizando o desarme autônomo das válvulas de expansão eletrônica ao cruzar os setpoints críticos da norma NR-13.

👨‍💻 Autores
Luis Gustavo Godoy Matos - Desenvolvedor de Automação / Engenharia Mecânica (UTFPR)

Lucas Augusto Peppes do Valle Torres - Pesquisa e Documentação / Engenharia Mecânica (UTFPR)

Projeto desenvolvido como Trabalho de Extensão Universitária vinculado ao Departamento de Engenharia Mecânica da Universidade Tecnológica Federal do Paraná (UTFPR - Campus Curitiba).

Para rodar este algoritmo localmente e visualizar o intertravamento atuando sobre as válvulas e gerando os relatórios de auditoria (`safety_audit_log.csv`), é necessário possuir o Python instalado no sistema.


1. Clone este repositório para a sua máquina:
```bash
git clone [https://github.com/LMatosMec/interlock-coolprop-r717.git](https://github.com/LMatosMec/interlock-coolprop-r717.git)
cd interlock-coolprop-r717
