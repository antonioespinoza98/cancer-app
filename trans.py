import script
import pandas as pd
import folium
from streamlit_folium import st_folium
cancer_edad = pd.DataFrame(script.mort_cancer_edad)


def desplegar_mapa():

    mapa = folium.Map(location=[9.748917, -83.753428], zoom_start=7.2, scrollWheelZoom = False, titles = 'Carto')
    choropleth = folium.Choropleth(
         geo_data='prueba_c.geojson'
     )
    choropleth.geojson.add_to(mapa)
    st_map = st_folium(mapa, width=700, height=450)