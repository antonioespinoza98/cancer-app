import streamlit as st
import folium
from streamlit_folium import st_folium
import desarrollo

def main():

    st.set_page_config("Página Principal")
    st.title('Datos de Cáncer')
    st.caption('Proyecto 4.1: Trabajo Comunitario Universitario 758')
    datos = desarrollo.desplegar_tipo_datos()
    df = desarrollo.tipo(datos)
    tiempo = desarrollo.desplegar_fecha(df)
    sexo = desarrollo.desplegar_sexo(df)
    localizacion = desarrollo.desplegar_zona(df)
    mapa = desarrollo.desplegar_mapa(df, tiempo, sexo, localizacion)
    canton = desarrollo.desplegar_canton(df, mapa)

        #Display Metrics
    st.subheader(f'Datos de incidencia en {canton}')

    col1, col2, col3 = st.columns([1, 2.5, 4])
    with col1:
        desarrollo.desplegar_datos(df, tiempo, sexo, canton, localizacion, '# de casos')
    with col2:
        desarrollo.desplegar_datos(df, tiempo, sexo, canton, localizacion, "Porcentaje del total de casos del país")
    with col3:
        desarrollo.desplegar_datos(df, tiempo, sexo, canton, localizacion, "Tasa de casos por cada 100 000 habitantes")

if __name__ == "__main__":
    main()