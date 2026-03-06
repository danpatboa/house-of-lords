import os
import pandas as pd

URL = 'https://api-test.yougov.com/public-data/v5/uk/trackers/how-should-the-house-of-lords-be-made-up-of/download/'
PATH = os.path.join('polling','1','{}.csv')

xl = pd.ExcelFile(URL)

for sheet_name in xl.sheet_names:
    df = pd.read_excel(xl, sheet_name=sheet_name)
    df = df.rename(columns={df.columns[0]: 'answer'})
    df.to_csv(PATH.format(sheet_name),index=False)