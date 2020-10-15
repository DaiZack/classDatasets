import pandas as pd

df = pd.read_csv('WHO-COVID-19-global-data.csv')

df.columns = [d.strip() for d in df.columns]

dfgroups = df.groupby('Country_code')

for n, g in dfgroups:
    if not n.strip():
        n = 'XX'
    g.drop('Country_code', axis=1).to_excel('regional\\'+n+'.xlsx', index=0)
