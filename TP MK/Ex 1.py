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