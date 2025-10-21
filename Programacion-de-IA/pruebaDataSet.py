from datasets import load_dataset
import pandas as pd

# Cargar el dataset de mamíferos marinos desde Hugging Face
print("Descargando dataset de Hugging Face...")
dataset = load_dataset("ardavey/marine_ocean_mammal_sound")

# Convertir a pandas DataFrame sin decodificar el audio
# El dataset puede tener diferentes splits (train, test, etc.)
print(f"Splits disponibles: {list(dataset.keys())}")

# Usar el split de entrenamiento
train_dataset = dataset['train']

# Convertir a pandas usando to_pandas() que maneja mejor los datos de audio
df = train_dataset.to_pandas()

# Mostrar información del dataset
print(f"\nTamaño del dataset: {len(df)} registros")
print(f"Número de columnas: {len(df.columns)}")

# Que columnas tiene disponibles
print("\nColumnas disponibles:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i}. {col} - Tipo: {df[col].dtype}")

# Mostrar las primeras filas (sin la columna de audio que es muy grande)
print("\nPrimeras 5 filas (sin columna 'audio'):")
columnas_mostrar = [col for col in df.columns if col != 'audio']
print(df[columnas_mostrar].head())

# 4 registros random
print("\n4 registros aleatorios (sin columna 'audio'):")
print(df[columnas_mostrar].sample(min(4, len(df))))

# Estadísticas del dataset
print("\nEstadísticas del dataset:")
print(f"Total de registros: {len(df)}")

# Si hay columnas categóricas, mostrar los valores únicos
for col in columnas_mostrar:
    if df[col].dtype == 'object' or df[col].dtype.name == 'category':
        valores_unicos = df[col].nunique()
        print(f"\n'{col}' tiene {valores_unicos} valores únicos")
        if valores_unicos <= 10:
            print(f"  Valores: {df[col].unique().tolist()}")

print("\n" + "="*50)
print("COLUMNAS ÚTILES PARA ENTRENAR UN MODELO DE IA:")
print("="*50)
print("Features (X): Las columnas que NO sean 'audio' pueden usarse como características")
print("Target (y): Depende de tu objetivo, por ejemplo 'label' o 'species' si existen")