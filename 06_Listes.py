# Une liste permet de ranger plusieurs valeurs dans une seule variable.
fruits = ["pomme", "banane", "cerise"]
notes = [12, 15, 9, 18]

print(fruits)
print(len(fruits))  # 3 : le nombre d'éléments

# On accède à un élément grâce à son indice (sa position). (on compte à partir de 0)
print(fruits[0])   # pomme
print(fruits[1])   # banane
print(fruits[-1])  # cerise (-1 = le dernier élément)

# Modifier un élément :
fruits[1] = "kiwi"
print(fruits)      # ['pomme', 'kiwi', 'cerise']

# Ajouter et retirer des éléments :
fruits.append("fraise")  # ajoute à la fin
fruits.remove("pomme")   # retire l'élément indiqué
print(fruits)

# Tester si un élément est dans la liste :
if "kiwi" in fruits:
    print("Il y a des kiwis !")

# Parcourir une liste avec une boucle for :
for fruit in fruits:
    print("J'aime les", fruit)

# Quelques fonctions pratiques sur les listes de nombres :
print(sum(notes))                # 54 : la somme
print(max(notes), min(notes))    # 18 9
print(sum(notes) / len(notes))   # 13.5 : la moyenne
print(sorted(notes))             # [9, 12, 15, 18] : liste triée

# --- Les dictionnaires ---
# Un dictionnaire associe une CLÉ à une VALEUR (comme un vrai dictionnaire ou un carnet d'adresses).
eleve = {"nom": "Marine", "age": 43, "classe": "CP"}
print(eleve["nom"])       # Marine
eleve["age"] = 18         # modifier une valeur
eleve["ville"] = "Lyon"   # ajouter une nouvelle clé
for cle, valeur in eleve.items():
    print(f"{cle} : {valeur}")