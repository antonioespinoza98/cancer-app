import streamlit as st
import folium
from streamlit_folium import st_folium
import trans

def main():

    st.set_page_config("Página Principal")
    st.title('Datos de Cáncer')
    st.caption('Proyecto 4.1: Trabajo Comunitario Universitario 758')
    mapa =  trans.desplegar_mapa()
if __name__ == "__main__":
    main()