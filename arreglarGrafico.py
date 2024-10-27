import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO  # Importar StringIO desde io

# Datos de ejemplo en formato CSV
data = """
fecha,ventas
2023-01-01,200
2023-01-02,220
2023-01-03,210
2023-01-04,205
2023-01-05,215
2023-01-06,225
"""

# Cargar los datos en un DataFrame de Pandas
df = pd.read_csv(StringIO(data))  # Usar StringIO para cargar los datos

# Convertir la columna 'fecha' a formato datetime
df['fecha'] = pd.to_datetime(df['fecha'])  # Corregir el nombre de la columna

# Gráfico de líneas de las ventas
plt.figure(figsize=(10, 6))
plt.plot(df['fecha'], df['ventas'], marker='o')  # Añadir marcador para mayor claridad
plt.title("Ventas Diarias")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.grid()  # Añadir una cuadrícula para facilitar la lectura
plt.show()

# Crear un gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(df['fecha'], df['ventas'], color='orange')  # Añadir color para distinguirlo
plt.title("Ventas Diarias")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.grid()  # Añadir cuadrícula
plt.show()

# Crear un histograma de las ventas
plt.figure(figsize=(10, 6))
plt.hist(df['ventas'], bins=5, color='skyblue', edgecolor='black')
plt.title("Distribución de Ventas")
plt.xlabel("Ventas")
plt.ylabel("Frecuencia")
plt.grid()  # Añadir cuadrícula
plt.show()
