import os
import pandas as pd

URL = 'https://researchbriefings.files.parliament.uk/documents/SN02384/SN02384.xlsx'

PATH = os.path.join('lords_by_party','3','mps.csv')

df = pd.read_excel(URL, sheet_name=1)
df.to_csv(PATH)

##403 forbidden