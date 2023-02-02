import pandas as pd
import matplotlib.pyplot as plt


arxiu = "df_covid19_countries.csv"
def Ex1(arxiu):
    # Cargar datos en un DataFrame de pandas
    df = pd.read_csv(arxiu)
    # Convertir la fecha en un tipo de fecha y extraer el mes
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    # Agrupar los datos por país y mes
    grouped = df.groupby(['location', 'month'])
    # Aplicar la función suma para obtener la cantidad total de casos por mes
    result = grouped['total_deaths'].sum()
    # Mostrar el resultado
    return result

print(Ex1(arxiu))


#plt.plot(("valores de x "),"(valores de y"),"....")
#plt.plot(("NOMBRE COLUMNA (NAME)"),("NOMBRE COLUMNA (AGE)"),("....")