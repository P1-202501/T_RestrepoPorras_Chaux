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

df = df.drop_duplicates()

#punto 4

columnas_corregidas = ['peso', 'talla', 'glucosa', 'colesterol']
df = df.dropna(subset=columnas_corregidas)

#punto 5
df['fuma'] = df['fuma'].str.lower().str.strip()
df['fuma'] = df['fuma'].replace({
    'sí': True, 'si': True, 'fuma': True,
    'no': False, 'desconocido': False, 'nunca': False, 'no fuma': False
})

#punto 6
df['fecha_de_tamizaje'] = pd.to_datetime(df['fecha_de_tamizaje'], dayfirst=True, errors='coerce')
df['mes'] = df['fecha_de_tamizaje'].dt.month
print(df['fecha_de_tamizaje'])
print(df['mes'])

#Parte 2

#Punto 7

df['imc'] = df['peso'] / (df['talla'] / 100) ** 2

#Punto 8
def clasificar_imc(imc):
    if imc < 18.5:
        return 'Bajo peso'
    elif imc < 25:
        return 'Normal'
    elif imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

df['clasificación_imc'] = df['imc'].apply(clasificar_imc)

#Punto 9
df['sedentario'] = df['actividad_física_(min/sem)'] < 60

#punto 10
df['hipertenso'] = (df['pas'] >= 140) | (df['pad'] >= 90)

#Punto 11
df['metabólicamente_alterado'] = (
    ((df['glucosa'] > 126).astype(int) +
     (df['colesterol'] > 240).astype(int) +
     (df['imc'] > 30).astype(int) +
     (df['sedentario']).astype(int)) >= 2
)

print(df)

#Parte 3

#Punto 12
riesgo_por_region = df.groupby('región')['metabólicamente_alterado'].mean().sort_values(ascending=False)
print("\nRiesgo metabólico por región:")
print(riesgo_por_region)

#Punto 13
sedentarismo_por_mes = df.groupby('mes')['sedentario'].mean().sort_values(ascending=False)
print("\nSedentarismo por mes:")
print(sedentarismo_por_mes)

#Parte 4

#Punto 14
df['clasificación_imc'].value_counts().plot(kind='bar', color='mediumseagreen')
plt.title('Distribución de Clasificación IMC')
plt.xlabel('Clasificación')
plt.ylabel('Cantidad de pacientes')
plt.tight_layout()
plt.show()