from extract import extract_supermarket_data
from transform import transform_supermarket_data
from load import load_supermarket_data


def run_etl():

    # Extract
    extract_supermarket_data()

    # Transform
    df = transform_supermarket_data()

    # Load
    load_supermarket_data(df)


if __name__ == "__main__":
    run_etl()