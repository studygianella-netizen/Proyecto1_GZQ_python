import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf
st.set_page_config(page_title="Proyecto 1 Python", layout="wide")

st.sidebar.image("python.png")

st.title("PROYECTO 1")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Gianella Zorrilla Quispe")
st.write ("Curso: Especialización en Python potenciado con IA - Edición - 58")
st.write ("2026")
st.image("fondo.png")

menu = st.sidebar.selectbox("Seleccione una opción",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if menu == "Home":
    st.write("Bienvenido a mi aplicación")
    st.write("Descripción del proyecto:")
    st.write("Aplicación interactiva desarrollada en Streamlit como proyecto aplicado del módulo de Fundamentos de Programación. El proyecto integra conceptos esenciales de Python como variables, estructuras de datos, control de flujo, funciones, programación funcional y programación orientada a objetos (POO), mediante una interfaz dinámica e intuitiva.")
    st.write("Tecnologías utilizadas:")
    st.write("Tecnologías utilizadas:")
elif menu == "Ejercicio 1":
    st.title("Flujo de Caja")

elif menu == "Ejercicio 2":
    st.title("Registro de Productos")

elif menu == "Ejercicio 3":
    st.title("Funciones Externas")

elif menu == "Ejercicio 4":
    st.title("CRUD con Clases")
