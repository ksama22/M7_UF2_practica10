#from function import * importaria tot de aquest arxiu
import function as f

# arxiu = pd.read_csv('files/mobile.csv', usecols=("id", "clock_speed"))
arxiu = 'files/mobile.csv'

print("Exercici 1")
print(f.Ex1(arxiu))

print("Exercici 2")
print(f.Ex2(arxiu))

print("Exercici 3")
print(f.Ex3(arxiu))
