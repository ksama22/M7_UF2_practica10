import pandas as pd
import matplotlib.pyplot as plt

def Ex1():
    # Importa el archivo
    arxiu = '../files/cities_population.csv'
    # Lee el csv
    df = pd.read_csv(arxiu, usecols=["City", "Population"]).replace({",":""},regex=True)

    df = df.dropna()
    df = df.head(10)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    plt.pie(Y, labels=X, autopct='%1.1f%%')
    plt.title("per ciutat, el total de població")
    #plt.legend(loc='lower left')
    plt.legend(bbox_to_anchor=(-0.03, 1))

    plt.show()
    print(df)
