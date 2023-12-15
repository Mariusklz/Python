note = []
coef = []
moyenne = 0
print("Veuillez entrez la note du module et le coefficient")
for i in range(5):
  tpm = input().split()
  note.append(float(tpm[0]))
  coef.append(float(tpm[1]))

for i in range(5):
  moyenne += note[i] * coef[i]
print("La moyenne est de ", moyenne / sum(coef))

if moyenne > 10 and not note[i] < 8:
  print("L'étudiant est admis")
else:
  print("L'étudiant est refusé")
