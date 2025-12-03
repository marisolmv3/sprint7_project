import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Data Analysis of Vehicles in the US - Project Sprint 7') # agregar un encabezado
st.write("Student: Marisol Mata Villegas")

st.subheader("Data viewer") # agregar un título
# crear una casilla de verificación
build_table= st.checkbox('Include manufactures with less than 1000 ads') 

# Build a table with all the columns of the dataset that according to the checkbox
if build_table:
    st.write(car_data)
else:
    filtered_data = car_data['days_listed'].value_counts()
    filtered_data = filtered_data[filtered_data >= 1000]
    st.write(car_data[car_data['days_listed'].isin(filtered_data.index)])


st.subheader("Vehicle types by manufacter") # agregar un título
# crear un gráfico de barras donde el eje x sea el modelo del vículo (model) y el eje y sea el conteo de tipos de vehículos por modelo (type), mostar solo los 15 modelos con más anuncios
top_15_models = car_data['model'].value_counts().nlargest(15).index
filtered_data = car_data[car_data['model'].isin(top_15_models)]
fig = px.histogram(filtered_data, x='model', color='type', labels={'model':'Vehicle Model', 'count':'Count of Vehicle Types'})
st.plotly_chart(fig) # mostrar el gráfico en la aplicación



st.subheader("Histogram of condition vs model_year") # agregar un título
# crear un histograma donde el eje x sea el año del modelo (model_year) y el eje y sea el conteo de la condición del vehículo (condition)
fig2 = px.histogram(car_data, x='model_year', color='condition', labels={'model_year':'model_year', 'count':'Count of Condition'})
st.plotly_chart(fig2) # mostrar el gráfico en la aplicación

# Compare price distribution (price) between manufacturers (model) using a bar plot
st.subheader("Compare price distribution between manufacturers") # agregar un título
# Seleccionar fabricantes para comparar en dos listas desplegables
manufacturer_1 = st.selectbox('Select first manufacturer', car_data['model'].unique(), index=0)
manufacturer_2 = st.selectbox('Select second manufacturer', car_data['model'].unique(), index=1)
st.write(f'Comparing price distribution between {manufacturer_1} and {manufacturer_2}')
fig3 = px.histogram(car_data[car_data['model'].isin([manufacturer_1, manufacturer_2])], x='model', y='price', labels={'model':'Manufacturer', 'price':'Price'})
st.plotly_chart(fig3) # mostrar el gráfico en la aplicación


# Agregar un slider
st.subheader(f'Construir un histograma para la columna odómetro con bins')
num_bins = st.slider('Selecciona el número de bins para el histograma de odómetro', min_value=5, max_value=100, value=20, step=5)
st.write(f'Construir un histograma para la columna odómetro con {num_bins} bins')
fig = px.histogram(car_data, x="odometer", nbins=num_bins)
st.plotly_chart(fig, use_container_width=True)


# Agregar un grafico de dispersion
# Seleccionar columnas para el eje x e y
x_column = st.selectbox('Selecciona la columna para el eje X', car_data.columns, index=car_data.columns.get_loc('model_year'))
y_column = st.selectbox('Selecciona la columna para el eje Y', car_data.columns, index=car_data.columns.get_loc('price'))
st.subheader(f'Construir un gráfico de dispersión para {x_column} vs {y_column}')
fig = px.scatter(car_data, x=x_column, y=y_column)  
st.plotly_chart(fig, use_container_width=True)  
