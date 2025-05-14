import pandas as pd
import matplotlib.pyplot as plt

#punto 1
df = pd.read_csv("biometria_pacientes.csv", encoding='latin1', sep=';')

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print("Primeras 10 filas:")
print(df.head(10))

#punto 2
duplicados = df.duplicated().sum()
print(f"Duplicados: {duplicados}")

nulos = df.isnull().sum()
print("Valores nulos por columna:")
print(nulos)

print("\nValores únicos en la columna 'fuma':")
print(df['fuma'].unique())

#punto 3

# df = df.drop_duplicates()

# columnas_corregidas = ['peso', 'talla', 'glucosa', 'colesterol']
# df = df.dropna(subset=columnas_corregidas)

# df['mes'] = df['fecha_de_tamizaje'].dt.month
