
Kp = 0.8
Ki = 0.05
Kd = 0.1

distance_demandee = 90.0
distance_mesuree = 70.0

erreur_precedente = 0.0
integrale = 0.0
dt = 0.1

tolerance = 1.0
max_iterations = 100

print("===== SIMULATION PID =====")

for i in range(max_iterations):

    erreur = distance_demandee - distance_mesuree

    if abs(erreur) <= tolerance:
        print("\nObjectif atteint dans la tolerance !")
        break

    integrale += erreur * dt
    derivee = (erreur - erreur_precedente) / dt

    correction = (
        Kp * erreur
        + Ki * integrale
        + Kd * derivee
    )

    # Modèle simplifié de déplacement
    distance_mesuree += correction * 0.1

    erreur_precedente = erreur

    print(
        f"Iteration {i + 1} | "
        f"Distance : {distance_mesuree:.2f} cm | "
        f"Erreur : {erreur:.2f} cm"
    )

else:
    print("\nNombre maximal d'iterations atteint.")

print("\n===== BILAN =====")
print(f"Distance demandee : {distance_demandee:.2f} cm")
print(f"Distance finale : {distance_mesuree:.2f} cm")
print(f"Erreur finale : {abs(distance_demandee - distance_mesuree):.2f} cm")
