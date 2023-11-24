#Exercice 1 : Choix de la structure itérative
#A


somme=0
p=int(input("Entrez un entier p:"))
for i in range(p+1):
    somme=somme+i
    print(somme)
print(("La somme des"),p,("premier entiers naturels est égale à"),somme)


#Exercice 1 : Choix de la structure itérative
#B


somme=0
p=int(input("Entrez un entier p:"))
while p != 100:
    p = int(input("Donnez un autre entier p:"))
print(("La somme des"),p,("premier entiers naturels est égale à"),somme)


##Exercice 1 : Choix de la structure itérative
##C


infDIx = 0                                      ##Le nombre de valeurs inférieur strictement à 10
entrelestrcu = 0                                ##Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15
supQuinze = 0                                   ##Le nombre de valeurs supérieur strictement à 15
for i in range(10):
        p=float(input("Entrez un nombre compris entre 0 et 20 p:"))
        liste = []
        while p > 20 or p < 0:
            print("Recommencer")
        liste.append(p)
        if p >= 10 and p < 15:
            entrelestrcu += 1

        elif p < 10:
            infDIx += 1

        elif p >= 15:
            supQuinze += 1
print("Le nombre de valeurs inférieur strictement à 10 est de :" , infDIx)
print("Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est de :" , entrelestrcu)
print("Le nombre de valeurs supérieur strictement à 15 est de :" , supQuinze)


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


## Exercice 3 : Jeu du Nombre mystère


import random
def nombres():
    mysteres = random.randint(0, 100)
    tentatives = 0
    find = False

    print("Devinez le nombre mystère entre 0 et 100.")

    while not find:
        guess = int(input("Entrez votre estimation : "))
        tentatives += 1

        if guess < mysteres:
            print("Le nombre mystère est plus grand.")
        elif guess > mysteres:
            print("Le nombre mystère est plus petit.")
        else:
            find = True
            print(f"Bravo ! Vous avez deviné le nombre mystère en {tentatives} tentatives.")


nombres()


## Exercice 4 : Factorielle itérative


def factorielle_while(n):
    result = 1
    print("Calcul de la factorielle avec une boucle while :")
    print(f"Factorielle de {n}! = 1")
    while n > 1:
        result *= n
        n -= 1
        print(f"Factorielle de {n}! = {result}")
    return result

def factorielle_for(n):
    result = 1
    print("\nCalcul de la factorielle avec une boucle for :")
    for i in range(1, n + 1):
        result *= i
        print(f"Factorielle de {i}! = {result}")
        return result

nbr = int(input("Entrez un entier pour calculer sa factorielle : "))
choix_de_boucle = input("Choisissez la boucle à utiliser ('while' ou 'for') : ")

if choix_de_boucle == 'while':
    result = factorielle_while(nbr)
elif choix_de_boucle == 'for':
    result = factorielle_for(nbr)
else:
    print("Choix de boucle invalide. Veuillez choisir 'while' ou 'for'.")

    print(f"\nLa factorielle de {nbr} est : {result}")


## Exercice 5 : Location de vélos


print("Bienvenu a la location de vélo")
hd = int(input("Donnez l'heure de début de la location (un entier) : "))
hf = int(input("Donnez l'heure de fin de la location (un entier) : "))

while hd not in range(0, 25) or hf not in range(0, 25):
    print("Les heures doivent être comprises entre 0 et 24 !")
    hd = int(input("Donnez l'heure de début de la location (un entier) : "))
    hf = int(input("Donnez l'heure de fin de la location (un entier) : "))

while hf < hd:
    print("Attention ! le début de la location est après la fin ...")
    hd = int(input("Donnez l'heure de début de la location (un entier) : "))
    hf = int(input("Donnez l'heure de fin de la location (un entier) : "))

while hf == hd:
    print("Attention ! l’heure de fin est identique à l’heure de début.")
    hd = int(input("Donnez l'heure de début de la location (un entier) : "))
    hf = int(input("Donnez l'heure de fin de la location (un entier) : "))

a = hd
nbrloc1 = 0
tarif1 = 0
nbrloc2 = 0
tarif2 = 0

while a != hf:
    if 0 <= a < 7 or 17 <= a <= 24:
        nbrloc1 += 1
        tarif1 += 1
    if 7 <= a < 17:
        nbrloc2 += 1
        tarif2 += 1
    a += 1

total = nbrloc1 * 1 + nbrloc2 * 2

print("Vous avez loué votre vélo pendant \n", nbrloc1, "heure(s) au tarif horaire de 1.0 euro \n", nbrloc2,"heure(s) au tarif horaire de 2.0 euro(s) \n Le montant total à payer est de", total, "euro(s).")
