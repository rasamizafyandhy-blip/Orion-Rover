
import math


impulsions_par_tour = 360
rayon_roue = 0.035  # m
impulsions = 360
temps = 2.0  # s

# Calcul du nombre de tours par seconde
frequence = impulsions / (impulsions_par_tour * temps)

# Calcul de la vitesse angulaire
vitesse_angulaire = 2 * math.pi * frequence

# Calcul de la vitesse linéaire
vitesse_lineaire = vitesse_angulaire * rayon_roue

print(" VITESSE DE LA ROUE ")
print(f"Fréquence : {frequence:.2f} tours/s")
print(f"Vitesse angulaire : {vitesse_angulaire:.2f} rad/s")
print(f"Vitesse linéaire : {vitesse_lineaire:.3f} m/s")
print(f"Vitesse linéaire : {vitesse_lineaire * 100:.2f} cm/s")
