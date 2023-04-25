import streamlit as st
import folium
from streamlit_folium import st_folium
import desarrollo

def main():

    st.set_page_config("Página Principal")
    st.title('Datos de Cáncer')
    st.caption('Proyecto 4.1: Trabajo Comunitario Universitario 758')
    tiempo = desarrollo.desplegar_fecha(desarrollo.incidencia)
    sexo = desarrollo.desplegar_sexo(desarrollo.incidencia)
    localizacion = desarrollo.desplegar_zona(desarrollo.incidencia)
    mapa = desarrollo.desplegar_mapa(desarrollo.incidencia, tiempo, sexo, localizacion)
    mapa = desarrollo.desplegar_canton(desarrollo.incidencia, mapa)
if __name__ == "__main__":
    main()