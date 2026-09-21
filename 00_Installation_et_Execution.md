# Bien démarrer : VS Code et Python

À lire avant les autres fichiers. Aucune inquiétude si tout est nouveau : on avance pas à pas.

## Les 3 mots à connaître
- **Python** : le langage de programmation. Il doit être installé sur l'ordinateur pour pouvoir lire et exécuter le code.
- **VS Code** : l'éditeur où l'on lit et écrit le code (un "Word" pour le code).
- **Terminal** : une fenêtre où l'on donne des ordres à l'ordinateur en écrivant du texte. Dans VS Code, il est intégré.

## 1. Ouvrir le dossier dans VS Code
1. Ouvrir VS Code.
2. Menu **Fichier > Ouvrir un dossier...** puis choisir le dossier du cours (celui qui contient les fichiers `01_...py`, `02_...py`, etc.).
3. Les fichiers apparaissent à gauche. Un clic sur un fichier l'ouvre.

## 2. Installer l'extension Python
1. Cliquer sur l'icône **Extensions** à gauche (les 4 carrés), ou faire `Ctrl+Shift+X` (`Cmd+Shift+X` sur Mac).
2. Chercher **Python** (par Microsoft) et cliquer sur **Installer**.

## 3. Choisir le bon Python
VS Code doit savoir quel Python utiliser.
1. Ouvrir un fichier `.py`.
2. Faire `Ctrl+Shift+P` (`Cmd+Shift+P` sur Mac) : une barre s'ouvre en haut.
3. Taper **Python: Select Interpreter** et valider.
4. Choisir la version de Python la plus récente dans la liste (souvent marquée "Recommended").

Le Python choisi s'affiche en bas à droite de la fenêtre.

## 4. (Optionnel) Activer un environnement virtuel
Un environnement virtuel est un "espace isolé" pour un projet : il évite que les projets se mélangent. Pour ce cours, ce n'est pas obligatoire, mais c'est une bonne habitude.

Dans le terminal de VS Code (menu **Terminal > Nouveau terminal**) :

```
python3 -m venv .venv
```
(sur Windows : `python -m venv .venv`)

Puis l'activer :
- Mac / Linux : `source .venv/bin/activate`
- Windows : `.venv\Scripts\activate`

Quand c'est activé, `(.venv)` apparaît au début de la ligne du terminal. Si VS Code propose d'utiliser ce nouvel environnement, accepter. Sinon, refaire l'étape 3 et choisir celui qui contient `.venv`.

## 5. Exécuter un fichier
### Méthode 1 : la flèche
Ouvrir le fichier, puis cliquer sur la **flèche ▶ en haut à droite** de l'éditeur. Le résultat s'affiche dans le terminal en bas.

### Méthode 2 : le terminal
Ouvrir un terminal (**Terminal > Nouveau terminal**) et écrire :

```
python 01_Entrée_Sortie.py
```
(sur Mac, si ça ne marche pas : `python3 01_Entrée_Sortie.py`)

Astuce : écrire les premières lettres du nom du fichier puis appuyer sur `Tab` complète le nom automatiquement.

## Bon à savoir
- Quand le programme attend une réponse (`input`), cliquer dans le terminal, taper la réponse, puis `Entrée`.
- Pour arrêter un programme qui tourne trop longtemps : `Ctrl+C` dans le terminal.
- En cas d'erreur, un message rouge apparaît. Lire la **dernière ligne** : elle indique le type d'erreur et souvent la cause. Une erreur n'est pas grave, tout le monde en fait, c'est comme ça qu'on apprend !
- Pour ce cours, modifier les fichiers, tester, casser, recommencer : il n'y a rien à perdre.
