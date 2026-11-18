# Testes e Validação — Citizen Assist AI Energias

## 1. Objetivo

Avaliar a funcionalidade de simulação de economia energética do Citizen Assist AI, considerando diferentes perfis de consumo residencial.

A avaliação busca verificar a clareza das informações, a coerência dos cálculos e a utilidade das recomendações relacionadas à eficiência energética e à energia solar fotovoltaica.

## 2. Metodologia

Foram definidos cinco cenários de simulação, variando o consumo mensal, a quantidade de lâmpadas convencionais e a tarifa de eletricidade.

Os cenários permitem avaliar o comportamento do sistema em diferentes condições de consumo.

## 3. Cenários de teste

| Teste | Consumo mensal | Lâmpadas | Tarifa |
|---|---|---|---|
| 1 | 100 kWh | 3 | R$ 0,90 |
| 2 | 200 kWh | 5 | R$ 0,90 |
| 3 | 350 kWh | 8 | R$ 0,90 |
| 4 | 500 kWh | 10 | R$ 0,90 |
| 5 | 150 kWh | 4 | R$ 1,10 |

### Verificações previstas

**Teste 1 — Baixo consumo**

Verificar se o programa apresenta estimativas compreensíveis para uma residência com consumo reduzido.

**Teste 2 — Consumo intermediário**

Verificar a comparação financeira entre substituição de lâmpadas e geração solar.

**Teste 3 — Consumo elevado**

Analisar o comportamento dos cálculos quando o consumo e a quantidade de lâmpadas aumentam.

**Teste 4 — Consumo muito elevado**

Verificar se as recomendações continuam coerentes em um cenário de maior demanda energética.

**Teste 5 — Tarifa diferente**

Verificar se a alteração da tarifa influencia corretamente as estimativas financeiras.

## 4. Exemplos fictícios de feedback

As respostas abaixo são exemplos de como um participante poderia avaliar o sistema. Não representam entrevistas ou testes externos efetivamente realizados.

**Pergunta 1: O simulador é fácil de utilizar?**

Exemplo: "Sim, achei o programa simples. As perguntas são diretas e não tive dificuldade para entender quais informações precisava inserir."

**Pergunta 2: Os resultados apresentados são compreensíveis?**

Exemplo: "Sim. Gostei de conseguir visualizar quanto poderia economizar com lâmpadas LED e energia solar."

**Pergunta 3: As recomendações são úteis?**

Exemplo: "Sim, principalmente porque mostram o investimento inicial e a economia estimada de cada alternativa."

**Pergunta 4: O que poderia melhorar?**

Exemplo: "Seria interessante adicionar gráficos para facilitar a comparação dos resultados."

## 5. Melhorias propostas

Com base na análise dos cenários, foram identificadas possíveis melhorias futuras:

- Implementação de gráficos comparativos.
- Inclusão de tarifas regionais de eletricidade.
- Possibilidade de informar a potência real das lâmpadas.
- Estimativas de geração solar considerando a localização.
- Maior detalhamento dos custos e do retorno financeiro.

Essas melhorias são propostas e não devem ser consideradas funcionalidades já implementadas.

## 6. Limitações

Os resultados energéticos são estimativas baseadas em parâmetros simplificados.

Os custos de equipamentos, a geração solar e as economias financeiras podem variar conforme as condições reais.

A execução dos cenários e a coleta de feedback externo devem ser documentadas separadamente quando realizadas.

## 7. Conclusão

Os cenários definidos permitem avaliar diferentes condições de consumo e comparar alternativas de economia energética.

A funcionalidade oferece uma base para orientar usuários sobre eficiência energética e fontes renováveis.

A validação com participantes externos permanece necessária para confirmar a facilidade de utilização e a compreensão das recomendações.
