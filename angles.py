
from astar import astar

# Calcul du chemin
chemin = astar()

# Directions de la carte
angles = {
    "HAUT": 90,
    "DROITE": 0,
    "BAS": -90,
    "GAUCHE": 180
}

print("===== ANGLES DE ROTATION =====")

if chemin is not None:

    directions = []

    # Identifier chaque direction
    for i in range(len(chemin) - 1):

        ligne1, colonne1 = chemin[i]
        ligne2, colonne2 = chemin[i + 1]

        if ligne2 < ligne1:
            direction = "HAUT"

        elif ligne2 > ligne1:
            direction = "BAS"

        elif colonne2 > colonne1:
            direction = "DROITE"

        else:
            direction = "GAUCHE"

        directions.append(direction)

    # Calculer les changements de direction
    direction_precedente = directions[0]

    for direction in directions[1:]:

        if direction != direction_precedente:

            angle_initial = angles[direction_precedente]
            angle_final = angles[direction]

            rotation = angle_final - angle_initial

            # Normaliser l'angle entre -180° et 180°
            rotation = (rotation + 180) % 360 - 180

            print(
                f"De {direction_precedente} vers {direction} : "
                f"{rotation} degrés"
            )

            direction_precedente = direction

else:
    print("Aucun chemin trouvé.")
