import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf
st.set_page_config(page_title="Proyecto 1 Python", layout="wide")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Gianella Zorrilla Quispe")
st.write ("Especialización en Python potenciado con IA - Edición - 58")

menu = st.sidebar.selectbox(
    "Seleccione una opción",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

if menu == "Home":
    st.title("Proyecto Aplicado en Streamlit")
    st.write("Bienvenido a mi aplicación")

elif menu == "Ejercicio 1":
    st.title("Flujo de Caja")

elif menu == "Ejercicio 2":
    st.title("Registro de Productos")

elif menu == "Ejercicio 3":
    st.title("Funciones Externas")

elif menu == "Ejercicio 4":
    st.title("CRUD con Clases")
