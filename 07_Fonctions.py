# Une fonction est un bloc de code auquel on donne un nom, pour pouvoir le réutiliser.
# On a déjà vu: print(), input(), len(), int()... Ici, on crée les nôtres.

# Définition avec le mot-clé def (n'oublie pas les deux-points et l'indentation) :
def dire_bonjour():
    print("Bonjour !")

# Définir une fonction ne l'exécute pas. Il faut l'APPELER :
dire_bonjour()
dire_bonjour()  # on peut l'appeler autant de fois qu'on veut

# Une fonction peut recevoir des paramètres (des informations dont elle a besoin) :
def saluer(prenom):
    print(f"Bonjour {prenom} !")

saluer("Marine")
saluer("Paul")

# Une fonction peut aussi renvoyer un résultat avec return :
def carre(nombre):
    return nombre * nombre

resultat = carre(5)
print(resultat)       # 25
print(carre(3) + 1)   # 10 : on peut utiliser le résultat directement dans un calcul

# Plusieurs paramètres :
def aire_rectangle(longueur, largeur):
    return longueur * largeur

print(aire_rectangle(4, 3))  # 12

# Différence entre print et return :
#   - print affiche quelque chose à l'écran, mais la valeur est perdue.
#   - return renvoie la valeur à celui qui appelle la fonction, qui peut la réutiliser.

# Un paramètre peut avoir une valeur par défaut :
def puissance(nombre, exposant=2):
    return nombre ** exposant

print(puissance(5))     # 25 (exposant par défaut = 2)
print(puissance(2, 10)) # 1024

# Une fonction qui utilise une condition :
def est_pair(nombre):
    return nombre % 2 == 0

print(est_pair(4))  # True
print(est_pair(7))  # False

# Pourquoi utiliser des fonctions ?
#   - éviter de répéter le même code
#   - découper un gros programme en petites parties faciles à comprendre
#   - tester chaque partie séparément
