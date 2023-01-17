from function import *

#arxiu = pd.read_csv('files/testcopy.csv', usecols=("id", "clock_speed"))
arxiu = pd.read_csv('files/test.csv', usecols=("id", "clock_speed"))
print("Exercici 1")
Ex1(arxiu)
print("Exercici 2")
Ex2(arxiu)
print("Exercici 3")
Ex3(arxiu)