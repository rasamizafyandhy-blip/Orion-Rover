
from astar import astar
from mouvements import generer_mouvements
import math

# Paramètres provisoires
RAYON_ROUE = 0.032       # mètres
TAILLE_CASE = 0.10      # mètres (hypothèse)
DISTANCE_ROUES = 0.15   # mètres (à mesurer)

# Calcul du chemin
chemin = astar()

# Génération des mouvements
mouvements = generer_mouvements(chemin)


def calculer_angle(direction_precedente, direction_actuelle):

    directions = {
        "HAUT": 0,
        "DROITE": 90,
        "BAS": 180,
        "GAUCHE": 270
    }

    difference = (
        directions[direction_actuelle]
        - directions[direction_precedente]
    )

    if difference > 180:
        difference -= 360
    elif difference < -180:
        difference += 360

    return difference


def generer_trajectoire(mouvements):

    trajectoire = []

    for i, mouvement in enumerate(mouvements):

        distance = mouvement["cases"] * TAILLE_CASE

        segment = {
            "direction": mouvement["direction"],
            "distance_m": distance,
            "angle_deg": 0
        }

        if i > 0:
            segment["angle_deg"] = calculer_angle(
                mouvements[i - 1]["direction"],
                mouvement["direction"]
            )

        trajectoire.append(segment)

    return trajectoire


if __name__ == "__main__":

    trajectoire = generer_trajectoire(mouvements)

    print("===== TRAJECTOIRE COMPLETE =====")

    for i, segment in enumerate(trajectoire):

        print(f"\nSegment {i + 1}")
        print("Direction :", segment["direction"])
        print("Distance :", segment["distance_m"], "m")
        print("Angle :", segment["angle_deg"], "degres")
