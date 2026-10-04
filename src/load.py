import os
from database import engine_supermarket


def load_supermarket_data(df):
    df.to_sql("supermarket_tratada", engine_supermarket, if_exists="replace", index=False)
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/supermarket_tratada.csv", index=False)

    print("Dados carregados em supermarket_tratada e salvos em data/processed/supermarket_tratada.csv")
    print("Dados carregados em supermarket_tratada.")