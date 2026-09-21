# Une condition permet au programme de prendre des décisions.
# Structure : if (si) / elif (sinon si) / else (sinon)

age = 17

if age >= 18:
    print("Tu es majeur.")
else:
    print("Tu es mineur.")

# ATTENTION : l'indentation (les 4 espaces au début de la ligne) est OBLIGATOIRE en Python en appuyant sur la touche Tab si elle ne se fait pas automatiquement.
# C'est elle qui indique quelles lignes appartiennent au "if". N'oublie pas non plus les deux-points ":".

# Les opérateurs de comparaison :
#   ==  égal à              !=  différent de
#   >   plus grand que      <   plus petit que
#   >=  plus grand ou égal  <=  plus petit ou égal

# Rappel : = affecte une valeur, == compare deux valeurs.

# Plusieurs cas avec elif (Python teste dans l'ordre et s'arrête au premier cas vrai) :
note = 14

if note >= 16:
    print("Très bien")
elif note >= 12:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")

# Combiner plusieurs conditions avec and (et), or (ou), not (non) :
age = 25
a_le_permis = True

if age >= 18 and a_le_permis:
    print("Tu peux conduire.")

jour = "samedi"
if jour == "samedi" or jour == "dimanche":
    print("C'est le week-end !")

if not a_le_permis:
    print("Tu dois passer le permis.")

# Exemple avec input() : est-ce que le nombre est pair ?
nombre = int(input("Donne un nombre entier : "))
if nombre % 2 == 0:  # rappel : % donne le reste de la division
    print("Ce nombre est pair.")
else:
    print("Ce nombre est impair.")