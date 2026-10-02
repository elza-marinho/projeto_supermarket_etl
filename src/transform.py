
import pandas as pd
from database import engine_supermarket

def transform():
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

    return df

if __name__ == "__main__":
    df = transform()
    print(df.head())
    print(df.dtypes)