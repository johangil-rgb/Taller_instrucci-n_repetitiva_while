# ---------------------------------------------------------
# Programa: Inversion Pedro y Juan
# Descripción:
# Calcula en cuántos meses Pedro y Juan pueden reunir
# el dinero necesario para realizar un negocio, usando
# interés compuesto mensual.
#
# Pedro: 3% mensual
# Juan : 4% mensual
# ---------------------------------------------------------

# -----------------
# LIBRERÍAS
# -----------------

import math

# -----------------
# INPUT
# -----------------

print("=====================================")
print("  CALCULADORA DE INVERSIÓN MENSUAL")
print("=====================================")

c1 = float(input("Ingrese el capital inicial de Pedro: "))
c2 = float(input("Ingrese el capital inicial de Juan: "))
c3 = float(input("Ingrese el capital necesario para el negocio: "))

# -----------------
# VALIDACIÓN
# -----------------

if c1 < 0 or c2 < 0 or c3 <= 0:
    print("Error: los valores deben ser positivos.")
else:

    # -----------------
    # PROCESAMIENTO
    # -----------------

    mes = 0
    tasa_pedro = 0.03
    tasa_juan = 0.04

    capital_pedro = c1
    capital_juan = c2

    print("\nEvolución del capital mes a mes")
    print("---------------------------------------")
    print("Mes | Capital Pedro | Capital Juan | Total")

    while (capital_pedro + capital_juan) < c3:
        mes += 1

        capital_pedro = capital_pedro * (1 + tasa_pedro)
        capital_juan = capital_juan * (1 + tasa_juan)

        total = capital_pedro + capital_juan

        print(mes, "|",
              round(capital_pedro,2), "|",
              round(capital_juan,2), "|",
              round(total,2))

    # -----------------
    # OUTPUT
    # -----------------

    print("\n=====================================")
    print("RESULTADOS")
    print("=====================================")

    print("Meses necesarios:", mes)
    print("Capital final de Pedro:", round(capital_pedro,2))
    print("Capital final de Juan:", round(capital_juan,2))
    print("Capital total acumulado:", round(capital_pedro + capital_juan,2))

    if (capital_pedro + capital_juan) >= c3:
        print("Pedro y Juan ya pueden realizar el negocio.")