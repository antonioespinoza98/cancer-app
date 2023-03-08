import script
import pandas as pd

cancer_edad = pd.DataFrame(script.mort_cancer_edad)

import folium
from IPython.display import  display

myMap = folium.Map(location = [9.748917, -83.753428])

myMap.save("CostaRica.html")