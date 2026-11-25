
from astar import astar

# Récupérer automatiquement le chemin A*
chemin = astar()


def determiner_direction(position_actuelle, position_suivante):

    ligne1, colonne1 = position_actuelle
    ligne2, colonne2 = position_suivante

    if ligne2 < ligne1:
        return "HAUT"

    elif ligne2 > ligne1:
        return "BAS"

    elif colonne2 < colonne1:
        return "GAUCHE"

    elif colonne2 > colonne1:
        return "DROITE"


def generer_mouvements(chemin):

    if chemin is None or len(chemin) < 2:
        return []

    mouvements = []

    for i in range(len(chemin) - 1):

        direction = determiner_direction(
            chemin[i],
            chemin[i + 1]
        )

        if mouvements and mouvements[-1]["direction"] == direction:
            mouvements[-1]["cases"] += 1

        else:
            mouvements.append({
                "direction": direction,
                "cases": 1
            })

    return mouvements


if __name__ == "__main__":

    mouvements = generer_mouvements(chemin)

    print("===== MOUVEMENTS DU ROVER =====")

    for mouvement in mouvements:
        print(
            mouvement["direction"],
            "->",
            mouvement["cases"],
            "cases"
        )
