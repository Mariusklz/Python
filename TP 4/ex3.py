nMax = 4
V1 = []
V2 = []
produit = 0
n = int(input("La taille des vecteurs :"))
if n < 1 or n > nMax:
    while n < 1 or n > nMax:
        n = int(input("La taille des vecteurs :"))
print("Saisie du premier vecteur :")
for i in range (0,n):
    V1.append(int(input("V1 [{}] :".format(i))))

print("Saisie du second vecteur :")
for i in range(0, n):
    V2.append(int(input("V2 [{}] :".format(i))))
    produit += V1[i] * V2[i]

print("Le Produit scalaire de V1 et V2 vaut :",produit)