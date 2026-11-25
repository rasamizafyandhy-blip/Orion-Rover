
import math

VITESSE_SON = 343  # m/s
DISTANCE_SECURITE = 0.20  # 20 cm

# Temps d'écho simulé, en secondes
temps_echo = 0.002

# Calcul de la distance
distance = (VITESSE_SON * temps_echo) / 2

# Le capteur est orienté vers l'avant : angle 0°
angle = 0
theta = math.radians(angle)

# Calcul des coordonnées de l'obstacle
x = distance * math.cos(theta)
y = distance * math.sin(theta)

print("\n CAPTEUR HC-SR04 ")
print(f"Distance : {distance:.3f} m")
print(f"Distance : {distance * 100:.1f} cm")
print(f"X : {x:.3f} m")
print(f"Y : {y:.3f} m")

print("\n  DECISION DU ROBOT")

if distance <= DISTANCE_SECURITE:
    print("DANGER ! Obstacle trop proche.")
    print("ACTION : ARRETER LE ROBOT")
else:
    print("Zone libre.")
    print("ACTION : LE ROBOT PEUT AVANCER")
