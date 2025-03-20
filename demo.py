import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# ... (tu código existente para leer el archivo Excel) ...

# Suponiendo que tu DataFrame tiene columnas 'Region' y 'Sales'
if 'Region' in df.columns and 'Sales' in df.columns:
    st.header("Ventas por Región")

    # Agrupar las ventas por región
    ventas_por_region = df.groupby('Region')['Sales'].sum()

    # Crear la gráfica de barras
    fig, ax = plt.subplots()
    ventas_por_region.plot(kind='bar', ax=ax)
    ax.set_xlabel("Región")
    ax.set_ylabel("Ventas Totales")
    ax.set_title("Ventas por Región")

    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)
else:
    st.error("El DataFrame no contiene las columnas 'Region' y 'Sales' necesarias para generar la gráfica.")
