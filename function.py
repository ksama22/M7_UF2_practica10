import pandas as pd
import matplotlib.pyplot as plt

def creaImagenDirectaDelCSV():
    df = pd.read_csv("files/test.csv")
    df.plot()
    plt.savefig("images/image.jpg")

def llegirTot():
    #Llegir fitxer
    df = pd.read_csv('files/test.csv')
    print(df.to_string())


def llegitNomColumnes():
    df = pd.read_csv('files/test.csv')
    print(df.columns)



def Ex1():
    #Llegir fitxer
    df = pd.read_csv('files/test.csv', usecols=("id","clock_speed"))
    print(df)

    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    # Plot the data using bar() method
    plt.bar(X, Y, color='red')
    plt.title("Exercici 1")
    plt.xlabel("ID Mobile")
    plt.ylabel("Clock Speed")
    # Show the plot
    plt.show()

def Ex2():
    # Llegir fitxer
    df = pd.read_csv('files/test.csv', usecols=("id", "battery_power"))
    print(df)

    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    # Plot the data using bar() method
    plt.bar(X, Y, color='green')
    plt.title("Exercici 2")
    plt.xlabel("ID Mobile")
    plt.ylabel("battery_power")
    # Show the plot
    plt.show()

def Ex3():
    # Llegir fitxer
    df = pd.read_csv('files/test.csv', usecols=("id", "px_height"))
    print(df)

    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    # Plot the data using bar() method
    plt.bar(X, Y, color='blue')
    plt.title("Exercici 3")
    plt.xlabel("ID Mobile")
    plt.ylabel("px_height")
    plt.savefig("images/exercici3.jpg")

    # Show the plot
    plt.show()
