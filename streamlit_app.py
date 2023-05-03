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
    canton = desarrollo.desplegar_canton(desarrollo.incidencia, mapa)

        #Display Metrics
    st.subheader(f'Datos de incidencia en {canton}')

    col1, col2, col3 = st.columns(3)
    with col1:
        desarrollo.desplegar_datos(desarrollo.incidencia, tiempo, sexo, canton, localizacion, '# de casos')
    with col2:
        desarrollo.desplegar_datos(desarrollo.incidencia, tiempo, sexo, canton, localizacion, "Porcentaje del total de casos del país")
    with col3:
        desarrollo.desplegar_datos(desarrollo.incidencia, tiempo, sexo, canton, localizacion, "Porcentaje de casos de cáncer en " + str(localizacion) + " en el país") 

if __name__ == "__main__":
    main()