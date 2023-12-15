billet_10 = 0
billet_100 = 0
billet_50 = 0
billet_20 = 0

montant = int(input("Entrez le montant à retirer : "))

billet_100 = montant // 100
reste = montant % 100
billet_50 = reste // 50
reste = reste % 50
billet_10 = reste // 10
reste = reste % 10
piece_2 = reste // 2
reste = reste % 2
piece_1 = reste // 1

print("Billets de 100 :", billet_100)
print("Billets de 50 :", billet_50)
print("Billets de 10 :", billet_10)
print("pièces de 2 :", piece_2)
print("pièces de 1 :", piece_1)
