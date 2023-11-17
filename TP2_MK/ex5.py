nombre=int(input("Entrez un nombre entier: "))


if nombre>0:
    if nombre % 2 == 0:
        print("nombre possif et pair")
    else:
        print("Le nombre est possitif et impaire")

elif nombre<0:
    if nombre % 2 == 0:
        print("nombre possif et pair")
    else:
        print("Le nombre est possitif et impaire")

else:
    print("le nombre est 0 (et il est pair)")