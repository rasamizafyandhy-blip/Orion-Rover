# 🤖 Robot Rover Livreur Autonome

## 1. Présentation du projet

Ce projet consiste à concevoir et réaliser un robot rover livreur autonome capable de transporter des livraisons vers plusieurs destinations.

Le robot reçoit ses commandes depuis une interface web, suit une piste au sol, détecte et évite les obstacles et reconnaît différents panneaux grâce à l'intelligence artificielle.

**Projet :** Atelier pilote TECH V2  
**Établissement :** ORION UNIVERSITY  
**Thème :** A — Robot rover livreur autonome

## 2. Objectifs du projet

- Commander le rover depuis une interface web.
- Suivre automatiquement une piste.
- Détecter et éviter les obstacles.
- Reconnaître six classes de panneaux grâce à l'IA.
- Effectuer plusieurs livraisons successives.
- Afficher la position et la trajectoire du rover en temps réel.

## 3. Technologies utilisées

| Domaine | Technologies |
|---|---|
| Électronique | ESP32, capteurs, moteurs |
| Robotique | C/C++, Arduino IDE, PID |
| Intelligence artificielle | Python, TensorFlow/Keras |
| Développement web | HTML, CSS, JavaScript, Flask |
| Base de données | SQLite |
| Gestion de projet | Git, GitHub, Kanban |

## 4. Organisation de l'équipe

| Membre | Responsabilité |
|---|---|
| Membre 1 | Électronique |
| Membre 2 | Robotique |
| Membre 3 | Mathématiques |
| Membre 4 | Intelligence artificielle |
| Membre 5 | Développement web |

## 5. Structure du projet

```text
rover-livreur-autonome/
│
├── electronique/
│   └── schemas/
│
├── robotique/
│   └── firmware/
│
├── mathematiques/
│   └── calculs/
│
├── intelligence-artificielle/
│   ├── dataset/
│   ├── modeles/
│   └── entrainement/
│
├── web/
│   ├── templates/
│   ├── static/
│   └── app.py
│
├── documentation/
│   ├── rapports/
│   └── images/
│
└── tests/
```


## 6. Mathématiques et algorithmique du rover

Cette partie regroupe les calculs mathématiques et les algorithmes nécessaires au déplacement du rover, à l'estimation de sa position et à la préparation de ses trajectoires.

### 6.1 Paramètres du rover

| Paramètre | Valeur | État |
|---|---:|---|
| Rayon des roues | 3,2 cm | Confirmé |
| Rayon en mètres | 0,032 m | Confirmé |
| Circonférence d'une roue | 0,201 m environ | Calculée |
| Distance entre les roues motrices | 0,15 m | Provisoire, à mesurer |
| Taille d'une case de simulation | 10 cm | Hypothèse |
| Résolution des encodeurs | À déterminer | En attente du matériel |

**Remarque :** les moteurs DC actuellement utilisés ne disposent pas d'encodeurs. Les calculs liés aux impulsions et à l'odométrie sont donc théoriques ou simulés en attendant l'installation des encodeurs.

### 6.2 Cinématique des roues

La circonférence d'une roue est calculée avec :

C = 2 × π × R

Avec un rayon de 0,032 m, la circonférence est d'environ 0,201 m.

Cette valeur permet d'estimer la distance parcourue à partir du nombre de tours de roue.

### 6.3 Cinématique du rover

Le rover utilise deux roues motrices indépendantes.

Les déplacements sont calculés à partir des distances parcourues par la roue gauche et la roue droite.

- Avancer : les deux roues tournent dans le même sens.
- Reculer : les deux roues tournent en sens inverse du déplacement avant.
- Tourner : les roues tournent à des vitesses différentes.
- Rotation sur place : les deux roues tournent en sens opposés.

### 6.4 Odométrie

L'odométrie permet d'estimer la position et l'orientation du rover à partir des déplacements de ses roues.

Elle utilisera les informations des encodeurs optiques ou magnétiques qui seront ajoutés aux moteurs.

Le capteur MPU6050 pourra également contribuer à l'estimation de l'orientation.

**Limite actuelle :** les déplacements réels ne peuvent pas encore être mesurés par encodeurs.

### 6.5 Recherche de chemin avec A*

L'algorithme A* est utilisé pour rechercher un chemin entre une position de départ et une destination sur une carte en grille.

Le principe :
- 0 représente une case libre.
- 1 représente un obstacle.
- Le rover recherche un chemin en évitant les obstacles.
- La distance est estimée avec la distance de Manhattan.

Une première simulation sur une grille de 10 × 10 a produit :
- 19 positions dans le chemin.
- 18 déplacements.
- 9 cases vers le haut.
- 9 cases vers la droite.

Avec une taille de case provisoire de 10 cm, la distance théorique est de 1,80 m.

### 6.6 Génération de trajectoire

Le chemin calculé par A* est transformé en instructions de déplacement.

Exemple de simulation :
1. Avancer de 0,90 m.
2. Effectuer une rotation de 90°.
3. Avancer de 0,90 m.

Les rotations et les distances sont ensuite converties en nombres de tours de roues.

Ces valeurs restent théoriques tant que les paramètres réels du rover ne sont pas mesurés.

### 6.7 Régulation PID

Une simulation PID a été réalisée pour illustrer la correction de la distance parcourue.

Exemple :
- Distance demandée : 90 cm.
- Distance finale simulée : 89,11 cm.
- Erreur finale : 0,89 cm.
- Tolérance de simulation : 1 cm.

Cette simulation ne représente pas encore une régulation réelle du moteur. Les coefficients PID devront être ajustés après l'installation des encodeurs et les essais physiques.

### 6.8 Évaluation de la précision

Le RMSE (Root Mean Square Error) permettra de mesurer l'écart entre les positions réelles et les positions estimées par l'odométrie.

Il sera utilisé lors des essais physiques pour évaluer la précision du déplacement.

Les premières valeurs utilisées dans le script sont uniquement des exemples de simulation.

### 6.9 État d'avancement

| Travail | État |
|---|---|
| Calcul du rayon et de la circonférence des roues | Calcul effectué |
| Calculs de vitesse et de distance | Simulation réalisée |
| Cinématique différentielle | Calculs réalisés |
| Algorithme A* | Simulation réalisée |
| Génération des mouvements | Simulation réalisée |
| Calcul des rotations et tours de roues | Simulation réalisée |
| Simulation PID | Réalisée |
| Préparation du calcul RMSE | Réalisée avec des données d'exemple |
| Odométrie avec encodeurs réels | En attente du matériel |
| Validation des déplacements physiques | À réaliser |
| Ajustement du PID sur le rover | À réaliser |



## 6. Panneaux à reconnaître

Le système d'intelligence artificielle doit reconnaître six classes :

1. STOP
2. Tourner à gauche
3. Tourner à droite
4. Ralentir
5. Arrivée
6. Aucun panneau

Le modèle sera adapté et réentraîné avec le dataset construit par notre groupe, conformément au règlement du concours.

## 7. Méthode de travail

Le projet est organisé selon la méthode Kanban.

Les tâches sont suivies sur GitHub Projects avec les statuts :

- À faire (Todo)
- En cours (In Progress)
- À vérifier (In Review)
- Terminé (Done)

Chaque membre travaille sur les tâches qui lui sont attribuées et versionne ses contributions avec Git.

## 8. État d'avancement

**Statut :** En cours de développement.

Les différentes parties du projet sont développées progressivement avant leur intégration dans le rover final.

## 9. Équipe

Projet réalisé par une équipe de cinq membres d'ORION UNIVERSITY.

**Objectif final :** réaliser un rover capable d'effectuer des livraisons de manière autonome, intelligente et sécurisée.
