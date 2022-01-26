'''
ASIGNATURA: Programación de Aplicaciones con Python
ALUMNO: Ignacio A. Fontal Patac
FECHA: 03/01/2022
ACTIVIDAD: Tema 13 - Streamlit
'''

import streamlit as st
import plotly.express as px

data = px.data.tips()

st.set_page_config(page_title="Tips", page_icon="🧠")

st.sidebar.header("Tips")
menu = st.sidebar.selectbox("Select an option", ['General Graph', 'Smoker or not', 'Sex', 'Trend', 'Day'])

if menu == 'General Graph':
    grafica = px.scatter(data, x='total_bill', y='tip')
    st.write(grafica)

if menu == 'Smoker or not':
    fumador = px.scatter(data, x='total_bill', y='tip', color='smoker')
    st.write(fumador)

if menu == 'Sex':
    sex = px.scatter(data, x='total_bill', y='tip', color='sex', facet_col='smoker')
    st.write(sex)

if menu == 'Trend':
    trend = px.scatter(data, x='total_bill', y='tip', color='sex', trendline='ols', facet_col='smoker')
    st.write(trend)

if menu == 'Day':
    day = px.scatter(data, x='total_bill', y='tip', facet_col='day', facet_row='time', category_orders={'day':['Thur', 'Fri', 'Sat', 'Sun']})
    st.write(day)




st.sidebar.info('Ignacio A. Fontal Patac')
st.sidebar.info('Programación de Aplicaciones con Python')
st.sidebar.info('Tema 13 - Streamlit')
st.sidebar.info('FECHA: 03/01/2022')
