import tradingeconomics as te
import pandas as pd
# Google spread sheets
from openpyxl import Workbook
from openpyxl import load_workbook

te.login('B44ECBFF555A4C8:405D4DAF7CD24C1')  # indicar credenciales

def LeeData(indicador,fecha):
  df=pd.DataFrame(
      te.getHistoricalData(country='Mexico', # Pais
                          indicator=f'{indicador}',  # indicador
                          initDate=f'{fecha}') #fecha inicial
      )
  return df

def pandas_to_xls(df,archivo,sheet, r=1,c=1):
  with pd.ExcelWriter(archivo,date_format="YYYY-MM-DD",
                      mode="a", engine="openpyxl",
                      if_sheet_exists='replace') as writer:
    writer.book = load_workbook(archivo)
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    df.to_excel(writer, sheet_name=sheet,startrow=r-1,startcol=c-1,header=False)
    writer.save()

archivo='archivo.xlsx'  #<--- Cambiar aqui el nombre del archivo-------
inicio='2015-01-01' #fecha de inicio con formato aaaa-mm-dd

#indicadores  --v------ Cambiar aqui ----v---
indicadores=['GDP','GDP from construction']
#hoja y posicion  ---v----- Cambiar aqui ----v---
tab=[('PIB',2,1),('PIB por actividad',2,1)]

for ind,t in zip(indicadores,tab):
  #lee informacion de GDP
  df=LeeData(indicador=ind,fecha=inicio)
  print(df.head())
  #guarda informacion en la hoja
  pandas_to_xls(df,archivo,t[0],t[1],t[2])