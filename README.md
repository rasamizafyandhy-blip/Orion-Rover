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
