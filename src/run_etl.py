# run_etl.py
from extract import extract
from load import load_raw

if __name__ == "__main__":
    df = extract()
    load_raw(df)