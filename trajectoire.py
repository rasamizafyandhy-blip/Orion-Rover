
import matplotlib.pyplot as plt

from astar import carte, depart, destination, astar

# Calcul du chemin
chemin = astar()

# Affichage de la carte
plt.figure(figsize=(8, 8))

plt.imshow(carte, cmap="Greys", origin="upper")

# Coordonnées du chemin
if chemin is not None:
    lignes = [position[0] for position in chemin]
    colonnes = [position[1] for position in chemin]

    plt.plot(colonnes, lignes, marker="o", label="Chemin A*")

# Départ et destination
plt.scatter(depart[1], depart[0], label="Départ")
plt.scatter(destination[1], destination[0], label="Destination")

plt.title("Trajectoire du rover - Algorithme A*")
plt.xlabel("Colonnes")
plt.ylabel("Lignes")

plt.xticks(range(len(carte[0])))
plt.yticks(range(len(carte)))

plt.grid(True)
plt.legend()
plt.show()
