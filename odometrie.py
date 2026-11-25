
import math


R = 0.032  # rayon du pneu 
L = 0.15   # distance entre les roues (valeur provisoire)

# Résolution simulée
# À remplacer par la résolution réelle des encodeurs optiques
P = 360  # impulsions comptées par tour de roue (simulation)

# Position initiale du rover
x = 0.0
y = 0.0
theta = 0.0

def mettre_a_jour_odometrie(N_gauche, N_droite):
    global x, y, theta

    # Distance parcourue par chaque roue
    dg = (N_gauche / P) * (2 * math.pi * R)
    dd = (N_droite / P) * (2 * math.pi * R)

    # Déplacement du centre du rover
    ds = (dg + dd) / 2

    # Variation de l'orientation
    dtheta = (dd - dg) / L

    # Mise à jour de la position
    x += ds * math.cos(theta + dtheta / 2)
    y += ds * math.sin(theta + dtheta / 2)
    theta += dtheta

    return x, y, theta


# Impulsions simulées reçues à chaque intervalle
mesures = [
    (360, 360),  # avance tout droit
    (360, 180),  # tourne à droite
    (180, 360)   # tourne à gauche
]

print(" ODOMETRIE AVEC ENCODEURS OPTIQUES ")

for i, (N_gauche, N_droite) in enumerate(mesures, start=1):

    x, y, theta = mettre_a_jour_odometrie(
        N_gauche, N_droite
    )

    print(f"\nÉtape {i}")
    print(f"Impulsions gauche : {N_gauche}")
    print(f"Impulsions droite : {N_droite}")
    print(f"X : {x:.3f} m")
    print(f"Y : {y:.3f} m")
    print(f"Orientation : {math.degrees(theta):.2f} degrés")
