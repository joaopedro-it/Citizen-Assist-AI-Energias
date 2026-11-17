# Citizen Assist AI — Primeiro Emprego

Projeto desenvolvido para a Global Solution 2026.2 da FIAP, com foco em orientação profissional, eficiência energética e sustentabilidade.

O Citizen Assist AI é um assistente de terminal desenvolvido em Python para orientar jovens sobre documentos, primeiro emprego, estágio e formação profissional.

O sistema também possui um simulador de economia de energia, que compara alternativas de eficiência energética e fontes renováveis.

**Aviso:** Este assistente não é um canal oficial e não utiliza IA generativa. Suas respostas são baseadas em regras e dados previamente cadastrados.

## Integrantes

- Erick Banhos de Castro — RM 572131
- Cauã Paes Vivaldo — RM 569906
- João Pedro Soler — RM 569725

## Objetivos de Desenvolvimento Sustentável (ODS)

- ODS 4 — Educação de Qualidade
- ODS 7 — Energia Limpa e Acessível
- ODS 8 — Trabalho Decente e Crescimento Econômico
- ODS 12 — Consumo e Produção Responsáveis

## Tecnologias utilizadas

- Python 3.10+
- JSON
- CSV
- Visual Studio Code
- GitHub

## Como executar

1. Instale Python 3.10 ou superior.
2. Abra a pasta do projeto no VS Code.
3. Execute o comando `python main.py` no terminal.
4. Escolha uma das opções disponíveis:

   - 1 — Fazer pergunta
   - 2 — Navegar por categorias
   - 3 — Consultar indicadores
   - 4 — Exportar CSV
   - 5 — Simular economia de energia
   - 0 — Sair

## Arquitetura do sistema

- `orientacao.py`: classe Orientacao, responsável por representar cada registro.
- `base_conhecimento.py`: classe BaseConhecimento, responsável pela leitura do JSON, normalização e busca.
- `assistente.py`: classe Assistente, responsável pelos atendimentos, histórico e indicadores.
- `main.py`: menu principal e acesso ao simulador.
- `data/base_conhecimento.json`: base com 12 orientações divididas em 3 categorias.

## Funcionamento do assistente

O assistente utiliza um algoritmo de pontuação para identificar orientações relacionadas às perguntas dos usuários.

O texto é normalizado, removendo acentos e diferenças entre letras maiúsculas e minúsculas.

A pontuação considera:

- 3 pontos para cada expressão-chave identificada.
- 1 ponto para cada palavra relevante encontrada no título.
- Pontuação igual ou superior a 6: correspondência alta.
- Pontuação entre 3 e 5: correspondência média.
- Pontuação inferior a 3: nenhuma orientação identificada.

O sistema pode apresentar até duas orientações relacionadas à pergunta.

## Simulador de Energias Renováveis e Sustentáveis

A funcionalidade foi desenvolvida para ajudar usuários a compreender seu consumo de eletricidade e avaliar alternativas de economia.

O simulador solicita:

- Consumo mensal de energia em kWh.
- Quantidade de lâmpadas convencionais.
- Tarifa de eletricidade em R$/kWh.

Com essas informações, o sistema apresenta estimativas de custos e economia.

### Alternativa 1 — Substituição por lâmpadas LED

A substituição de lâmpadas convencionais por LED pode reduzir o consumo de eletricidade e proporcionar economia financeira.

Exemplo de simulação:

- Consumo residencial: 200 kWh/mês.
- Quantidade de lâmpadas: 4.
- Tarifa: R$ 0,90/kWh.
- Economia estimada: 30,6 kWh/mês.
- Economia financeira: R$ 27,54/mês.
- Investimento estimado: R$ 48,00.

### Alternativa 2 — Energia solar fotovoltaica

A energia solar fotovoltaica utiliza a radiação solar para produzir eletricidade, sendo uma alternativa renovável.

Exemplo de simulação:

- Consumo residencial: 200 kWh/mês.
- Geração solar estimada: 120 kWh/mês.
- Economia bruta estimada: R$ 108,00/mês.
- Investimento hipotético: R$ 4.500,00.

### Comparação das alternativas

A substituição por LED apresenta menor investimento inicial e pode proporcionar economia com uma implementação relativamente simples.

A energia solar fotovoltaica utiliza uma fonte renovável e pode reduzir a quantidade de eletricidade adquirida da rede, mas exige maior investimento inicial e condições adequadas de instalação.

Os valores apresentados são estimativas ilustrativas. Não representam propostas comerciais ou garantias de economia.

A economia solar real depende de fatores como localização, radiação solar, sombreamento, características do sistema, regras tarifárias e custos de disponibilidade.

As economias das duas alternativas não devem ser simplesmente somadas, pois a redução do consumo altera a quantidade de energia que pode ser compensada pela geração solar.

## Sustentabilidade e impactos ambientais

A utilização de lâmpadas LED contribui para a redução do desperdício de eletricidade.

A energia solar fotovoltaica permite gerar eletricidade a partir de uma fonte renovável.

Entretanto, ambas as tecnologias possuem impactos relacionados à fabricação, ao transporte e ao descarte de seus componentes.

## Testes e validação

O projeto inclui testes automatizados para verificar funcionalidades do sistema.

Os testes com usuários devem avaliar a compreensão das informações, a utilidade das recomendações e a facilidade de utilização.

Os resultados dos testes externos, os comentários recebidos e os ajustes efetivamente realizados devem ser registrados no arquivo `TESTES_USUARIOS.md`.

## Segurança e limitações

O assistente não solicita identificadores pessoais e possui regras para bloquear determinadas entradas potencialmente sensíveis.

As orientações profissionais são gerais e devem ser verificadas nas fontes oficiais.

Os resultados do simulador energético são estimativas baseadas nas premissas documentadas e podem variar conforme as condições reais de utilização.

## Fontes de referência

Para orientações profissionais:

- Gov.br
- Ministério do Trabalho e Emprego
- Receita Federal
- MEC
- INEP
- Lei nº 11.788/2008

Para orientações energéticas:

- ANEEL — https://www.gov.br/aneel
- EPE — https://www.epe.gov.br
- INMETRO — https://www.gov.br/inmetro

As fontes devem ser verificadas para confirmar as informações e premissas utilizadas.

## Documentação complementar

- `README_SERS.md` — Documentação específica da disciplina de Energias Renováveis e Sustentáveis.
- `DADOS_E_CALCULOS.md` — Premissas, cálculos e comparação das alternativas.
- `TESTES_USUARIOS.md` — Registro dos testes com usuários.
- `ROTEIRO_VIDEO_3_MIN.md` — Roteiro da apresentação técnica.

## Vídeo de apresentação

O vídeo técnico da disciplina de Soluções em Energias Renováveis e Sustentáveis demonstra o funcionamento do simulador, a comparação das alternativas e as principais recomendações.

**Link do vídeo:** [INSERIR LINK DO YOUTUBE]

## Integração entre disciplinas

O Citizen Assist AI foi desenvolvido como um projeto interdisciplinar da Global Solution 2026.2.

A contribuição de Soluções em Energias Renováveis e Sustentáveis foi integrada ao assistente por meio de um simulador energético, permitindo apresentar orientações sobre consumo, eficiência energética e fontes renováveis.

A documentação específica dessa contribuição está disponível no arquivo `README_SERS.md`.

---

**FIAP — Ciência da Computação | Global Solution 2026.2**
