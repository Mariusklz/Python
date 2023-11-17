base = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives=int(input("Combien de personnes seront conviées:"))

fromage = fromage * nbConvives / base
eau = eau * nbConvives / base
ail = ail * nbConvives / base
pain = pain * nbConvives / base

print("Pour faire une fondue fribourgeoise pour" , nbConvives ,  "personnes, il vous faut :\n-",fromage , "gr de fromage \n-" , eau , "dl d'eau \n-" , ail , "gousse(s) d'ail \n-" , pain , "gr de pain")