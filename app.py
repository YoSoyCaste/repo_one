import pandas as pd
import plotly.express as px
import streamlit as st

# Lee data
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para histograma.
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    # Mensaje
    st.write('Creación de un histograma con los odómetros de los coches del conjunto de datos')
    
    # Crea histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Muestra histograma
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
build_scatter_plot = st.checkbox('Construir un gráfico de dispersión')

if build_scatter_plot:
    # Mensaje
    st.write('Creación de un gráfico de dispersión entre la relación de Precio VS Odómetro de los coches en el conjunto de datos')
    
    # Crea gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="price", y="odometer", title="Precio vs. Odómetro")
    
    # Muestra gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)