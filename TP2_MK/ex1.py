x=input("Entrez x : ")
y=input("Entrez y : ")

print("Les valeurs choisies sont : x = " + x + ", y = " + y)
print("Avant permutation : x = " + x + ", y = " + y)
z = 0

z = x
x = y
y = z

print("Valeurs après 1 ère Permutation: "
      "\nx : " + x +
      "\ny : " + y )


y = x
x = z

print("Valeurs après 2 ème Permutation: "
      "\nx : " + x +
      "\ny : " + y )

z = x
x = y
y = z

print("Valeurs après 3 ème Permutation: "
      "\nx : " + x +
      "\ny : " + y )

y = x
x = z

print("Valeurs après 4 ème Permutation: "
      "\nx : " + x +
      "\ny : " + y )