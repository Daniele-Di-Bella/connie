import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Imposta i permessi necessari
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Inserisci il percorso al tuo file di credenziali
cred_path = 'percorso/al/tuo/file/cred.json'

# Autenticazione con il tuo file di credenziali
credentials = ServiceAccountCredentials.from_json_keyfile_name(cred_path, scope)

# Inizializza l'oggetto gspread con le credenziali
gc = gspread.authorize(credentials)

# ID del foglio di calcolo Google Sheet
spreadsheet_id = 'ID_del_tuo_foglio'

# Nome del foglio all'interno del foglio di calcolo
sheet_name = 'Nome_del_tuo_foglio'

# Apri il foglio di calcolo
worksheet = gc.open_by_key(spreadsheet_id).worksheet(sheet_name)

# Ottieni tutti i dati dal foglio di calcolo come lista di dizionari
data = worksheet.get_all_records()

# Converti la lista di dizionari in un DataFrame di Pandas
df = pd.DataFrame(data)

# Ora puoi utilizzare df come qualsiasi DataFrame di Pandas
print(df.head())
