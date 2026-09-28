import pandas as pd

def extract():
    RAW_DIR = "data/raw"
    
    caminho_csv = f"{RAW_DIR}/Supermarket Analysis.csv"
    
    df = pd.read_csv(
        caminho_csv,
        sep=";",
        encoding="utf-8-sig",
        dtype=str,


    )
    return df

if __name__ == "__main__":
    df = extract()
    print(df.head())
    print(df.info())