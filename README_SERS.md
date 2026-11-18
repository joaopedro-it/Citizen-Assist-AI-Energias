# Citizen Assist AI - Extensao de Energias Renovaveis e Sustentaveis

## Proposito
Complemento ao Citizen Assist AI - Primeiro Emprego para orientar jovens e familias sobre economia de eletricidade. Implementacao didatica sem equipamentos fisicos e sem IA generativa.

## Integrantes

- Erick Banhos de Castro — RM 572131
- Cauã Paes Vivaldo — RM 569906
- João Pedro Soler — RM 569725

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


## Limitações

Todos os preços, tarifas e estimativas de geração solar utilizados neste projeto são baseados em premissas hipotéticas e não representam resultados garantidos.

O simulador não considera impostos, encargos, custos de manutenção, financiamento ou variações regionais de tarifa.

As referências utilizadas incluem ANEEL, EPE e INMETRO, com informações complementares disponíveis no arquivo `DADOS_E_CALCULOS.md`.

Os cenários de simulação e a documentação de validação estão disponíveis em `TESTES_USUARIOS.md`. A avaliação com participantes externos ainda não foi documentada.

## Integração com o Citizen Assist AI

O simulador de energia foi integrado ao menu principal do Citizen Assist AI, permitindo comparar alternativas de eficiência energética e energia solar fotovoltaica.

A funcionalidade apresenta estimativas de consumo, economia financeira, investimento inicial e limitações das alternativas.

## Conclusão

A contribuição da disciplina de Soluções em Energias Renováveis e Sustentáveis amplia as funcionalidades do Citizen Assist AI, oferecendo orientações acessíveis sobre consumo consciente de eletricidade e sustentabilidade.
## Testes tecnicos
`python -m unittest test_energia.py -v`
