
# Paramètres PID (valeurs initiales de simulation)
Kp = 2.0
Ki = 0.1
Kd = 0.5

# Objectif et mesure simulée
distance_demandee = 90.0  # cm
distance_mesuree = 85.0   # cm

# Erreur
erreur = distance_demandee - distance_mesuree

# Mémoire du PID
erreur_precedente = 0.0
integrale = 0.0
dt = 0.1

# Calcul PID
integrale += erreur * dt
derivee = (erreur - erreur_precedente) / dt

correction = (
    Kp * erreur
    + Ki * integrale
    + Kd * derivee
)

print("===== CORRECTEUR PID =====")
print(f"Erreur : {erreur:.2f} cm")
print(f"Correction PID : {correction:.2f}")
