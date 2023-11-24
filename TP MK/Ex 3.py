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