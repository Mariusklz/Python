nombre=float(input("Vous cherchez la table de multiplication de quel nombre ? : "))
multiplication = [nombre,nombre,nombre,nombre,nombre,nombre,nombre,nombre,nombre,nombre]
#multiplication = [ round(nombre * 0, 1), round(nombre * 1, 1), round(nombre * 2, 1), round(nombre * 3, 1), round(nombre * 4, 1), round(nombre * 5, 1), round(nombre * 6, 1), round(nombre * 7, 1), round(nombre * 8, 1), round(nombre * 9, 1)]
#print( nombre, "* 0 =",multiplication[0],"\n",nombre, "* 1 =",multiplication[1],"\n",nombre, "* 2 =",multiplication[2],"\n",nombre, "* 3 =",multiplication[3],"\n",nombre, "* 4 =",multiplication[4],"\n",nombre, "* 5 =",multiplication[5],"\n",nombre, "* 6 =",multiplication[6],"\n",nombre, "* 7 =",multiplication[7],"\n",nombre, "* 8 =",multiplication[8],"\n",nombre, "* 9 =",multiplication[9],"\n")
for i in range(0,10):
    x = round(nombre * i, 1)
    print(nombre, "*", i, "=", x)