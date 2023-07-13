import gspread
from oauth2client.service_account import ServiceAccountCredentials

myscope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file',
           'https://www.googleapis.com/auth/drive']
mycreds = ServiceAccountCredentials.from_json_keyfile_name('accesos/cancerapp-379721-c41349f688a2.json',myscope)
myclient = gspread.authorize(mycreds)

mort_cant = myclient.open("cancer").worksheet('mortalidad')
inc_cant = myclient.open("cancer").worksheet('incidencia')
fondo = """
<style>
[data-testid]
</style>
"""

# Deberíamos de utilizar nombres específicos para todos los scripts
# por ejemplo para traer los datos debería ser {causa}_{enfermedad}_{edad}, entonces debería de ser: mort_cancer_edad

mort_cancer_canton = mort_cant.get_all_records()
inc_cancer_canton = inc_cant.get_all_records()

