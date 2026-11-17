# Citizen Assist AI - Extensao de Energias Renovaveis e Sustentaveis

## Proposito
Complemento ao Citizen Assist AI - Primeiro Emprego para orientar jovens e familias sobre economia de eletricidade. Implementacao didatica sem equipamentos fisicos e sem IA generativa.

## Integrantes
[PREENCHER NOME COMPLETO E RM]

## Como executar
Python 3.10+; no terminal, dentro desta pasta, execute `python main.py` (ou `py main.py` no Windows). Opcao **1**: pesquisar `energia solar` para obter orientacao; opcao **5**: simular economia. Informe consumo mensal (kWh), quantidade de lampadas antigas e tarifa (R$/kWh). Nao ha bibliotecas externas.

## O que foi acrescentado
- `energia.py`: calculos, premissas, comparacao e interface do simulador.
- `main.py`: opcao 5 integrada ao menu original.
- `data/base_conhecimento.json`: nova orientacao pesquisavel sobre energia.
- `DADOS_E_CALCULOS.md`: dados estimados, formulas, comparacao, custos, viabilidade, impactos e fontes.
- `TESTES_USUARIOS.md`: registro a preencher com testes reais.
- `test_energia.py`: testes automatizados de calculo e limites.
- `ROTEIRO_VIDEO_3_MIN.md`: roteiro de apresentacao.
- `ENTREGA_SERS_MODELO.txt`: modelo para envio no portal.

## Exemplo (200 kWh/mes, 5 lampadas, R$ 0,90/kWh)
- Conta estimada (somente parcela de consumo): R$ 180,00/mes.
- LED: 38,25 kWh/mes, cerca de R$ 34,43/mes; investimento ilustrativo R$ 60.
- Solar 1 kWp: ate 120 kWh/mes aproveitaveis, economia bruta ilustrativa R$ 108/mes; investimento ilustrativo R$ 4.500.

## Limitacoes
Todos os precos, tarifa e produtividade solar sao **premissas hipoteticas**; resultados nao sao garantidos. Nao inclui impostos, encargos, minimo faturavel, regras de compensacao, perdas, manutencao ou financiamento. Consultar ANEEL, EPE e INMETRO, com links em `DADOS_E_CALCULOS.md`. Testes com pessoas, confirmacao de referencias, identificacao de integrantes e links de publicacao devem ser completados antes da entrega.

## Testes tecnicos
`python -m unittest test_energia.py -v`
