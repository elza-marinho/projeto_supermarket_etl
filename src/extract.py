import pandas as pd
from sqlalchemy import text
from database import engine_supermarket

def extract_supermarket_data():
    RAW_DIR = "data/raw"
    caminho_csv = f"{RAW_DIR}/SuperMarket Analysis.csv"
    df = pd.read_csv(
        caminho_csv,
        sep=",",
        encoding="utf-8-sig",
        dtype=str,
    )
    return df



    
    
    
    
    
    


    