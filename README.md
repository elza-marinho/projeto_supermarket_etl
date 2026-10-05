# ETL e análise de vendas de supermercado

Projeto de ETL em Python que lê o CSV bruto de vendas de um supermercado, trata os dados, grava o resultado no PostgreSQL e em CSV, e usa o dado tratado para responder perguntas de negócio com gráficos.

**Fonte dos dados:** `SuperMarket Analysis.csv`, disponível no Kaggle.

## Tecnologias

Python, pandas, SQLAlchemy, PostgreSQL, DBeaver, VS Code.

## Estrutura do projeto

├── data/
│   ├── raw/                # CSV original, sem alterações
│   └── processed/          # CSV tratado gerado pelo ETL
├── charts/                 # gráficos gerados pela análise
├── src/
│   ├── database.py         # conexão com o PostgreSQL
│   ├── extract.py          # lê o CSV bruto (todas as colunas como texto)
│   ├── transform.py        # trata os dados
│   ├── load.py             # grava no banco e em CSV
│   └── run_etl.py          # executa extract -> transform -> load
├── criar_tabela.sql        # cria a tabela no PostgreSQL
├── consultas.sql           # consultas das perguntas de negócio
├── requirements.txt
├── .env.example            # modelo das credenciais do banco
└── README.md

## Como executar

1. **Ambiente virtual** (no terminal do VS Code):
bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Linux/macOS

2. **Dependências:**
bash
   pip install -r requirements.txt

3. **Dados:** baixe o `SuperMarket Analysis.csv` do Kaggle e coloque em `data/raw/`. A pasta `data/processed/` recebe o CSV tratado.

4. **Banco de dados:** crie o banco `supermarket` no PostgreSQL (pelo DBeaver). Depois, usando a extensão SQLTools do VS Code (ou o próprio DBeaver), execute `criar_tabela.sql` para criar a tabela.

5. **Credenciais:** copie `.env.example` para `.env` e preencha usuário, senha, host, porta e nome do banco.

6. **Rodar o ETL:**
bash
   python src/run_etl.py

## O que cada etapa faz

- **extract.py:** lê o CSV bruto com todas as colunas como texto.
- **transform.py:**
  - padroniza os nomes das colunas (minúsculas, sem espaços);
  - converte datas, horas e colunas numéricas para o tipo correto;
  - verifica nulos e remove linhas duplicadas;
  - cria a coluna `dia_semana`;
  - renomeia as colunas para português.
- **load.py:** grava o resultado na tabela 'supermarket_tratada' do PostgreSQL e em 'data/processed/supermarket_tratada.csv'. Usa "if_exists="replace", então rodar o ETL mais de uma vez não duplica linhas.

## Análise de negócio

As perguntas foram respondidas a partir de 'data/processed/supermarket_tratada.csv' e das consultas SQL em 'consultas.sql'.

| | Pergunta | Resposta |
|---|---|
| Qual filial teve o maior faturamento? | Giza (110.568,71) |
| Qual filial realizou mais vendas? | Alex (340 vendas) |
| Qual linha de produto teve o maior faturamento? | Food and beverages (56.144,84) |
| Qual linha de produto teve a melhor avaliação média? | Food and beverages |
| Qual foi o valor médio das vendas? | 322,97 |
| Qual foi a maior venda registrada? | 1.042,65 |
| Qual foi a forma de pagamento mais utilizada? | Ewallet (34,5%), com Cash praticamente empatada (34,4%) |
| Em que dia da semana ocorreram mais vendas? | Sábado (164 vendas) |

Os gráficos correspondentes ficam na pasta charts
