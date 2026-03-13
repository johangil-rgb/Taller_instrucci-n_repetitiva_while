# -----------------
# Programa para calcular en qué rebote
# la pelota no alcanza la quinta parte
# de la altura inicial
# -----------------

# -----------------
# input
# -----------------
h = float(input("Ingrese la altura inicial de la pelota: "))

# -----------------
# processing
# -----------------
altura = h
rebote = 0
limite = h / 5

while altura >= limite:
    rebote = rebote + 1
    altura = altura * 0.9

# -----------------
# output
# -----------------
print("La pelota deja de superar la quinta parte de la altura inicial en el rebote:", rebote)