import pandas as pd

def remove_duplicates(df):
    """Elimina duplicados del dataset."""
    return df.drop_duplicates()

def fill_missing_values(df):
    """Imputa valores nulos en columnas de texto."""
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    df['rating'] = df['rating'].fillna('Unknown')
    return df

def convert_dates(df):
    """Convierte la columna date_added y crea columnas derivadas."""
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month
    df['day_added'] = df['date_added'].dt.day
    return df

def split_duration(df):
    """Separa la duración en valor numérico y tipo."""
    df['duration_type'] = df['duration'].str.extract(r'(min|Season|Seasons)')
    df['duration_value'] = df['duration'].str.extract(r'(\d+)').astype(float)
    return df

def split_genres(df):
    """Convierte la columna listed_in en listas."""
    df['listed_in'] = df['listed_in'].str.split(', ')
    return df

def full_cleaning_pipeline(df):
    """Pipeline completo de limpieza."""
    df = remove_duplicates(df)
    df = fill_missing_values(df)
    df = convert_dates(df)
    df = split_duration(df)
    df = split_genres(df)
    return df
