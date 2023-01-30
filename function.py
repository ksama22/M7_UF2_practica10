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
    # Separo la cerca de dades de la cerca d'arxius
    mlist = Ex1Dades(nfile)
    X = mlist[0]
    Y = mlist[1]
    # Plot the data using bar() method
    plt.bar(X, Y, color='red')
    plt.title("Exercici 1")
    plt.xlabel("ID Mobile")
    plt.ylabel("Clock Speed")
    # Show the plot
    # plt.show()
    return plt


def Ex1Dades(nfile):
    # Llegir fitxer
    excludeList = generaList()
    arxiu = pd.read_csv(nfile, usecols=("id", "clock_speed"))
    # arxiu = arxiu[arxiu["id"] <= 120]
    arxiu = arxiu.loc[[3, 13, 34, 56, 70, 85, 110, 120, 210, 400]]
    # arxiu = arxiu[arxiu["id"]==10]
    X = list(arxiu.iloc[:, 0])
    print("mi lista x", X)
    Y = list(arxiu.iloc[:, 1])
    print("mi lismta Y", Y)
    mlist = []
    mlist.append(Y)
    mlist.append(Y)
    return mlist


def Ex2(nfile):
    mList = Ex2Dades(nfile)
    X = mList[0]
    Y = mList[1]
    # Plot the data using bar() method
    plt.bar(X, Y, color='green')
    plt.title("Exercici 2")
    plt.xlabel("ID Mobile")
    plt.ylabel("battery_power")
    # Show the plot
    # plt.show()
    return plt


def Ex2Dades(arxiu):
    # Llegir fitxer
    df = pd.read_csv(arxiu, usecols=("id", "battery_power"))
    df = df[df["id"] <= 10]
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])
    mlist = []
    mlist.append(X)
    mlist.append(Y)
    return mlist


def Ex3(nfile):
    mlist = Ex3Dades(nfile)
    X = mlist[0]
    Y = mlist[1]
    # Plot the data using bar() method
    plt.bar(X, Y, color='blue')  # ,width=0.2
    plt.title("Exercici 3")
    plt.xlabel("ID Mobile")
    plt.ylabel("px_height")
    # plt.savefig("images/exercici3.jpg")
    # Show the plot
    # plt.show()
    return plt
def Ex3Dades(nfile):
    # Llegir fitxer
    df = pd.read_csv(nfile, usecols=("id", "px_height"))
    df = df[df["id"] <= 10]
    print(df)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])
    mlist = []
    mlist.append(X)
    mlist.append(Y)
    return mlist

def createInOneFigure(listTL=[], listTR=[], listBL=[], listBR=[]):
    # Para crear figuras 'figure()' y 'num' es el nombre
    windows = plt.figure(num="Grafica 1")
    # Nomes crea el grafic si el valor no es el per defecte
    if len(listTL) != 0:
        fig1 = windows.add_subplot(2, 2, 1)  # top-left
        fig1.set_title("Grafica 1 (Top-Left)")
        fig1.hist(listTL)
    # Nomes crea el grafic si el valor no es el per defecte
    if len(listTR) != 0:
        fig2 = windows.add_subplot(2, 2, 2)  # top-right
        fig2.set_title("Grafica 2 (Top-Right)")
        fig2.hist(listTR)
    # Nomes crea el grafic si el valor no es el per defecte
    if len(listBL) != 0:
        fig3 = windows.add_subplot(2, 2, 3)  # bottom-left
        fig3.set_title("Grafica 3 (Botom-Left)")
        fig3.hist(listBL)
    # Nomes crea el grafic si el valor no es el per defecte
    if len(listBR) != 0:
        fig4 = windows.add_subplot(2, 2, 4)  # bottom-right
        fig3.set_title("Grafica 3 (Botom-Right)")
        fig4.hist(listBR)
    # Mostra els grafics disponibles
    plt.show()
