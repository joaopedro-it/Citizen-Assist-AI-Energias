# Citizen Assist AI — Primeiro Emprego

Assistente de terminal para orientar jovens sobre documentos, primeiro emprego, estagio e formacao. **Nao e um canal oficial.** Nao usa IA generativa: busca por regras.

## Integrantes
- [NOME COMPLETO — RM]

## ODS
- ODS 4 — Educacao de qualidade
- ODS 8 — Trabalho decente e crescimento economico

## Executar
1. Instale Python 3.10+.
2. Abra esta pasta no VS Code.
3. Execute `python main.py` (Windows pode usar `py main.py`).
4. Escolha 1 para perguntar, 2 para categorias, 3 para indicadores, 4 para CSV, 0 para sair.

## Arquitetura
- `orientacao.py`: classe Orientacao, representa cada registro.
- `base_conhecimento.py`: classe BaseConhecimento, le JSON, normaliza, pontua e busca.
- `assistente.py`: classe Assistente, atendimento, historico, indicadores e CSV.
- `main.py`: menu principal.
- `data/base_conhecimento.json`: 12 orientacoes em 3 categorias.

## Pontuacao
Normalizacao: minusculas, sem acentos nem pontuacao. +3 para cada expressao-chave encontrada como sequencia de palavras; +1 para cada palavra distinta da pergunta com 4+ letras presente no titulo. Busca devolve tuplas `(pontos, orientacao)` ordenadas por pontuacao. >=6: ALTA; 3 a 5: MEDIA; <3: sem orientacao. Mostra ate duas alternativas. Empate: menor id.

## Seguranca e limites
Perguntas com `@` ou 8+ digitos sao recusadas e nao registradas. O assistente nao pede identificadores pessoais. Historico de perguntas pode conter texto livre: nao digite dados pessoais. Fontes e datas devem ser conferidas pela equipe antes da entrega. `verificado_em: PENDENTE` significa **nao verificado**, nunca data inventada. Orientacoes sao gerais e podem mudar; consulte a fonte oficial.

## Fontes de referencia (conferir antes da entrega)
Gov.br / Ministerio do Trabalho, Receita Federal, TSE, Inep, MEC, Escola Virtual de Governo e Lei 11.788/2008. Links especificos estao no JSON. Registre a data real de verificacao em cada orientacao.

## Teste com usuarios (OBRIGATORIO — PREENCHER COM RESULTADOS REAIS)
- 3 participantes externos: [PENDENTE]
- Pelo menos 10 atendimentos: [PENDENTE]
- Resposta encontrada (%): [PENDENTE]
- Ajudou (%): [PENDENTE]
- Tempo medio: [PENDENTE]
- Tentativas por atendimento: [PENDENTE]
- Facilidade (1 a 5): [PENDENTE]
- Duvidas sem solucao: [PENDENTE]
- Melhoria realizada apos teste: [PENDENTE]

Nao inclua nomes nem dados pessoais dos participantes. A facilidade fica em `data/avaliacoes.json`; calcule a media das notas reais.

## Video tecnico
Link: [PENDENTE]
Duracao de 5 a 8 minutos. Todos integrantes devem falar. Mostrar JSON, classes e composicao, pontuacao com exemplo, testes de sucesso/fracasso, bloqueio de dados, categorias, mudanca ao vivo de palavra-chave, historico, CSV, indicadores, decisao tecnica e limitacao.

## Integracao com outras disciplinas
Nao implementada (opcional).


## Extensao de Energias Renovaveis e Sustentaveis
A contribuicao da disciplina SERS foi integrada: consulte **README_SERS.md** para executar e entender os calculos, referencias, testes e video.
