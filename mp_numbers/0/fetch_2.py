import os
import pandas as pd

URL = 'https://researchbriefings.files.parliament.uk/documents/SN02384/SN02384.xlsx'



#df = pd.read_excel(URL, sheet_name=1)
##403 forbidden

IN_PATH = os.path.join('mp_numbers','0','SN02384.xlsx')
OUT_PATH = os.path.join('mp_numbers','1','mps.csv')

df = pd.read_excel(IN_PATH,sheet_name=1,header=2,usecols=[0,3,4,5],names=['ge','asembled','dissolved','number'])

df['asembled'] = pd.to_datetime(df['asembled'],dayfirst=True)
df['dissolved'] = pd.to_datetime(df['dissolved'],dayfirst=True)
df.to_csv(OUT_PATH,index=False)