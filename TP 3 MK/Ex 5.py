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