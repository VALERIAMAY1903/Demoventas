# prompt: arma una grafica de las sales por region del dataframe df usando streamlit

import pandas as pd
import streamlit as st
import plotly.express as px


# Lee el archivo Excel
try:
    df = pd.read_excel('SalidaFinalVentas.xlsx')
    print(df.head()) # Muestra las primeras filas del DataFrame
except FileNotFoundError:
    st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no fue encontrado.")
    st.stop() # Detener la ejecución si no se encuentra el archivo
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
    st.stop() # Detener la ejecución si ocurre un error


# Verifica si la columna 'Region' existe en el DataFrame
if 'Region' not in df.columns:
    st.error("Error: La columna 'Region' no se encuentra en el archivo.")
    st.stop()

# Verifica si la columna 'Ventas' existe en el DataFrame. Si no existe, intenta usar 'Sales' como alternativa
if 'Ventas' not in df.columns:
    if 'Sales' in df.columns:
        sales_column = 'Sales'
        st.warning("La columna 'Ventas' no fue encontrada. Usando 'Sales' en su lugar.")
    else:
        st.error("Error: La columna 'Ventas' (ni 'Sales') no se encuentra en el archivo. Asegúrate de que exista una columna llamada 'Ventas' o 'Sales' en tu archivo Excel.")
        st.stop()
else:
    sales_column = 'Ventas'


# Crea la gráfica usando Plotly Express, utilizando la columna correcta para las ventas
fig = px.bar(df, x='Region', y=sales_column, title='Ventas por Región')

# Muestra la gráfica en Streamlit
st.plotly_chart(fig)

# Muestra el DataFrame en Streamlit (opcional)
st.write(df)



# Lee el archivo Excel
try:
    df = pd.read_excel('SalidaFinalVentas.xlsx')
except FileNotFoundError:
    st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no fue encontrado.")
    st.stop()
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
    st.stop()

# Filtro para la columna 'Region'
if 'Region' in df.columns:
    region_filter = st.selectbox('Selecciona una Región', df['Region'].unique())
else:
    st.warning("La columna 'Region' no existe en el DataFrame. No se puede aplicar el filtro de región.")
    region_filter = None

# Filtro para la columna 'State'
if 'State' in df.columns:
    state_filter = st.selectbox('Selecciona un Estado', df['State'].unique())
else:
    st.warning("La columna 'State' no existe en el DataFrame. No se puede aplicar el filtro de estado.")
    state_filter = None

# Aplica los filtros
if region_filter is not None and state_filter is not None:
    filtered_df = df[(df['Region'] == region_filter) & (df['State'] == state_filter)]
elif region_filter is not None:
    filtered_df = df[df['Region'] == region_filter]
elif state_filter is not None:
    filtered_df = df[df['State'] == state_filter]
else:
    filtered_df = df  # Si no hay filtros, muestra el DataFrame original

# Muestra el resultado
if not filtered_df.empty:
    st.write(filtered_df)
else:
    st.write("No se encontraron resultados para los filtros seleccionados.")
    # ... (tu código existente de Streamlit) ...

region_filter = st.multiselect("Selecciona las regiones:", df['Region'].unique())
state_filter = st.multiselect("Selecciona los estados:", df['State'].unique())

if region_filter and state_filter:
  df_filtered = df[df['Region'].isin(region_filter) & df['State'].isin(state_filter)]
  st.dataframe(df_filtered)
  if not df_filtered.empty:
    st.write(df_filtered.iloc[0])  # Imprimir solo el primer resultado
elif region_filter:
  df_filtered = df[df['Region'].isin(region_filter)]
  st.dataframe(df_filtered)
  if not df_filtered.empty:
    st.write(df_filtered.iloc[0])  # Imprimir solo el primer resultado
elif state_filter:
  df_filtered = df[df['State'].isin(state_filter)]
  st.dataframe(df_filtered)
  if not df_filtered.empty:
    st.write(df_filtered.iloc[0])  # Imprimir solo el primer resultado
else:
  st.dataframe(df)
# Crea una gráfica de pastel con la columna Category
category_counts = df['Category'].value_counts()
fig, ax = plt.subplots()
ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)
