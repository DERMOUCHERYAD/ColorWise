# ColorWise

## Introduction
ColorWise est une application qui permet d'explorer les graphes et de découvrir les algorithmes de coloriage. Elle utilise une interface graphique pour afficher les résultats et les informations pertinentes.

## Lancement du Projet directement avec le Script PowerShell
Un script PowerShell setup_and_run.ps1 est fourni pour vous faciliter la configuration et l'exécution de l'application. Ce script vérifie automatiquement les prérequis, installe les dépendances nécessaires, et lance l'application.
## Utilisation du Script
1.  Ouvrir PowerShell Assurez-vous d'ouvrir PowerShell dans le répertoire racine du    projet.
2.  Autoriser l'exécution des scripts Si vous n'avez pas déjà autorisé l'exécution des scripts, utilisez la commande suivante :
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
3.  Exécuter le script Lancez le script avec la commande suivante :
    .\setup_and_run.ps1
## Remarque 
Un fichier nommé `exemples.txt` dans le package contient des exemples de matrices, étiquetages, sommets et autres données de test que vous pouvez utiliser pour explorer les fonctionnalités de l'application.

### Sinon:

## Prérequis
- Python 3.8 ou supérieur installé sur votre machine.

## Installation
Pour installer et exécuter ce projet, suivez les étapes ci-dessous :

1. Clonez le dépôt : ou  Décompresser le fichier Zip 
    ```bash
    git clone https://github.com/DERMOUCHERYAD/ColorWise.git
    cd votre-repo
    ```

2. Créez et activez un environnement virtuel :
    ```bash
    python -m venv env
    cd env/Scripts
    activate
    cd ../..
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation
Pour lancer l'application, exécutez le fichier principal :
```bash
python main.py
```
## Remarque 
Un fichier nommé `exemples.txt` dans le package contient des exemples de matrices, étiquetages, sommets et autres données de test que vous pouvez utiliser pour explorer les fonctionnalités de l'application.

## Empaquetage en exécutable (facultatif)
Pour générer un fichier exécutable unique, utilisez PyInstaller :

```bash
pyinstaller --onefile main.py
```
Le fichier exécutable sera dans le dossier `dist`. (Attention il faut inclure les images de l'applications)

## Fonctionnalités
-Affichage des graphes
-Coloration des graphes
-Calcul de la couleur minimale possible
-Interface utilisateur intuitive

## Structure du projet
1.  main.py : Point d'entrée de l'application.
2.  model.py : Contient la logique métier et les algorithmes de coloriage.
3.  view.py : Gère l'affichage de l'interface utilisateur.
4.  controller.py : Interagit avec le modèle et la vue pour         orchestrer les actions de l'utilisateur.

## Documentation 
      docs/DETAILS.md (pour une documentation générale)
      build/(pour une documentation détaillée )  

## Contributeurs
DERMOUCHE Mohammed Ryad
