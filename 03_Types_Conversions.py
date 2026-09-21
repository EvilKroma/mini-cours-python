# Une variable est une "boîte" qui porte un nom et contient une valeur.
# Chaque valeur a un TYPE, qui détermine ce qu'on peut faire avec.

entier = 42          # int   : nombre entier
decimal = 3.14       # float : nombre à virgule (avec un point, pas une virgule !)
texte = "Bonjour"    # str   : string pour chaîne de caractères (entre guillemets)
booleen = True       # bool  : vrai (True) ou faux (False), avec une majuscule

# type() permet de connaître le type d'une valeur :
print(type(entier))   # <class 'int'>
print(type(decimal))  # <class 'float'>
print(type(texte))    # <class 'str'>
print(type(booleen))  # <class 'bool'>

# Les types se comportent différemment :
print(2 + 3)      # 5      : addition de nombres
print("2" + "3")  # "23"   : concaténation de textes (on colle les textes)
print("ha" * 3)   # "hahaha" : répéter un texte

# On ne peut pas mélanger n'importe quoi :
# print("Age : " + 20)  # <- Erreur (TypeError) : on ne peut pas additionner un texte et un nombre.
print("Age : " + str(20))  # OK : str() convertit le nombre en texte
print(f"Age : {20}")       # OK aussi, et souvent plus simple : les f-strings convertissent automatiquement

# Les fonctions de conversion :
print(int("12") + 1)     # 13   : texte -> entier
print(float("3.5") * 2)  # 7.0  : texte -> décimal
print(int(3.9))          # 3    : décimal -> entier (la partie décimale est supprimée, pas arrondie !)
print(str(100) + " euros")

# Un booléen est le résultat d'une comparaison :
print(5 > 3)   # True
print(5 == 3)  # False (attention : == compare, alors que = affecte une valeur à une variable)

# Un peu de vocabulaire sur les textes :
prenom = "Marine"
print(len(prenom))      # 6       : nombre de caractères
print(prenom.upper())   # MARINE  : tout en majuscules
print(prenom.lower())   # marine  : tout en minuscules
print(prenom[0])        # M       : le premier caractère (on compte à partir de 0 et pas 1)