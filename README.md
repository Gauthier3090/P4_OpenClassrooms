# Projet 4: Développez un programme logiciel en Python

![Image of OpenClassrooms](https://onatestepourtoi.com/wp-content/uploads/2020/02/Logo_openclassrooms_onatestepourtoi.jpg)

## Résumé du projet

Un programme en python qui permet de créer différents tournois d'échecs. Ce programme se lance sur un terminal et posséde différents menus comme :

* Joueurs
    * Lister des joueurs
        * Lister les joueurs par ordre alphabétique
        * Lister les joueurs par classement
    * Ajouter des joueurs
    * Modifier le rang d'un joueur
* Tournois
    * Lister les tournois
        * Lister l'ensemble des tournois
        * Lister tous les tours d'un tournoi
        * Lister tous les matchs d'un tournoi
        * Lister les vainqueurs d'un tournoi
    * Créer un tournoi
    * Jouer un tournoi
* Quitter

Lors d'ajouts ou de modifications, les données sont mises à jour dans la base de données.

# Configurer un environnement virtuel Python

## Windows 10

La création d'environnements virtuels est faite en exécutant la commande [venv](https://docs.python.org/fr/3/library/venv.html) :

```bash
python -m venv \path\to\new\virtual\venv
```

Pour commencer à utiliser l’environnement virtuel, il doit être activé :

```bash
.\venv\Scripts\activate.bat
```

Utilisez le gestionnaire de packages [pip](https://pip.pypa.io/en/stable/) pour installer les paquets requis :

```bash
pip install -r requirements.txt
```

Pour lancer le programme :

```bash
py .\main.py
```


## Linux ou MacOs

La création d'environnements virtuels est faite en exécutant la commande [venv](https://docs.python.org/fr/3/library/venv.html) :

```bash
python3 -m venv \path\to\new\virtual\venv
```

Pour commencer à utiliser l’environnement virtuel, il doit être activé :

```bash
source venv/bin/activate
```

Utilisez le gestionnaire de packages [pip](https://pip.pypa.io/en/stable/) pour installer les paquets requis :

```bash
pip install -r requirements.txt
```

Pour lancer le programme :

```bash
python3 main.py
```

Pour générer un rapport HTML flake8 utilisez cette ligne de commande :

```bash
flake8 --format=html --htmldir=flake-report --max-line-length=120 --exclude=venv && open flake8-rapport/index.html
```
