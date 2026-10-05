def count_types(df):
    """Cuenta películas y series."""
    return df['type'].value_counts()

def top_countries(df, n=10):
    """Top países con más contenido."""
    return df['country'].value_counts().head(n)

def top_genres(df, n=10):
    """Top géneros más frecuentes."""
    return df['listed_in'].explode().value_counts().head(n)

def rating_distribution(df):
    """Distribución de clasificaciones."""
    return df['rating'].value_counts()

def duration_summary(df):
    """Resumen de duración de películas y series."""
    movies = df[df['duration_type'] == 'min']
    shows = df[df['duration_type'].isin(['Season', 'Seasons'])]
    return movies['duration_value'].describe(), shows['duration_value'].describe()
