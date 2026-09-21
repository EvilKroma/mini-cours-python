# Une boucle permet de répéter des instructions sans les réécrire.

# --- La boucle for : on sait combien de fois on veut répéter ---
# range(5) génère les nombres 0, 1, 2, 3, 4 (on commence à 0 et on s'arrête AVANT 5).
for i in range(5):
    print("Tour numéro", i)

# range(début, fin, pas) : on peut choisir où commencer et de combien avancer.
for i in range(1, 6):      # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 11, 2):  # 0, 2, 4, 6, 8, 10
    print(i)

# Exemple utile : la table de multiplication de 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# On peut aussi parcourir un texte lettre par lettre :
for lettre in "Python":
    print(lettre) # Affiche P, puis y, puis t, puis h, puis o, puis n sur des lignes séparées.

# --- La boucle while : on répète TANT QU'une condition est vraie ---
compteur = 3
while compteur > 0:
    print("Décompte :", compteur)
    compteur = compteur - 1  # sans cette ligne, la boucle ne s'arrêterait jamais
print("Décollage !")

# ATTENTION : si la condition reste toujours vraie, le programme tourne à l'infini.
# (Pour l'arrêter dans le terminal : Ctrl + C)

# Exemple : redemander tant que la réponse n'est pas correcte
mot_de_passe = ""
while mot_de_passe != "python":
    mot_de_passe = input("Mot de passe : ")
print("Bienvenue !")

# --- break : sortir de la boucle immédiatement ---
while True:  # boucle "infinie" volontaire
    reponse = input("Tape 'stop' pour arrêter : ")
    if reponse == "stop":
        break
print("Fin de la boucle.")