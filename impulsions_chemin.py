import math


R = 0.032          # Rayon de roue : 3.2 cm
TAILLE_CASE = 0.10 # Une case = 10 cm (hypothèse)
P = 360            # Impulsions par tour (à vérifier)

# Circonférence de la roue
circonference = 2 * math.pi * R

# Distance pour une case
distance_case = TAILLE_CASE

# Nombre de tours de roue pour une case
tours_case = distance_case / circonference

# Nombre d'impulsions pour une case
impulsions_case = tours_case * P

# Chemin A* : 18 déplacements
nombre_deplacements = 18

# Distance totale
distance_totale = nombre_deplacements * distance_case

# Impulsions pour le trajet en ligne droite
impulsions_totales = nombre_deplacements * impulsions_case

print("===== IMPULSIONS POUR LE CHEMIN A* =====")
print(f"Distance par case : {distance_case * 100:.1f} cm")
print(f"Distance totale : {distance_totale:.2f} m")
print(f"Impulsions par case : {impulsions_case:.1f}")
print(f"Impulsions totales : {impulsions_totales:.0f}")
