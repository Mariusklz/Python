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