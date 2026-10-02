# run_etl.py
from extract import extract_supermarket_data
from transform import transform
from load import load, load_tratada


def run_etl():
    extract_supermarket_data()
 


if __name__ == "__main__":
    run_etl()    