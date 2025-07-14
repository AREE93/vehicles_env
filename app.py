import pandas as pd
import plotly.graph_objects as go
import streamlit as st
dataraw = pd.read_csv('vehicles_us.csv')

st.header('Venta de vehículos')
histo_button = st.button('Generar histográma')

if histo_button:
    st.write('Creación de un histográma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=dataraw['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

