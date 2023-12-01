##Exercie 2 : Compte à rebours
## Avec WHILE


import time
def rebour(p):
    while p >= 0:
        print(p)
        time.sleep(1)
        p -= 1
p = int(input("Entrez un nombre entier positif : "))
if p < 0:
    print("Veuillez entrer un nombre entier positif.")
else:
    rebour(p)


##Exercie 2 : Compte à rebours
## Avec FOR


import time
N = int(input("Entrez la valeur de N : "))
for i in range (N, 0, -1):
    print(i)
    time.sleep(1)