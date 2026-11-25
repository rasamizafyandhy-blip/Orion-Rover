
import math


P = 360  # impulsions par tour
T = 2.0  #  temps en s
R = 0.035  # rayon de la roue en mètres

# Impulsions des deux encodeurs
impulsions_gauche = 360
impulsions_droite = 180

# Calcul des fréquences
f_gauche = impulsions_gauche / (P * T)
f_droite = impulsions_droite / (P * T)

# Calcul des vitesses linéaires
v_gauche = 2 * math.pi * R * f_gauche
v_droite = 2 * math.pi * R * f_droite

# Vitesse moyenne du rover
v_rover = (v_gauche + v_droite) / 2

print(" VITESSE DU ROVER")
print(f"Vitesse roue gauche : {v_gauche:.3f} m/s")
print(f"Vitesse roue droite : {v_droite:.3f} m/s")
print(f"Vitesse moyenne : {v_rover:.3f} m/s")

print("\n DIRECTION ")

if v_gauche > v_droite:
    print("Le rover tourne vers la droite.")
elif v_droite > v_gauche:
    print("Le rover tourne vers la gauche.")
else:
    print("Le rover avance tout droit.")
