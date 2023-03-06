import gspread
from oauth2client.service_account import ServiceAccountCredentials

myscope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file',
           'https://www.googleapis.com/auth/drive']
mycreds = ServiceAccountCredentials.from_json_keyfile_name('accesos/cancerapp-379721-c41349f688a2.json',myscope)
myclient = gspread.authorize(mycreds)

mysheet = myclient.open("cancer").worksheet('hoja1')

data = mysheet.get_all_records()

row = mysheet.row_values(3)

print(row)