import gspread
from oauth2client.service_account import ServiceAccountCredentials

myscope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file',
           'https://www.googleapis.com/auth/drive']
mycreds = ServiceAccountCredentials.from_json_keyfile_name('accesos/cancerapp-379721-c41349f688a2.json',myscope)
myclient = gspread.authorize(mycreds)

mysheet = myclient.open("cancer").worksheet('hoja1')


# Deberíamos de utilizar nombres específicos para todos los scripts
# por ejemplo para traer los datos debería ser {causa}_{enfermedad}_{edad}, entonces debería de ser: mort_cancer_edad

mort_cancer_edad = mysheet.get_all_records()