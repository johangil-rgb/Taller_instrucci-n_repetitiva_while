# interes_compuesto_pedro_juan

Programa en Python que calcula en cuántos meses Pedro y Juan pueden reunir el dinero necesario para realizar un negocio utilizando interés compuesto mensual.

---

## Problema

Pedro tiene un capital **c1** pesos y Juan tiene un capital **c2** pesos.  
Al unir sus capitales no alcanzan el dinero necesario para realizar un negocio que requiere **c3** pesos.

Deciden invertir su dinero para ganar interés:

- Pedro obtiene **3% de interés compuesto mensual**
- Juan obtiene **4% de interés compuesto mensual**

El programa debe calcular en cuántos meses la suma de sus capitales será suficiente para realizar el negocio.

---

## Diseño

El algoritmo utiliza un **ciclo while** para calcular mes a mes el crecimiento del capital hasta que la suma de ambos capitales alcance o supere el capital requerido.

![alt text][def]

[def]: diagrama.png

---

## Algoritmo

1. Leer los capitales iniciales `c1`, `c2` y el capital requerido `c3`.
2. Inicializar la variable `mes` en 0.
3. Mientras `(c1 + c2) < c3`:
   - Calcular el nuevo capital de Pedro.
   - Calcular el nuevo capital de Juan.
   - Incrementar el número de meses.
4. Mostrar el número de meses necesarios.

---

## Código

```python
# Programa para calcular en cuantos meses Pedro y Juan
# pueden reunir el dinero necesario para un negocio

# -----------------
# input
# -----------------

c1 = float(input("Capital inicial de Pedro: "))
c2 = float(input("Capital inicial de Juan: "))
c3 = float(input("Capital necesario para el negocio: "))

# -----------------
# processing
# -----------------

mes = 0

while (c1 + c2) < c3:
    c1 = c1 * 1.03
    c2 = c2 * 1.04
    mes = mes + 1

# -----------------
# output
# -----------------

print("Meses necesarios para reunir el dinero:", mes)
print("Capital total final:", c1 + c2)
```

---
