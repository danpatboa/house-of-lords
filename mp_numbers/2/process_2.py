import os
import pandas as pd

IN_PATH = os.path.join('lords_by_party','0','SN02384.xlsx')
OUT_PATH = os.path.join('lords_by_party','5','mps.csv')

df = pd.read_excel(IN_PATH,sheet_name=1,header=2,usecols=[0,3,4,5],names=['ge','asembled','dissolved','number'])
df = df[df['ge'] >= 1997]

df['asembled'] = pd.to_datetime(df['asembled'])
df['dissolved'] = pd.to_datetime(df['dissolved']).fillna(pd.Timestamp.today())


# Expand each row into monthly intervals
monthly_rows = []
for _, row in df.iterrows():
    months = pd.date_range(start=row['asembled'], end=row['dissolved'], freq='MS')
    for month in months:
        monthly_rows.append({'date': month, 'number': row['number']})

monthly_df = pd.DataFrame(monthly_rows)

# If multiple rows overlap the same month, sum (or use another agg e.g. mean)
monthly_df = monthly_df.groupby('date')['number'].sum().reset_index()
monthly_df = monthly_df[monthly_df['date'] >= '2000-01-01']

monthly_df.to_csv(OUT_PATH,index=False)
