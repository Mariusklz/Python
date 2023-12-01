nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
note = []
Etudiants =[]
somme = 0
for i in range(0, nombreEtudiants):
    note.append(float(input("note de l'étudiant {} : ".format(i))))
    if note[i] < 0 or note[i] > 20:
        while note[i] < 0 or note[i] > 20:
            note[i] = (float(input("note de l'étudiant {} : ".format(i))))
    somme += note[i]

moyenne = somme / nombreEtudiants
print("La moyenne de classe est de :", moyenne)
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(0, nombreEtudiants):
    print(i,"|",note[i],"|",note[i] - moyenne)