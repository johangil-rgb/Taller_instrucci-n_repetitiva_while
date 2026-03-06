# juego_rpg_jefe

Programa en Python que simula un combate contra un jefe utilizando un **bucle while**.  
El jugador puede atacar, curarse, usar parry o conjuro y elegir equipamiento antes de iniciar la partida.

---

# Descripción

El jugador comienza con **50 puntos de vida (HP)** y debe luchar contra un jefe.

En cada turno:

- El jugador elige una acción.
- El jefe realiza un ataque con daño aleatorio.
- El combate continúa hasta que uno de los dos llegue a **0 HP**.

El programa utiliza:

- **while** para repetir los turnos
- **break** para terminar el combate cuando alguien pierde

---

# Diseño

![alt text][def]

[def]: diagrama.png

El diagrama muestra el flujo del combate usando un ciclo **while**.

---

# Menú principal

Al iniciar el programa aparecen dos opciones:
