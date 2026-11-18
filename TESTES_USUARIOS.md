# Testes e Validação — Citizen Assist AI Energias

## Objetivo

Verificar a coerência das estimativas energéticas e a clareza das orientações apresentadas pelo simulador.

## Metodologia

Foram definidos cinco cenários para avaliar diferentes níveis de consumo residencial, quantidades de lâmpadas e tarifas de eletricidade.

Os cenários são simulações planejadas e não representam avaliações realizadas por participantes externos.

## Cenários de simulação

| Teste | Consumo mensal | Lâmpadas | Tarifa |
|---|---|---|---|
| 1 | 100 kWh | 3 | R$ 0,90 |
| 2 | 200 kWh | 5 | R$ 0,90 |
| 3 | 350 kWh | 8 | R$ 0,90 |
| 4 | 500 kWh | 10 | R$ 0,90 |
| 5 | 150 kWh | 4 | R$ 1,10 |

## Critérios de avaliação

- Funcionamento do simulador com diferentes entradas.
- Coerência dos cálculos de consumo e economia.
- Comparação entre lâmpadas LED e energia solar.
- Clareza das recomendações apresentadas.
- Identificação dos custos e das limitações.

## Validação técnica

O projeto possui testes automatizados no arquivo `test_energia.py`.

Para executar:

`python -m unittest test_energia.py -v`

## Melhorias futuras

- Adicionar gráficos comparativos.
- Permitir a seleção de tarifas regionais.
- Considerar a localização na estimativa de geração solar.
- Ampliar as informações sobre retorno financeiro.

## Testes externos

A avaliação com participantes externos ainda não foi documentada.

Os cenários apresentados neste relatório não substituem testes reais de usabilidade.

## Conclusão

O simulador permite comparar alternativas de eficiência energética e geração renovável com base em parâmetros informados pelo usuário.

Os resultados são estimativas didáticas, sujeitas às premissas e limitações descritas em `DADOS_E_CALCULOS.md`.
