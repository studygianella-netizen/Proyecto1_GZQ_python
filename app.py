import streamlit as st
import numpy as np
import libreria_funciones as lf
st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Gianella Z")

st.sidebar.image("Image20260512194119.png")

sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"] )

if sesion == "Sesión 1":
  st.write("Bienvenido la sesión 1")
  st.image("Image20260512194059.png" )


   cuota = round(lf.cuota_prestamo(principal, tasa_anual, anios, pagos_anio),2)
   st.write(f"El valor de la cuota es {cuota}")
