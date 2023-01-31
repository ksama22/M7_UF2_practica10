import pandas as pd
arxiu = "df_covid19_countries.csv"
# Llegir fitxer
df = pd.read_csv(arxiu)
#listAllPaises = pd.unique(df.location)
#print(listAllPaises)
print(df.groupby(by=["location"]).sum())
