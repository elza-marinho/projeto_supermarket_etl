
import pandas as pd
from database import engine_supermarket

def transform_supermarket_data():
    df = pd.read_sql("SELECT * FROM supermarket_raw", engine_supermarket)

    # padronizando os nomes das colunas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    
  

    # ajuste de tipagem
    df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y")
    df["time"] = pd.to_datetime(df["time"], format="%I:%M:%S %p").dt.time
    df["unit_price"] = df["unit_price"].astype(float)
    df["quantity"] = df["quantity"].astype(int)
    df["sales"] = df["sales"].astype(float)
    df["rating"] = df["rating"].astype(float)
    


    # checando nulos 
    print(df.isnull().sum())

    #  remover duplicados
    df = df.drop_duplicates()

    # coluna derivada
    df["dia_semana"] = df["date"].dt.day_name()
    
    
    colunas_pt = {
    "invoice_id": "id_venda",
    "branch": "filial",
    "city": "cidade",
    "customer_type": "tipo_cliente",
    "gender": "genero",
    "product_line": "linha_produto",
    "unit_price": "preco_unitario",
    "quantity": "quantidade",
    "tax_5%": "imposto",
    "sales": "vendas",
    "date": "data_venda",
    "time": "hora_venda",
    "payment": "forma_pagamento",
    "cogs": "custo_mercadoria",
    "gross_margin_percentage": "margem_percentual",
    "gross_income": "receita_bruta",
    "rating": "avaliacao",
}
    
    df = df.rename(columns=colunas_pt)


    return df

if __name__ == "__main__":
    df = transform_supermarket_data()
   
