a=input("Entrez la première valeur : ")
b=input("Entrez la deuxième valeur : ")
c=input("Entrez la troisième valeur : ")

print("Les valeurs choisies sont : a = " + a + ", b = " + b + ", c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")
z = 0


z = a
a = c
c = b
b = z

print("Les valeurs permutées sont : a :" + a + ", b :" + b + ", c :" + c)
