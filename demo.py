import streamlit as st
import pandas as pd

# Asegúrate de que el archivo 'SalidaFinalVentas.xlsx' esté en el mismo directorio
# que tu script de Streamlit o especifica la ruta completa.

try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  st.dataframe(df)  # Muestra el DataFrame en la aplicación de Streamlit
except FileNotFoundError:
  st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo: {e}")
  
