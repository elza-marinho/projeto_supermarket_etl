# ETL e análise de vendas de supermercado

Projeto de **ETL em Python** desenvolvido para processar dados de vendas de um supermercado. O projeto realiza a extração dos dados a partir de um arquivo CSV, transformação e limpeza dos dados com Pandas, carregamento dos dados tratados no PostgreSQL e geração de um arquivo CSV processado.

Após o processo de ETL, os dados tratados são utilizados para responder perguntas de negócio por meio de consultas SQL e análises com gráficos.

A fonte dos dados utilizada foi o dataset **Supermarket Sales**, disponível no Kaggle.

## Tecnologias utilizadas

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* SQL
* Matplotlib
* python-dotenv

## Estrutura do projeto

```text
.
├── data/
│   ├── raw/                       # CSV original, sem alterações
│   └── processed/                 # CSV tratado gerado pelo ETL
├── charts/                        # Gráficos gerados durante a análise
├── src/
│   ├── database.py                # Conexão com o PostgreSQL
│   ├── extract.py                 # Extração dos dados do CSV
│   ├── transform.py               # Transformação e limpeza dos dados
│   └── load.py                    # Carregamento dos dados
├── consultas.sql                  # Consultas utilizadas na análise
├── criar_tabela.sql               # Criação das tabelas no PostgreSQL
├── run_etl.py                     # Execução do pipeline ETL
├── requirements.txt               # Dependências do projeto
└── .env                           # Variáveis de ambiente
```

## Fluxo do projeto

O projeto segue as três principais etapas de um processo ETL:

### Extract → Transform → Load

### 1. Configuração do ambiente

Crie um ambiente virtual no VS Code:

```bash
python -m venv venv
```

Ative o ambiente virtual e instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 2. Banco de dados

Crie um banco de dados PostgreSQL chamado `supermarket`.

As credenciais de acesso ao banco são configuradas no arquivo `.env`, utilizando variáveis de ambiente para informações como:

* usuário;
* senha;
* host;
* porta;
* nome do banco.

O arquivo `.env` não deve ser versionado no GitHub.

### 3. Criação das tabelas

O arquivo `criar_tabela.sql` contém os comandos SQL utilizados para criar as tabelas necessárias no banco de dados PostgreSQL.

### 4. Dados brutos

O arquivo original `Supermarket Analysis.csv` é armazenado em:

```data
data/raw/
```

O arquivo original é mantido sem alterações, preservando os dados da fonte.

### 5. Extract

O arquivo `extract.py` realiza a leitura do CSV bruto.

Os dados são inicialmente carregados mantendo as colunas como texto, preparando o DataFrame para a etapa de transformação.

### 6. Transform

O arquivo `transform.py` é responsável pelo tratamento dos dados.

As principais transformações realizadas são:

* padronização dos nomes das colunas;
* conversão de datas, horários e colunas numéricas para os tipos adequados;
* verificação de valores nulos;
* remoção de linhas duplicadas;
* criação da coluna `dia_semana`;
* renomeação das colunas para português.

### 7. Load

O arquivo `load.py` realiza o carregamento dos dados tratados:

* na tabela `supermarket_tratada` do PostgreSQL;
* no arquivo `data/processed/supermarket_tratada.csv`.

O carregamento no PostgreSQL utiliza `if_exists="replace"`, fazendo com que a tabela seja substituída a cada nova execução do processo, evitando a duplicação dos dados durante execuções repetidas.

### 8. Execução do ETL

O pipeline completo pode ser executado pelo arquivo:

```src
run_etl.py
```

O fluxo executado é:

```text
Extract → Transform → Load
```

## Análise e perguntas de negócio

Após o tratamento dos dados, as perguntas de negócio foram respondidas utilizando o arquivo:

```src
data/processed/supermarket_tratada.csv
```

e consultas SQL armazenadas em:

```sql
consultas.sql
```

### Resultados

| Pergunta                                             | Resposta           |               Valor |
| ---------------------------------------------------- | ------------------ | ------------------: |
| Qual filial teve o maior faturamento?                | Giza               |       R$ 110.568,71 |
| Qual filial realizou mais vendas?                    | Alex               |          340 vendas |
| Qual linha de produto teve o maior faturamento?      | Food and beverages |        R$ 56.144,84 |
| Qual linha de produto teve a melhor avaliação média? | Food and beverages |                7,11 |
| Qual foi o valor médio das vendas?                   | —                  |           R$ 322,97 |
| Qual foi a maior venda registrada?                   | —                  |         R$ 1.042,65 |
| Qual foi a forma de pagamento mais utilizada?        | Ewallet            | 34,5% (Cash: 34,4%) |
| Em que dia da semana ocorreram mais vendas?          | Sábado             |          164 vendas |

Foram utilizadas ferramentas como **Python, Pandas, SQL e PostgreSQL**, além da geração de gráficos para apoiar a análise dos resultados.
