# prompt: arma una gráfica de la sales por region del dataframe df usando streamlit

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# Asegúrate de que el archivo 'SalidaFinalVentas.xlsx' esté en el mismo directorio
# que tu notebook de Colab o especifica la ruta completa.

try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  print(df.head())  # Muestra las primeras filas del DataFrame para verificar la lectura.
except FileNotFoundError:
  print("Error: El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
except Exception as e:
  print(f"Ocurrió un error al leer el archivo: {e}")



# Asegúrate de que el archivo 'SalidaFinalVentas.xlsx' esté en el mismo directorio
# que tu script de Streamlit o especifica la ruta completa.

try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  st.dataframe(df)  # Muestra el DataFrame en la aplicación de Streamlit

  # Agrupa las ventas por región
  sales_by_region = df.groupby('Region')['Sales'].sum()

  # Crea una gráfica de barras
  st.subheader('Ventas por Región')
  fig, ax = plt.subplots()
  ax.bar(sales_by_region.index, sales_by_region.values)
  ax.set_xlabel('Región')
  ax.set_ylabel('Ventas Totales')
  st.pyplot(fig)

except FileNotFoundError:
  st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo: {e}")
