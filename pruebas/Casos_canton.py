import streamlit as st
from folium import plugins
import script
import pandas as pd
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
from branca.colormap import StepColormap
from colour import Color
import branca.colormap as cm
from branca.colormap import LinearColormap
import numpy as np 
cancer_edad = pd.DataFrame(script.mort_cancer_edad)
dataincidencia = pd.DataFrame(script.inc_cancer_canton)

#bins = [0, 400,546,987, 1000,3004, 4000,7478,8000,9000,10000, np.inf]

def desplegar_mapa(df):

    mapa = folium.Map(location=[9.748917, -83.753428], zoom_start=7.2, scrollWheelZoom = False, titles = 'Carto')
    #folium.TileLayer('Stamen Terrain').add_to(mapa)
    choropleth = folium.Choropleth(
         geo_data='cantonescanas.geojson',
         data=df,
         columns=("CANTON","INCIDENCIA"),
         key_on="feature.properties.Canton",
         highlight=True,
         fill_color="YlOrRd",
         fill_opacity=0.7,
         line_opacity=0.7,
         #bins = bins,
         legend_name="prueba de datos",
         reset = True

     )
    choropleth.geojson.add_to(mapa)
    df = dataincidencia.set_index("CANTON")
    canton = "SAN JOSE"

    for feature in choropleth.geojson.data["features"]:
        canton =feature["properties"]["Canton"]
        feature["properties"]["Provincia"] = "Casos : " + str(df.loc[canton,"INCIDENCIA"][0])


    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(["Canton","Provincia"],labels = False)
    )
    st_map = st_folium(mapa, width=700, height=450)
