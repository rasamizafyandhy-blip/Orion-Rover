import math

# Valeurs simulées
P = 360
R = 0.035

# Impulsions des encodeurs
impulsions_gauche = 360
impulsions_droite = 360

# Calcul de la distance de chaque roue
distance_gauche = (
    impulsions_gauche / P
) * (2 * math.pi * R)

distance_droite = (
    impulsions_droite / P
) * (2 * math.pi * R)

# Distance parcourue par le centre du rover
distance_rover = (
    distance_gauche + distance_droite
) / 2

print("    DISTANCE PARCOURUE PAR LE ROVER ")

print(f"Roue gauche : {distance_gauche:.3f} m")
print(f"Roue droite : {distance_droite:.3f} m")

print(f"Distance du rover : {distance_rover:.3f} m")

print(f"En cm : {distance_rover * 100:.2f} cm")