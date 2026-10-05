import pandas as pd

def load_data(path):
    """Carga un archivo CSV."""
    return pd.read_csv(path)

def save_processed(df, path):
    """Guarda el dataset procesado."""
    df.to_csv(path, index=False)

def info(df):
    """Imprime información general del dataset."""
    print(df.info())
