import pandas as pd
import matplotlib.pyplot as plt


def creaImagenDirectaDelCSV(file):
    # Obre el fitxer csv i general una imatge grafica de tot l'arxiu
    df = pd.read_csv(file)
    df.plot()
    plt.savefig("images/image.jpg")


def llegirTot(file):
    # Llegir fitxer
    df = pd.read_csv(file)
    # Retorna tot l'arxiu saltarse columnes
    print(df.to_string())


def llegitNomColumnes(file):
    # LLEGEIX E
    df = pd.read_csv(file)
    print(df.columns)


def generaList():
    aList = [];
    for x in range(1, 1000):
        if (x == 3) or (x == 13) or (x == 34) or (x == 56) or (x == 70) or (x == 85) or (x == 110) or (x == 120) or (
                x == 210) or (x == 400) or (x == 650):
            a = "b"
        else:
            aList.append(x)
    return aList


def Ex1(nfile):
    # Llegir fitxer
    excludeList = generaList()
    arxiu = pd.read_csv(nfile, usecols=("id", "clock_speed"), skiprows=excludeList)
    arxiu = arxiu[arxiu["id"] <= 120]

    # arxiu = arxiu[arxiu["id"]==10]
    X = list(arxiu.iloc[:, 0])
    Y = list(arxiu.iloc[:, 1])
    # Plot the data using bar() method
    plt.bar(X, Y, color='red')
    plt.title("Exercici 1")
    plt.xlabel("ID Mobile")
    plt.ylabel("Clock Speed")
    # Show the plot
    plt.show()
    return arxiu


def Ex2(nfile):
    # Llegir fitxer
    df = pd.read_csv(nfile, usecols=("id", "battery_power"))
    df = df[df["id"] <= 10]
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    # Plot the data using bar() method
    plt.bar(X, Y, color='green')
    plt.title("Exercici 2")
    plt.xlabel("ID Mobile")
    plt.ylabel("battery_power")
    # Show the plot
    plt.show()
    return df


def Ex3(nfile):
    # Llegir fitxer
    df = pd.read_csv(nfile, usecols=("id", "px_height"))
    df = df[df["id"] <= 10]
    print(df)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    # Plot the data using bar() method
    plt.bar(X, Y, color='blue')  # ,width=0.2
    plt.title("Exercici 3")
    plt.xlabel("ID Mobile")
    plt.ylabel("px_height")
    # plt.savefig("images/exercici3.jpg")
    # Show the plot
    plt.show()
    return df
