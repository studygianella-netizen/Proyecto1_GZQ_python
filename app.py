import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lf

from libreria_clases_proyecto1 import Empleado
st.set_page_config(page_title="Proyecto 1 Python", layout="wide")




# =====================================================
# SESSION STATE
# =====================================================

if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

if "productos" not in st.session_state:
    st.session_state.productos = []

if "historial_funciones" not in st.session_state:
    st.session_state.historial_funciones = []

if "empleados" not in st.session_state:
    st.session_state.empleados = []

# =====================================================
# FUNCIONES EJERCICIO 3
# =====================================================

def calcular_bono(sueldo, porcentaje):
    bono = sueldo * (porcentaje / 100)
    total = sueldo + bono
    return bono, total

# =====================================================
# CLASE EJERCICIO 4
# =====================================================

class Empleado:

    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo





st.sidebar.image("python.png")

st.title("PROYECTO 1")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Gianella Zorrilla Quispe")
st.write ("Curso: Especialización en Python potenciado con IA - Edición - 58")
st.write ("Año: 2026")
st.image("fondo.png")

menu = st.sidebar.selectbox("Seleccione una opción",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])



if menu == "Home":
    st.write("Bienvenido a mi aplicación")
    st.write("Descripción del proyecto:")
    st.write("Aplicación interactiva desarrollada en Streamlit como proyecto aplicado del módulo de Fundamentos de Programación. El proyecto integra conceptos esenciales de Python como variables, estructuras de datos, control de flujo, funciones, programación funcional y programación orientada a objetos (POO), mediante una interfaz dinámica e intuitiva.")
    st.write("Tecnologías utilizadas:")
    st.write("""
    - Python
    - Streamlit
    - Pandas
    - NumPy
    """)



elif menu == "Ejercicio 1":
    st.title("Flujo de Caja")
    st.markdown("""
    En este ejercicio se registran ingresos y gastos para calcular
    el flujo de caja final.
        """)

    concepto = st.text_input("Concepto")

    tipo = st.selectbox(
        "Tipo de Movimiento",
        ["Ingreso", "Gasto"]
    )

    valor = st.number_input(
        "Valor",
        min_value=0.0,
        step=1.0
    )

    if st.button("Agregar Movimiento"):

        movimiento = {
            "Concepto": concepto,
            "Tipo": tipo,
            "Valor": valor
        }

        st.session_state.movimientos.append(movimiento)

        st.success("Movimiento agregado correctamente")

    if len(st.session_state.movimientos) > 0:

        df_movimientos = pd.DataFrame(st.session_state.movimientos)

        st.write("### Movimientos Registrados")

        st.dataframe(df_movimientos)

        ingresos = df_movimientos[df_movimientos["Tipo"] == "Ingreso"]["Valor"].sum()

        gastos = df_movimientos[df_movimientos["Tipo"] == "Gasto"]["Valor"].sum()

        saldo = ingresos - gastos

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Ingresos", f"S/ {ingresos:.2f}")
        col2.metric("Total Gastos", f"S/ {gastos:.2f}")
        col3.metric("Saldo Final", f"S/ {saldo:.2f}")

        if saldo >= 0:
            st.success("El flujo de caja está A FAVOR")
        else:
            st.error("El flujo de caja está EN CONTRA")



elif menu == "Ejercicio 2":
    st.title("Registro de Productos")

    st.markdown("""
    Registro de productos utilizando NumPy y DataFrames.
    """)

    producto = st.text_input("Nombre del Producto")

    categoria = st.selectbox("Categoría",
        ["Tecnología","Oficina","Hogar","Educación"])

    precio = st.number_input("Precio", min_value=0.0, step=1.0)

    cantidad = st.number_input("Cantidad", min_value=1, step=1)

    if st.button("Agregar Producto"):

        total = precio * cantidad

        registro = np.array([
            producto,
            categoria,
            precio,
            cantidad,
            total
        ], dtype=object)

        st.session_state.productos.append(registro)

        st.success("Producto agregado correctamente")

    if len(st.session_state.productos) > 0:

        df_productos = pd.DataFrame(
            st.session_state.productos,
            columns=["Producto","Categoría","Precio","Cantidad","Total"])

        st.write("### Productos Registrados")

        st.dataframe(df_productos)



elif menu == "Ejercicio 3":
    st.title("Funciones Externas")
    st.markdown("""
    En este ejercicio se utiliza una función para calcular
    bonos salariales.
    """)

    sueldo = st.number_input("Ingrese el sueldo",
        min_value=0.0,
        step=100.0)

    porcentaje = st.number_input("Ingrese porcentaje de bono",
        min_value=0.0,
        max_value=100.0,
        step=1.0)

    if st.button("Calcular Bono"):

        bono, total = calcular_bono(sueldo, porcentaje)

        st.write(f"### Bono: S/ {bono:.2f}")
        st.write(f"### Total a recibir: S/ {total:.2f}")

        historial = {
            "Sueldo": sueldo,
            "Porcentaje": porcentaje,
            "Bono": bono,
            "Total": total
        }

        st.session_state.historial_funciones.append(historial)

    if len(st.session_state.historial_funciones) > 0:

        df_historial = pd.DataFrame(
            st.session_state.historial_funciones
        )

        st.write("### Historial")

        st.dataframe(df_historial)



elif menu == "Ejercicio 4":
    st.title("CRUD con Clases")
    st.markdown("""
    Sistema CRUD utilizando Programación Orientada a Objetos (POO)
    con clases importadas desde una librería externa.
    """)

    # =================================================
    # CREAR
    # =================================================

    st.subheader("Crear Empleado")

    nombre = st.text_input("Nombre del Empleado")

    cargo = st.text_input("Cargo")

    sueldo = st.number_input(
        "Sueldo",
        min_value=0.0,
        step=100.0
    )

    if st.button("Guardar Empleado"):

        if nombre != "" and cargo != "":

            nuevo_empleado = Empleado(
                nombre,
                cargo,
                sueldo
            )

            st.session_state.empleados.append(
                nuevo_empleado.mostrar_datos()
            )

            st.success("Empleado registrado correctamente")

        else:

            st.error("Complete todos los campos")

    # =================================================
    # LEER
    # =================================================

    if len(st.session_state.empleados) > 0:

        st.subheader("Lista de Empleados")

        df_empleados = pd.DataFrame(
            st.session_state.empleados
        )

        st.dataframe(df_empleados)

        # =============================================
        # ACTUALIZAR
        # =============================================

        st.subheader("Actualizar Empleado")

        indice_actualizar = st.selectbox(
            "Seleccione empleado",
            range(len(st.session_state.empleados)),
            format_func=lambda x:
            st.session_state.empleados[x]["Nombre"]
        )

        nuevo_nombre = st.text_input(
            "Nuevo Nombre"
        )

        nuevo_cargo = st.text_input(
            "Nuevo Cargo"
        )

        nuevo_sueldo = st.number_input(
            "Nuevo Sueldo",
            min_value=0.0,
            step=100.0,
            key="nuevo_sueldo"
        )

        if st.button("Actualizar Empleado"):

            if nuevo_nombre != "":
                st.session_state.empleados[indice_actualizar]["Nombre"] = nuevo_nombre

            if nuevo_cargo != "":
                st.session_state.empleados[indice_actualizar]["Cargo"] = nuevo_cargo

            st.session_state.empleados[indice_actualizar]["Sueldo"] = nuevo_sueldo

            st.success("Empleado actualizado correctamente")

        # =============================================
        # ELIMINAR
        # =============================================

        st.subheader("Eliminar Empleado")

        indice_eliminar = st.selectbox(
            "Seleccione empleado a eliminar",
            range(len(st.session_state.empleados)),
            format_func=lambda x:
            st.session_state.empleados[x]["Nombre"],
            key="eliminar"
        )

        if st.button("Eliminar Empleado"):

            st.session_state.empleados.pop(
                indice_eliminar
            )

            st.warning("Empleado eliminado correctamente")
