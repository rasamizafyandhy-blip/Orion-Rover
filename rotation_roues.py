import math


R = 0.032  # rayon de roue : 3,2 cm
L = 0.15   # distance entre les roues (provisoire)

# Angle de rotation souhaité
angle_deg = 90

# Conversion en radians
angle_rad = math.radians(angle_deg)

# Distance parcourue par chaque roue
distance_gauche = -(L * angle_rad) / 2
distance_droite = (L * angle_rad) / 2

# Circonférence des roues
circonference = 2 * math.pi * R

# Nombre de tours de roue
tours_gauche = distance_gauche / circonference
tours_droite = distance_droite / circonference

print("===== ROTATION DES ROUES =====")

print(f"Angle de rotation : {angle_deg} degrés")

print(f"Distance roue gauche : {distance_gauche:.3f} m")
print(f"Distance roue droite : {distance_droite:.3f} m")

print(f"Nombre de tours gauche : {tours_gauche:.2f}")
print(f"Nombre de tours droite : {tours_droite:.2f}")
