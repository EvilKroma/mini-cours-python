# Pour écrire une réponse ou un texte en console, il faut utiliser la fonction print().
print("Bonjour!")

# On peut y ajouter des variables pour rendre le texte plus dynamique :
nom = "Marine"
print("Bonjour " + nom + "!") # On peut utiliser le signe + pour concaténer des chaînes de caractères. Concaténner veut dire les mettre bout à bout pour en faire une seule chaîne de caractères.
print(f"Bonjour {nom}!")      # On peut aussi utiliser les f-strings pour insérer des variables dans une chaîne de caractères.
print("Bonjour", nom)         # Ou séparer par des virgules : print ajoute un espace automatiquement.

# Pour demander une réponse à l'utilisateur, il faut utiliser la fonction input().
reponse = input("Comment ça va ? ")
print(f"Tu réponds : {reponse}")

# ATTENTION : input() renvoie TOUJOURS du texte (une chaîne de caractères), même si on tape un nombre.
# Pour faire des calculs, il faut convertir le texte en nombre :
age_texte = input("Quel âge as-tu ? ")
age = int(age_texte)       # int() convertit en nombre entier
print(f"L'année prochaine, tu auras {age + 1} ans.")

# On peut aussi écrire la conversion directement autour de input() :
taille = float(input("Quelle est ta taille en mètres (ex : 1.75) ? ")) # float() convertit en nombre à virgule
print(f"Ta taille est de {taille} m.")

# Que se passe-t-il si on tape "abc" à la place d'un nombre ? Python affiche une erreur (ValueError).