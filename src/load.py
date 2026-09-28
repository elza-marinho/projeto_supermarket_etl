# load.py
from database import engine

def load_raw(df):
   
    df.to_sql("raw", engine, if_exists="append", index=False)
    print(f"{len(df)} linhas carregadas na raw")
