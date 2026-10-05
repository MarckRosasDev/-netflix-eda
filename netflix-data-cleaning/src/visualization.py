import matplotlib.pyplot as plt
import seaborn as sns

def plot_type_distribution(df):
    plt.figure(figsize=(8,5))
    sns.countplot(data=df, x='type', hue='type', palette='viridis', legend=False)
    plt.title("Distribución de contenido: Películas vs Series")
    plt.show()

def plot_year_added(df):
    plt.figure(figsize=(12,6))
    sns.countplot(data=df, x='year_added', hue='year_added', palette='coolwarm', legend=False)
    plt.title("Contenido agregado por año")
    plt.xticks(rotation=45)
    plt.show()

def plot_top_genres(df):
    genres = df['listed_in'].explode().value_counts().head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=genres.values, y=genres.index, palette='cubehelix')
    plt.title("Top 10 géneros más frecuentes")
    plt.show()

def plot_movie_duration(df):
    movies = df[df['duration_type'] == 'min']
    plt.figure(figsize=(12,5))
    sns.histplot(movies['duration_value'], kde=True, color='blue')
    plt.title("Distribución de duración de películas")
    plt.show()

def plot_show_seasons(df):
    shows = df[df['duration_type'].isin(['Season', 'Seasons'])]
    plt.figure(figsize=(12,5))
    sns.countplot(data=shows, x='duration_value', hue='duration_value', palette='rocket', legend=False)
    plt.title("Distribución de temporadas en series")
    plt.show()

def plot_movie_outliers(df):
    movies = df[df['duration_type'] == 'min']
    plt.figure(figsize=(10,5))
    sns.boxplot(data=movies, x='duration_value', color='purple')
    plt.title("Outliers en duración de películas")
    plt.show()
