import math


R = 0.032       # Rayon de roue en mètres
L = 0.15        # Distance entre les roues en mètres
P = 360         # Impulsions par tour de roue (à vérifier)

# Rotation de 90 degrés vers la droite
theta = math.radians(90)

# Distance parcourue par chaque roue pendant la rotation
distance_gauche = -(L * theta) / 2
distance_droite = (L * theta) / 2

# Nombre de tours de roue
tours_gauche = distance_gauche / (2 * math.pi * R)
tours_droite = distance_droite / (2 * math.pi * R)

# Nombre d'impulsions
impulsions_gauche = tours_gauche * P
impulsions_droite = tours_droite * P

print("===== IMPULSIONS DES ENCODEURS =====")
print(f"Roue gauche : {impulsions_gauche:.0f} impulsions")
print(f"Roue droite : {impulsions_droite:.0f} impulsions")
