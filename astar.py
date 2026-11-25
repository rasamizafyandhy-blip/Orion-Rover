
import heapq

# 0 = case libre
# 1 = obstacle

carte = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

depart = (9, 0)
destination = (0, 9)


def heuristique(position):
    ligne, colonne = position
    ligne_dest, colonne_dest = destination

    return abs(ligne - ligne_dest) + abs(colonne - colonne_dest)


def astar():

    cases_a_explorer = []

    heapq.heappush(
        cases_a_explorer,
        (heuristique(depart), depart)
    )

    cout = {depart: 0}
    parent = {}

    while cases_a_explorer:

        _, position = heapq.heappop(cases_a_explorer)

        if position == destination:

            chemin = [position]

            while position in parent:
                position = parent[position]
                chemin.append(position)

            chemin.reverse()
            return chemin

        ligne, colonne = position

        voisins = [
            (ligne - 1, colonne),
            (ligne + 1, colonne),
            (ligne, colonne - 1),
            (ligne, colonne + 1)
        ]

        for voisin in voisins:

            l, c = voisin

            if l < 0 or l >= len(carte):
                continue

            if c < 0 or c >= len(carte[0]):
                continue

            if carte[l][c] == 1:
                continue

            nouveau_cout = cout[position] + 1

            if voisin not in cout or nouveau_cout < cout[voisin]:

                cout[voisin] = nouveau_cout
                parent[voisin] = position

                f = nouveau_cout + heuristique(voisin)

                heapq.heappush(
                    cases_a_explorer,
                    (f, voisin)
                )

    return None


# Exécution uniquement si ce fichier est lancé directement
if __name__ == "__main__":

    chemin = astar()

    print("===== ALGORITHME A* =====")

    if chemin:
        print("Chemin trouvé !")
        print("Nombre de cases :", len(chemin))
        print("Distance :", len(chemin) - 1, "unités")

        for position in chemin:
            print(position)

    else:
        print("Aucun chemin possible.")
