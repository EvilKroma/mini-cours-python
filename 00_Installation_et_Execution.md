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

## 2. Installer l'extension Python (tu l'as déjà fait mais c'est à savoir)
1. Cliquer sur l'icône **Extensions** à gauche (les 4 carrés), ou faire `Cmd+Shift+X`.
2. Chercher **Python** (par Microsoft) et cliquer sur **Installer**.

## 3. Choisir le bon Python : celui de l'environnement virtuel
Python n'est pas installé sur tout l'ordinateur : il est dans un **environnement virtuel** (un "espace isolé" propre à ce projet, souvent un dossier nommé `venv` ou `.venv`). VS Code doit donc être réglé pour utiliser CE Python-là.

1. Ouvrir un fichier `.py`.
2. Faire `Cmd+Shift+P` : une barre s'ouvre en haut.
3. Taper **Python: Select Interpreter** et valider.
4. Dans la liste, choisir l'entrée qui mentionne l'environnement virtuel (par exemple `.venv` ou `venv`).
5. Si elle n'apparaît pas (ou si la liste est vide) : ce n'est pas grave. Choisir **Enter interpreter path...** (toujours présent dans la liste), puis **Find...**, et sélectionner à la main le fichier `python` situé dans le dossier de l'environnement, sous-dossier `bin` (par exemple `Python/.venv/bin/python`).
   - Un dossier dont le nom commence par un point (comme `.venv`) est masqué sur Mac. Dans la fenêtre de sélection, faire `Cmd+Shift+.` pour le faire apparaître.
   - Si la commande **Python: Select Interpreter** n'existe pas, c'est que l'extension Python n'est pas installée : voir l'étape 2.

Tant qu'un fichier `.py` est ouvert, le Python choisi s'affiche dans la barre du bas, à droite (par exemple `3.14.0 (.venv)`). Il doit mentionner le nom de l'environnement. Un clic dessus rouvre la liste pour en changer.

## 4. Activer l'environnement dans le terminal
Dans le terminal de VS Code (menu **Terminal > Nouveau terminal**), l'environnement s'active souvent tout seul quand l'étape 3 est faite. On le voit quand `(venv)` ou `(.venv)` apparaît au début de la ligne.

Sinon, l'activer à la main (en adaptant le chemin si l'environnement est ailleurs) :

```
source .venv/bin/activate
```

Une fois activé, la commande `python` utilise le bon Python. Pour le quitter : `deactivate`.

## 5. Exécuter un fichier
### Méthode 1 : la flèche
Ouvrir le fichier, puis cliquer sur la **flèche ▶ en haut à droite** de l'éditeur. Le résultat s'affiche dans le terminal en bas.

### Méthode 2 : le terminal
Ouvrir un terminal (**Terminal > Nouveau terminal**) et écrire :

```
python 01_Entrée_Sortie.py
```
(l'environnement doit être activé, voir l'étape 4)

Astuce : écrire les premières lettres du nom du fichier puis appuyer sur `Tab` complète le nom automatiquement.

## Bon à savoir
- Quand le programme attend une réponse (`input`), cliquer dans le terminal, taper la réponse, puis `Entrée`.
- Pour arrêter un programme qui tourne trop longtemps : `Ctrl+C` dans le terminal.
- En cas d'erreur, un message rouge apparaît. Lire la **dernière ligne** : elle indique le type d'erreur et souvent la cause. Une erreur n'est pas grave, tout le monde en fait, c'est comme ça qu'on apprend !
- Pour ce cours, modifier les fichiers, tester, casser, recommencer : il n'y a rien à perdre.
