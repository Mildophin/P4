# Projet 4 du parcours python d'OC : Tournoi d'échecs
Ce programme est un gestionnaire de tournois d'échecs dans le cadre d'un projet d'OC
## Installation:
Premièrement, installer Python 3.9 ou plus récent (https://www.python.org/downloads/).
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/Mildophin/P4.git
```
Placez vous dans le dossier P4, puis créez un nouvel environnement virtuel:
```
python -m venv venv
```
Ensuite, activez-le.
Windows:
```
venv\scripts\activate.bat
```
Linux:
```
source venv/bin/activate
```
Il ne reste plus qu'à installer les packages requis:
```
pip install -r requirements.txt
```
Vous vous pourrez lancer le script:
```
python main.py
```

## Utilisation & Mode d'emploi
Le menu principal est divisé en 4 options différentes.
### 1) Créer un tournoi
- Le programme vous permet de gérer des tournois d'échecs. Lors de la première utilisation, sélectionnez "Créer un tournoi", puis laissez vous guider.
- Si aucun joueurs n'est présent dans la base de donnée, vous serez invité à en créer.
- Lors d'un tournoi, vous serez invité à rentrer les résultats après chaque match. A la fin d'un tournoi, un classement sera généré.
- Pendant le tournoi, vous aurez la possibilité de sauvegarder le tournoi en cours, en charger un nouveau, de voir ou modifier les classements.
### 2) Charger un tournoi
- Cette section vous permet de charger un tournoi depuis la base de donnée.
- Une fois le tournoi chargé, vous serez invité à le continuer.
### 3) Créer des joueurs
- Lorsque vous sélectionnez cette option, vous êtes invité à rentrer le nombre de joueurs à créer.
- Laissez vous ensuite guider par le programme.
### 4) Les rapports
- Cette section vous permet de générer différents rapport.
- Vous pouvez consulter: le classement global des joueurs par classement et ordre alphabétique.
- Les détails des tournois passés: classement des joueurs du tournoi, tours et matchs de chaque tournois.
## Générer le rapport Flake8
- Installez flake8 avec la commande: 
```
pip install flake8-html
```
- S'il n'existe pas, créer un fichier setup.cfg dans le dossier mère du projet
- Ecrire le texte suivant dedans:
```
[flake8]
exclude = .git, env (dossier de l'environnement virtuel), __pycache__, .gitignore
max-line-length = 119
```
- Tapez la commande:
```
flake8 --format=html --htmldir=flake-report
```
- Le rapport sera généré dans le dossier flake8 dans le dossier P4.
