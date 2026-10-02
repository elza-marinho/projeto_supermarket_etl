import pandas as pd

if __name__ == "__main__":
    caminho_csv = r"data/raw/Supermarket Analysis.csv"
    df = pd.read_csv(caminho_csv)

    print(df.head())
    print(df.info())
    print(df.shape)
    print(df.columns)
    print(df.dtypes)
    print(df.describe())
    print(df.isnull().sum())
    print(df.duplicated().sum())