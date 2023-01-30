# from function import * importaria tot de aquest arxiu
import function as f

# arxiu = pd.read_csv('files/mobile.csv', usecols=("id", "clock_speed"))
arxiu = 'files/mobile.csv'

# Per separat
print("Exercici 1")
f.Ex1(arxiu).show()

print("Exercici 2")
f.Ex2(arxiu).show()

print("Exercici 3")
f.Ex3(arxiu).show()

# Fica la primera grafica del exercici 1
f.createInOneFigure(listTL=f.Ex1Dades(arxiu), listTR=f.Ex2Dades(arxiu), listBL=f.Ex3Dades(arxiu))
