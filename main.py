#from function import * importaria tot de aquest arxiu
import function as f

# arxiu = pd.read_csv('files/mobile.csv', usecols=("id", "clock_speed"))
arxiu = 'files/mobile.csv'

#Per separat
print("Exercici 1")
f.Ex1(arxiu).show()

print("Exercici 2")
f.Ex2(arxiu).show()

print("Exercici 3")
f.Ex3(arxiu).show()


#Crea una figura ambs el valors
l3 = [[3, 5, 2, 5, 1],[2, 5, 3, 2, 1]]
l4 = [2, 5, 3, 2, 1]
#Fica la primera grafica del exercici 1
f.createInOne(listTL=f.Ex1Copia(arxiu), listBR=l4)
