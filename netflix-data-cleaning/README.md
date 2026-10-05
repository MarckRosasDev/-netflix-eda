# Análisis Exploratorio de Datos (EDA) — Catálogo de Netflix

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre el catálogo oficial de Netflix.  
El objetivo es identificar patrones de contenido, distribución por países, géneros más frecuentes, tendencias temporales y características clave del catálogo.

La limpieza avanzada del dataset está pausada; el análisis se realiza sobre el dataset original para mantener transparencia y trazabilidad.

---

## Estructura del proyecto

netflix-data-cleaning/
│
├── data/                 # Dataset original
├── notebooks/            # Notebook principal del análisis
├── src/                  # Funciones auxiliares (EDA, visualización, limpieza)
├── visuals/              # Gráficos generados
├── README.md             # Documentación del proyecto
└── requirements.txt      # Dependencias del proyecto

---

## Objetivos del análisis

- Analizar la distribución entre películas y series.  
- Identificar los países con mayor producción dentro del catálogo.  
- Evaluar los géneros más frecuentes.  
- Revisar tendencias temporales de contenido agregado.  
- Detectar valores nulos y características del dataset original.  
- Generar conclusiones y recomendaciones accionables.

---

## Principales hallazgos

### 1. Distribución de contenido
El catálogo contiene una mayor proporción de películas respecto a series.  
Las películas representan la mayoría del contenido disponible.

### 2. Países con mayor producción
Estados Unidos domina la producción del catálogo.  
Otros países relevantes incluyen India, Reino Unido y Canadá.

### 3. Géneros más frecuentes
Los géneros más comunes incluyen:
- Documentales  
- Dramas  
- Comedias  
- International Movies  

Estos géneros representan una parte significativa del catálogo.

### 4. Tendencias temporales
El contenido agregado muestra un crecimiento notable entre 2016 y 2020.  
Los años previos presentan menor volumen de incorporación.

### 5. Valores nulos
El dataset contiene valores nulos en columnas como:
- director  
- cast  
- country  
- date_added  

La limpieza avanzada está pendiente.

---

## Conclusiones generales

1. El catálogo de Netflix está fuertemente concentrado en películas.  
2. Estados Unidos es el principal país productor del contenido disponible.  
3. Los géneros más frecuentes reflejan una estrategia enfocada en drama, documental y contenido internacional.  
4. El crecimiento del catálogo se aceleró en los últimos años analizados.  
5. El dataset requiere limpieza para análisis más avanzados (pendiente).

---

## Recomendaciones

- Completar la limpieza del dataset para análisis más profundos.  
- Analizar géneros emergentes para identificar oportunidades de contenido.  
- Evaluar la distribución por país para detectar mercados subrepresentados.  
- Implementar dashboards interactivos para monitorear tendencias del catálogo.

---

## Tecnologías utilizadas

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter / VS Code Notebooks  

---

## Notebook en Kaggle
*[Catálogo de Netflix](https://www.kaggle.com/code/marcoantonioolmos/netflix-movies-and-tv-shows)*

---

## 👤 Autor

**Marco Antonio Olmos**  
Analista de Datos — TripleTen  
