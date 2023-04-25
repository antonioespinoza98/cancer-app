# Otros scripts
import script
# Librerias
import pandas as pd
import folium
from streamlit_folium import st_folium
import streamlit as st
# Pasamos el archivo a un DataFrame de Pandas
incidencia = pd.DataFrame(script.inc_cancer_canton)

# Filtro para el año
def desplegar_fecha(df):
    #primero filtramos por año y sacamos un record por año usando .unique()
    year_list = list(df['ANO'].unique())
    #ordenamos
    year_list.sort()
    year = st.sidebar.selectbox('Año', year_list, len(year_list)-1)
    st.header(f'{year}')
    return year

# Desplegar filtro para el canton
def desplegar_canton(df, func_mapa):
    lista_canton = [''] + list(df['CANTON'].unique())
    lista_canton.sort()
    canton_index = lista_canton.index(func_mapa) if func_mapa and func_mapa in lista_canton else 0
    return st.sidebar.selectbox('CANTON', lista_canton, canton_index)
    
# Filtro para localización anatómica
def desplegar_zona(df):
    lista_zona = ['TODAS'] + list(df['LOCALIZACION'].unique())
    return st.sidebar.selectbox('Localización', lista_zona)

# Filtro para sexo
def desplegar_sexo(df):
    lista_sexo = ['TODOS'] + list(df['SEXO'].unique())
    return st.sidebar.radio('Sexo', lista_sexo,0)
    

# Función del mapa
def desplegar_mapa(df, func_ano, func_sexo, func_localizacion):
    df = df[(df['ANO'] == func_ano)]
    if func_sexo=='TODOS':
        df = df
    else: 
        df = df[(df['SEXO']==func_sexo)]
    if func_localizacion=='TODAS':
        df = df
    else: 
        df = df[(df['LOCALIZACION']==func_localizacion)]
    mapa = folium.Map(location=[9.748917, -83.753428], zoom_start=7.2, scrollWheelZoom = False, titles = 'Carto')
    choropleth = folium.Choropleth(
         geo_data='cantones.geojson',
         data = df,
         columns = ('CANTON','INCIDENCIA'),
         key_on= 'feature.properties.Canton',
         fill_color="YlOrRd",
         fill_opacity=0.7,
         line_opacity=0.2,
         legend_name="Incidencia de Cáncer"
     )
    choropleth.geojson.add_to(mapa)
    # Cuadro en el mapa
    df = df.set_index("CANTON")
   
    for feature in choropleth.geojson.data["features"]:
        canton =feature["properties"]["Canton"]
        if ((func_sexo!='TODOS') and  (func_localizacion!='TODAS')):
            # If it's a single integer, convert it to a string
            feature["properties"]["Provincia"] = "Casos : " + str(df.loc[canton, "INCIDENCIA"])
        else:
            # If it's a list of integers, add them up and convert the result to a string
            feature["properties"]["Provincia"] = "Casos : " + str(sum(df.loc[canton, "INCIDENCIA"]))

        

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(["Canton","Provincia"],labels = False)
    )

    st_map = st_folium(mapa, width=700, height=450)