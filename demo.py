# prompt: arma una grafica de las ventas por region del dataframe df usando Streamlit

import plotly.express as px

# ... (tu código existente) ...

try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')

  # Suponiendo que tu DataFrame tiene columnas 'Region' y 'Ventas'
  # Ajusta los nombres de las columnas si son diferentes
  fig = px.bar(df, x='Region', y='Ventas', title='Ventas por Región')
  st.plotly_chart(fig)

except FileNotFoundError:
  st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
except KeyError as e:
    st.error(f"Error: La columna '{e}' no se encontró en el DataFrame. Asegúrate de que el archivo tenga las columnas 'Region' y 'Ventas'.")
except Exception as e:
  st.error(f"Ocurrió un error al generar la gráfica: {e}")
