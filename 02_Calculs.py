# Les calculs simples s'écrivent comme sur papier en maths, par exemple :
addition = 2 + 3
soustraction = 5 - 2
multiplication = 4 * 3
division = 10 / 2
puissance = 2 ** 3

# Attention : Python n'affiche rien tout seul ! Pour voir un résultat, il faut utiliser print().
print("Addition :", addition)             # 5
print("Soustraction :", soustraction)     # 3
print("Multiplication :", multiplication) # 12
print("Division :", division)             # 5.0 (une division donne toujours un nombre à virgule)
print("Puissance :", puissance)           # 8

# On peut remplacer les nombres par des variables pour rendre le code plus lisible :
a = 2
b = 3
somme = a + b
print("a + b =", somme)

# Les parenthèses fonctionnent comme en maths :
sans_parentheses = 2 + 3 * 4   # 14, car 3 * 4 est calculé en premier
avec_parentheses = (2 + 3) * 4 # 20, car les parenthèses sont calculées en premier
print(sans_parentheses, avec_parentheses)

# Deux opérateurs très utiles en plus :
division_entiere = 10 // 3 # 3 : le résultat de la division, sans les décimales
modulo = 10 % 3            # 1 : le reste de la division (10 = 3 * 3 + 1)
print("10 // 3 =", division_entiere)
print("10 % 3 =", modulo)

# Plus compliqué : les racines et les logarithmes nécessitent la bibliothèque math :
import math # Import de la bibliothèque math pour utiliser les fonctions mathématiques avancées.

# Racine carrée
racine_carre = math.sqrt(16) # La fonction sqrt() calcule la racine carrée d'un nombre.
print("Racine de 16 :", racine_carre) # 4.0

# Puissance (autre méthode, équivalente à 2 ** 3, mais qui renvoie toujours un nombre à virgule)
puissance_math = math.pow(2, 3)
print("2 puissance 3 :", puissance_math) # 8.0

# Logarithme
logarithme = math.log(100, 10) # Le deuxième argument est la base du logarithme.
print("Log de 100 en base 10 :", logarithme) # 2.0
# Avec un seul argument, math.log(x) calcule le logarithme népérien (base e).

# Quelques constantes et arrondis utiles :
print("Pi :", math.pi)
print("Arrondi de 3.14159 à 2 décimales :", round(3.14159, 2)) # 3.14
