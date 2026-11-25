
import math

# Paramètres du rover
P = 360       # impulsions par tour
R = 0.035    # rayon de roue 
L = 0.15      # distance entre les roues : 15 cm (simulation)

# Impulsions simulées des encodeurs
N_gauche = 360
N_droite = 180

# Position initiale du rover
x = 0.0
y = 0.0
theta = 0.0   # angle initial en radians

# Distance parcourue par chaque roue
dg = (N_gauche / P) * (2 * math.pi * R)
dd = (N_droite / P) * (2 * math.pi * R)

# Déplacement du centre du rover
ds = (dg + dd) / 2

# Variation de l'angle du rover
dtheta = (dd - dg) / L

# Mise à jour de la position
x_new = x + ds * math.cos(theta + dtheta / 2)
y_new = y + ds * math.sin(theta + dtheta / 2)

# Nouvel angle
theta_new = theta + dtheta

print(" CINEMATIQUE DU ROVER ")
print(f"Distance roue gauche : {dg:.3f} m")
print(f"Distance roue droite : {dd:.3f} m")
print(f"Déplacement du centre : {ds:.3f} m")

print("\n NOUVELLE POSITION ")
print(f"X : {x_new:.3f} m")
print(f"Y : {y_new:.3f} m")
print(f"Angle : {math.degrees(theta_new):.2f} degrés")
