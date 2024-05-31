import streamlit as st
import string
import random
import pyperclip


def generar(long, dig=False, upp=False, punct=False):
    let = string.ascii_lowercase
    num = string.digits if dig else ""
    simb = string.punctuation if punct else ""
    may = string.ascii_uppercase if upp else ""
    caracteres = let + num + simb + may
    longi = int(long)
    contrasena = "".join(random.choice(caracteres) for i in range(int(longi)))
    return contrasena

st.markdown("<h1 style='text-align:center;'>Generador de Contraseñas</h1>", unsafe_allow_html=True)
st.markdown("---")
long = st.number_input(label="Ingrese el el largo de la contraseña requerida: ",value=0)
st.markdown("<h3>Opciones de Contraseña</h3>", unsafe_allow_html=True)
digito = st.toggle(label="Números")
mayuscula = st.toggle(label="Mayúsculas")
simbolo = st.toggle(label="Símbolos")
btn = st.button(label="Generar Contraseña")
if btn:
    pswd = generar(long,digito,mayuscula,simbolo)
    w = st.code(pswd, language="python")
  
