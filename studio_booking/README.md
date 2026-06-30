# Studio Booking Manager

## Description

Studio Booking Manager est une application Python en ligne de commande permettant de gérer les inscriptions à des cours collectifs.

L'application utilise :

* Python
* SQLAlchemy (ORM)
* SQLite
* Programmation Orientée Objet (POO)

## Fonctionnalités

* Créer un cours
* Afficher tous les cours
* Inscrire une personne à un cours
* Afficher les cours complets
* Quitter l'application

## Structure du projet

```text
studio_booking/
│
├── main.py
├── database.py
├── models.py
├── crud.py
├── menu.py
├── seed.py
├── requirements.txt
├── README.md
└── studio.db
```

## Prérequis

* Python 3.10 ou supérieur

## Installation

### 1. Cloner le dépôt

```bash
git clone <URL_DU_DEPOT>
cd studio_booking
```

### 2. Créer un environnement virtuel

Windows

```bash
python -m venv venv
```

Linux / macOS

```bash
python3 -m venv venv
```

### 3. Activer l'environnement virtuel

Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

Linux / macOS

```bash
source venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

## Lancer l'application

```bash
python main.py
```

## Menu

```
=== Studio Booking Manager ===

1. Créer un cours
2. Afficher les cours
3. Inscrire une personne à un cours
4. Afficher les cours complets
5. Quitter
```

## Technologies utilisées

* Python
* SQLAlchemy
* SQLite

## Auteur

Projet réalisé dans le cadre de l'évaluation du module Python.
