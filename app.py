import pandas as pd
import plotly.graph_objects as go
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv')

st.header('Venta de vehículos')
histo_check = st.checkbox('Generar histográma')
disper_check = st.checkbox('Generar gráfico de dispersión')

if histo_check:
    st.write('Creación de un histográma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro', y="Odómetro en millas")
    st.plotly_chart(fig, use_container_width=True)
if disper_check:
    st.write('Creación de diagráma de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

