# Projet de Fabrication de Crayons

_Auteur 1_ : GOUMOU GONO  
_Auteur 2_ : GAO JINGQI  
_Date_ : 08/1/2024

Ce projet vise à simuler la gestion d'une chaîne de production pour des usines en utilisant Django pour la partie serveur et C++ pour la partie client.

---

## 1. Installation et Démarrage

### 1.0 - Prérequis
Avant de commencer, assurez-vous que les éléments suivants sont installés :
- **Python 3.10 ou plus récent**
- **pip** (gestionnaire de paquets Python)
- **Git**
- **Venv** (environnement virtuel Python)
- **CMake** (version 3.14 ou plus récente)
- **Compilateur C++** compatible avec C++17

### 1.1 - Cloner le Dépôt
Clonez le dépôt Git sur votre machine locale :
```bash
git clone https://github.com/Zawelon/tp_coo.git

### 1.2 - Se Placer dans le Dossier
Positionnez-vous dans le répertoire du projet :
```bash
cd tp_coo

## 2. Configuration de l'Environnement Python

### 2.1 - Créer un Environnement Virtuel
Créez un environnement virtuel pour isoler les dépendances :
```bash
python3 -m venv env
echo env >> .gitignore

### Activez l'environnement virtuel selon votre système :
#### Linux/MacOS :
```bash
source env/bin/activate

#### Windows :
```bash
env\Scripts\activate

### 2.2 - Installer les Dépendances Python
Mettez à jour pip et installez les bibliothèques nécessaires :
```bash
pip install -U pip
pip install django

### 3. Lancer le Serveur Django

#### 3.1 - Préparer la Base de Données
Générez et appliquez les migrations :
```bash
python manage.py makemigrations
python manage.py migrate

#### 3.2 - Créer un Super Utilisateur
Créez un utilisateur administrateur pour accéder au panneau d'administration Django :
```bash
python manage.py createsuperuser

#### 3.3 - Lancer le Serveur
Démarrez le serveur local :
```bash
python manage.py runserver

### Accédez à l'interface administrateur
Accédez à l'interface administrateur à l'adresse suivante :  
[http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 4. Configuration et Compilation C++

### 4.1 - Installation des Bibliothèques C++
Le projet utilise les bibliothèques suivantes :
- `nlohmann/json` pour la gestion des données JSON
- `cpr` pour les requêtes HTTP
- `Eigen3` pour les calculs mathématiques

Ces bibliothèques sont gérées automatiquement par CMake via `FetchContent`.

### 4.2 - Préparer la Compilation
Configurez le projet avec CMake dans un dossier `build` dédié :
```bash
cmake -B build -S .

### 4.3 - Compiler le Projet
Compilez le programme :
```bash
cmake --build build

### 4.4 - Exécuter le Programme
Lancez le programme compilé :
```bash
./build/low_level

## 5. Fonctionnalités Principales

- **API Django** :
  - Modèles définis pour `Ville`, `Usine`, `Machine`, `Produit`, et bien plus.
  - Points de terminaison pour récupérer des données en JSON.
  
- **C++** :
  - Interaction avec l'API Django via des requêtes REST.
  - Classes C++ pour modéliser les entités et afficher leurs données.

---

## 6. Dépendances Techniques

- **Python** : Django pour la gestion du backend.
- **C++** :
  - `nlohmann/json` pour manipuler les données JSON.
  - `cpr` pour effectuer des requêtes REST.
  - `Eigen3` pour les calculs mathématiques.

---

## 7. Améliorations Futures

- Support pour des bases de données avancées comme PostgreSQL.
- Ajout de tests unitaires automatisés pour les deux parties.
- Optimisation des appels API et gestion des erreurs dans le client C++.
