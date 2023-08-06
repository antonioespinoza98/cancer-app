# Otros scripts
import script
# Librerias
import pandas as pd
import folium
from streamlit_folium import st_folium
import streamlit as st
# Pasamos el archivo a un DataFrame de Pandas
INCIDENCIA = pd.DataFrame(script.inc_cancer_canton)
MORTALIDAD = pd.DataFrame(script.mort_cancer_canton)

# Filtro para mortalidad o incidencia

def desplegar_tipo_datos():
    return st.sidebar.radio('TIPO DE DATOS', ['INCIDENCIA', 'MORTALIDAD'])

def tipo(tipo):
    if tipo == 'INCIDENCIA':
        return INCIDENCIA
    else:
        return MORTALIDAD

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
    lista_canton = list(df['CANTON'].unique())
    lista_canton.sort()
    lista_canton = ["COSTA RICA"] + lista_canton
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
         columns = ('CANTON','TASA'),
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
        if(func_sexo=='FEMENINO') and  (func_localizacion=='PROSTATA'):
            df.loc[canton, "INCIDENCIA"] = 0
            feature["properties"]["Provincia"] = "Casos : " + str(df.loc[canton, "INCIDENCIA"])+ "Tasa de incidencia por 100 000 habitantes: " +  str(df.loc[canton, "TASA"])
            feature["properties"]["Dato"] = "Tasa de casos por 100 000 habitantes : " + str(round(df.loc[canton, "TASA"],2))        
            feature["properties"]["Poblacion"] = "Población del cantón : " + str((df.loc[canton, "POBLACION"]))
        elif(func_sexo=='MASCULINO') and  (func_localizacion=='MAMA'):
            df.loc[canton, "INCIDENCIA"] = 0
            feature["properties"]["Provincia"] = "Casos : " + str(df.loc[canton, "INCIDENCIA"])    
            feature["properties"]["Dato"] = "Tasa de casos por 100 000 habitantes : " + str(round(df.loc[canton, "TASA"],2))
            feature["properties"]["Poblacion"] = "Población del cantón : " + str((df.loc[canton, "POBLACION"]))
        elif ((func_sexo!='TODOS') and  (func_localizacion!='TODAS')):
            feature["properties"]["Provincia"] = "Casos : " + str(df.loc[canton, "INCIDENCIA"])
            feature["properties"]["Dato"] = "Tasa de casos por 100 000 habitantes : " + str(round(df.loc[canton, "TASA"],2))
            feature["properties"]["Poblacion"] = "Población del cantón : " + str((df.loc[canton, "POBLACION"]))
        elif ((func_sexo=='TODOS') and  (func_localizacion=='PROSTATA')):
            feature["properties"]["Provincia"] = "Casos : " + str(df.loc[canton, "INCIDENCIA"])
            feature["properties"]["Dato"] = "Tasa de casos por 100 000 habitantes : " + str(round(df.loc[canton, "TASA"],2))    
            feature["properties"]["Poblacion"] = "Población del cantón : " + str((df.loc[canton, "POBLACION"]))
        else:
            feature["properties"]["Provincia"] = "Casos : " + str(sum(df.loc[canton, "INCIDENCIA"]))
            feature["properties"]["Dato"] = "Tasa de casos por 100 000 habitantes : " + str(round(df.loc[canton, "TASA"],2))
            feature["properties"]["Poblacion"] = "Población del cantón : " + str((df.loc[canton, "POBLACION"]))
        if(func_localizacion=='TODAS' or (func_localizacion!='TODAS' and func_sexo=='TODOS')):
            feature["properties"]["Poblacion"] = "Población del cantón : " + str(max(df.loc[canton, "POBLACION"])+min(df.loc[canton, "POBLACION"]))
            feature["properties"]["Dato"] = "Tasa de casos por 100 000 habitantes : " + str(round(sum(df.loc[canton, "INCIDENCIA"])/(max(df.loc[canton, "POBLACION"])+min(df.loc[canton, "POBLACION"]))*100000,2))
       

        

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(["Canton","Provincia","Dato", "Poblacion"],labels = False)
    )

    st_map = st_folium(mapa, width=700, height=450)


#Función de cuadro de datos
def desplegar_datos(df, func_ano, func_sexo, canton, func_localizacion, title):
    df = df[(df['ANO'] == func_ano)]
    df_total = df
    if func_localizacion=='TODAS':
        df = df
    else: 
        df = df[(df['LOCALIZACION']==func_localizacion)]
    df_localizacion = df
    if canton == "COSTA RICA":
        df = df
    else:
        df = df[(df['CANTON'] == canton)]
    if func_sexo=='TODOS':
        df = df
    else: 
        df = df[(df['SEXO']==func_sexo)]
    df.drop_duplicates(inplace=True)
    if title == "# de casos":
        if ((func_sexo!='TODOS') and  (func_localizacion!='TODAS')):
            total=  sum(df["INCIDENCIA"])
        else:
            total = sum(df["INCIDENCIA"])
        st.metric(title, str(round(total)))
    elif title == "Porcentaje del total de casos del país":
        if ((func_sexo!='TODOS') and  (func_localizacion!='TODAS')):
            total= (sum(df["INCIDENCIA"]) / sum(df_total["INCIDENCIA"]) *100)
        else:
            total = (sum(df["INCIDENCIA"]) / sum(df_total["INCIDENCIA"]) *100)
        st.metric(title, str(round(total,ndigits=2)))
    elif title == "Tasa de casos por cada 100 000 habitantes":
            total= df["TASA"]
    if(func_sexo=='FEMENINO') and  (func_localizacion=='PROSTATA'):
        total=0

    