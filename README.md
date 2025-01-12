# PROJET DE CONCEPTION DES SYSTÈMES ORIENTÉE OBJET ET SYSTÈMES TEMP REEL 
### Titre: Conception d'une application de gestion d'une usine de fabrication de crayons

---
### Auteurs

- [GOUMOU GONO](https://www.linkedin.com/in/gono-goumou-506a2b14b)
- [GAO JINGQI](https://www.linkedin.com/in/gono-goumou-506a2b14b)


**Encadrant** : [Guilhem Saurel](https://www.linkedin.com/in/nim65s/)
#### Formation: [Master EEA-ISTR](https://eea.univ-tlse3.fr/ingenierie-des-systemes-temps-reel)
#### Année universitaire : 2024-2025
---
## Description
Ce projet vise à simuler la gestion des usines de production de crayon en utilisant Django pour la partie serveur et C++ pour la partie client.

---

## Dépendances du Projet

Voici les dépendances nécessaires pour faire fonctionner ce projet :

- ![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
- ![pip](https://img.shields.io/badge/pip-Gestionnaire_de_paquets_Python-orange)
- ![Git](https://img.shields.io/badge/Git-Github-purple)
- ![Venv](https://img.shields.io/badge/Venv-Environnement_virtuel_Python-red)
- ![CMake](https://img.shields.io/badge/CMake-3.14%2B-yellow)
- ![C++ Compiler](https://img.shields.io/badge/C%2B%2B_Compiler-C%2B%2B17%2B-green)
---

## Guide détaillé pour l'installation et le lancement
### Téléchargement du projet 
#### Cloner le Dépôt
Clonez le dépôt Git sur votre machine locale :
```bash
git clone https://github.com/Zawelon/tp_coo.git
```

#### Se Placer dans le Dossier
Positionnez-vous dans le répertoire du projet :
```bash
cd tp_coo
```
---

### Configuration de l'Environnement Python

#### Créer un Environnement Virtuel
Créez un environnement virtuel pour isoler les dépendances :
```bash
python3 -m venv env
echo env >> .gitignore
```

#### Activez l'environnement virtuel selon votre système :
##### Linux/MacOS :
```bash
source env/bin/activate
```

##### Windows :
```bash
env\Scripts\activate
```

#### Installer les Dépendances Python
Mettez à jour pip et installez les bibliothèques nécessaires :
```bash
pip install -U pip
pip install django
```

#### Lancer le Serveur Django
##### Se Placer dans le Dossier crayon
Positionnez-vous dans le répertoire du projet :
```bash
cd crayon
```
##### Préparer la Base de Données
Générez et appliquez les migrations :
```bash
python manage.py makemigrations
python manage.py migrate
```

##### Créer un Super Utilisateur
Créez un utilisateur administrateur pour accéder au panneau d'administration Django :
```bash
python manage.py createsuperuser
```

##### Lancer le Serveur
Démarrez le serveur local :
```bash
python manage.py runserver
```

#### Accédez à l'interface administrateur
Accédez à l'interface administrateur à l'adresse suivante :  
[http://localhost:8000/admin/](http://localhost:8000/admin/)

---

### Configuration et Compilation C++

#### Installation des Bibliothèques C++
Le projet utilise les bibliothèques suivantes :
- `nlohmann/json` pour la gestion des données JSON
- `cpr` pour les requêtes HTTP
- `Eigen3` pour les calculs mathématiques

Ces bibliothèques sont gérées automatiquement par CMake via `FetchContent`.

#### Préparer la Compilation
Configurez le projet avec CMake dans un dossier `build` dédié :
```bash
cmake -B build -S .
```

#### Compiler le Projet
Compilez le programme :
```bash
cmake --build build
```

#### Exécuter le Programme
Lancez le programme compilé :
```bash
./build/low_level
```

---
## Fonctionnalités Principales

- **API Django** :
  - Modèles définis pour `Ville`, `Usine`, `Machine`, `Produit`, et bien plus.
  - Points de terminaison pour récupérer des données en JSON.
  
- **C++** :
  - Interaction avec l'API Django via des requêtes REST.
  - Classes C++ pour modéliser les entités et afficher leurs données.

---

## Dépendances Techniques

- **Python** : Django pour la gestion du backend.
- **C++** :
  - `nlohmann/json` pour manipuler les données JSON.
  - `cpr` pour effectuer des requêtes REST.
  - `Eigen3` pour les calculs mathématiques.

---

### Améliorations Futures

- Support pour des bases de données avancées comme PostgreSQL.
- Ajout de tests unitaires automatisés pour les deux parties.
- Optimisation des appels API et gestion des erreurs dans le fichier client C++.
