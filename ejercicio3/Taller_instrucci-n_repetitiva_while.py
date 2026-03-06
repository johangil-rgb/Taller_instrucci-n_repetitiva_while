# -----------------------------------
# Juego: Adivina el número
# -----------------------------------

# -----------------
# libraries
# -----------------
import random

# -----------------
# input
# -----------------
numero_secreto = random.randint(1, 100)
intento = int(input("Adivina el número (1-100): "))

# -----------------
# processing
# -----------------
while intento != numero_secreto:

    if intento < numero_secreto:
        print("Más alto")
    else:
        print("Más bajo")

    intento = int(input("Intenta de nuevo: "))

# -----------------
# output
# -----------------
print("¡Correcto! Adivinaste el número")