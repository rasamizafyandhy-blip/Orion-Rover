from trajectoire_complete import generer_trajectoire, mouvements
import math

R = 0.032       # Rayon des roues (m)
L = 0.15        # Distance entre les roues (m), provisoire

trajectoire = generer_trajectoire(mouvements)


def calculer_tours(distance):
    return distance / (2 * math.pi * R)


def calculer_rotation(angle_degres):

    angle = math.radians(angle_degres)

    distance_gauche = -(L * angle) / 2
    distance_droite = (L * angle) / 2

    tours_gauche = calculer_tours(distance_gauche)
    tours_droite = calculer_tours(distance_droite)

    return tours_gauche, tours_droite


if __name__ == "__main__":

    print("===== SEQUENCE DE DEPLACEMENT DU ROVER =====")

    for i, segment in enumerate(trajectoire):

        # Effectuer le virage avant le segment
        angle = segment["angle_deg"]

        if angle != 0:

            gauche, droite = calculer_rotation(angle)

            print(f"\nACTION : ROTATION {angle} degrés")
            print(f"Roue gauche : {gauche:.2f} tours")
            print(f"Roue droite : {droite:.2f} tours")

        # Avancer sur le segment
        distance = segment["distance_m"]
        tours = calculer_tours(distance)

        print(f"\nACTION : AVANCER {distance:.2f} m")
        print(f"Roue gauche : {tours:.2f} tours")
        print(f"Roue droite : {tours:.2f} tours")
