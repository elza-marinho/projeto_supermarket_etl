from database import engine_supermarket

def load_tratada(df):
    df.to_sql("supermarket_tratada", engine_supermarket, if_exists="append", index =False)
    


print("Tabelas processadas carregadas no PostgreSQL.")
