# adivinar_numero

Programa en Python donde la computadora genera un número aleatorio entre **1 y 100** y el usuario debe adivinarlo.

## Descripción

El programa utiliza un **bucle `while`** que se repite hasta que el usuario adivina el número correcto.

Cada vez que el usuario introduce un número, el programa da una pista:

- **"Más alto"** si el número secreto es mayor.
- **"Más bajo"** si el número secreto es menor.
- **"¡Correcto!"** cuando el usuario adivina el número.

El juego termina cuando el usuario acierta.

---

## Diseño

![alt text][def]

[def]: diagrama.png

El diagrama de flujo muestra cómo el programa:

1. Genera un número aleatorio.
2. Pide un número al usuario.
3. Compara el número ingresado con el número secreto.
4. Da pistas para ayudar al usuario.
5. Repite el proceso usando un **ciclo `while`** hasta acertar.

[def]: 2fdde9968756a881f56c26af1feca42c.jpg