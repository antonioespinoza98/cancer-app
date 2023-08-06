# Otros scripts
import script
# Librerias
import pandas as pd
# Pasamos el archivo a un DataFrame de Pandas
incidencia = pd.DataFrame(script.inc_cancer_canton)

# Error: Cuando la función desplegar mapa intenta desplegar los datos del 2012 y 2014, no encuentra los datos para Zarcero
# Haciendo un poco de análisis, en las tablas crudas de datos, estos no existen. Entonces tenemos que pensar en una forma de solucionar esto
# para los datos totales, mi propuesta para este error es hacer una función que pueda detectar datos faltantes en el archivo
# geojson y el archivo de excel y que cuando encuentre incogruencias entonces que le asigne un valor de cero o nulo para que el mapa funcione

for i in incidencia["ANO"].unique():
    
    print(i,incidencia["CANTON"].nunique())

# Al parecer para cada año hay 82 cantones exactos, sin embargo ahora hay que ver por qué Zarcero no está en 2012 ni 2014, pero cumple igual con la cantidad

# get a list of unique years in the dataframe
years = incidencia['ANO'].unique()

# get the list of districts for the base year (2012)
base_districts = set(incidencia[incidencia['ANO'] == 2012]['CANTON'].unique())

# iterate through each year after the base year and compare it with the base year
for i in range(1, len(years)):
    curr_year = years[i]

    # get the list of districts for the current year
    curr_districts = set(incidencia[incidencia['ANO'] == curr_year]['CANTON'].unique())

    # get the list of districts that are in curr_year but not in the base year
    missing_districts = list(base_districts - curr_districts)

    # print out the missing districts for this year comparison
    print(f"The year 2012 is missing these districts when compared to year {curr_year}: {missing_districts}")

#2013

# get a list of unique years in the dataframe
years = incidencia['ANO'].unique()

# get the list of districts for the base year (2012)
base_districts = set(incidencia[incidencia['ANO'] == 2013]['CANTON'].unique())

# iterate through each year after the base year and compare it with the base year
for i in range(1, len(years)):
    curr_year = years[i]

    # get the list of districts for the current year
    curr_districts = set(incidencia[incidencia['ANO'] == curr_year]['CANTON'].unique())

    # get the list of districts that are in curr_year but not in the base year
    missing_districts = list(base_districts - curr_districts)

    # print out the missing districts for this year comparison
    print(f"The year 2013 is missing these districts when compared to year {curr_year}: {missing_districts}")

#2014

# get a list of unique years in the dataframe
years = incidencia['ANO'].unique()

# get the list of districts for the base year (2012)
base_districts = set(incidencia[incidencia['ANO'] == 2014]['CANTON'].unique())

# iterate through each year after the base year and compare it with the base year
for i in range(1, len(years)):
    curr_year = years[i]

    # get the list of districts for the current year
    curr_districts = set(incidencia[incidencia['ANO'] == curr_year]['CANTON'].unique())

    # get the list of districts that are in curr_year but not in the base year
    missing_districts = list(base_districts - curr_districts)

    # print out the missing districts for this year comparison
    print(f"The year 2014 is missing these districts when compared to year {curr_year}: {missing_districts}")

# 2015

# get a list of unique years in the dataframe
years = incidencia['ANO'].unique()

# get the list of districts for the base year (2012)
base_districts = set(incidencia[incidencia['ANO'] == 2015]['CANTON'].unique())

# iterate through each year after the base year and compare it with the base year
for i in range(1, len(years)):
    curr_year = years[i]

    # get the list of districts for the current year
    curr_districts = set(incidencia[incidencia['ANO'] == curr_year]['CANTON'].unique())

    # get the list of districts that are in curr_year but not in the base year
    missing_districts = list(base_districts - curr_districts)

    # print out the missing districts for this year comparison
    print(f"The year 2015 is missing these districts when compared to year {curr_year}: {missing_districts}")
