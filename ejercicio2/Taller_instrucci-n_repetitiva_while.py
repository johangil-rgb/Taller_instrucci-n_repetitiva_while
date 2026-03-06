import random

def juego(equipo):

    jugador_hp = 50
    jefe_hp = 150
    curaciones = 6
    daño_base = 10

    parry_activo = False
    conjuro_activo = False

    esquives = 0
    bonus_cura = 0
    bonus_hp = 0

    if equipo == 1:  # collar sagrado
        daño_base += 3
        jugador_hp += 20
        bonus_cura = 7

    if equipo == 2:  # ultimo aliento
        esquives = 5

    if equipo == 3:  # conjuro
        conjuro_activo = True

    while True:

        print("\n----------------------")
        print("Tu HP:", jugador_hp)
        print("HP del jefe:", jefe_hp)
        print("Curaciones restantes:", curaciones)
        print("----------------------")

        if conjuro_activo:
            print("(a) atacar  (c) curarse  (k) conjuro")
        else:
            print("(a) atacar  (c) curarse  (p) parry")

        # oportunidad de parry
        parry_disponible = random.randint(1,10) == 1
        if parry_disponible and not conjuro_activo:
            print("¡Oportunidad de PARRY!")

        # oportunidad de conjuro
        conjuro_disponible = random.randint(1,4) == 1
        if conjuro_disponible and conjuro_activo:
            print("¡Puedes usar CONJURO!")

        accion = input("Acción: ").lower()

        daño_jugador = 0

        if accion == "a":
            daño_jugador = random.randint(8,15) + daño_base

        elif accion == "c" and curaciones > 0:
            curar = random.randint(18,25) + bonus_cura
            if curar > 32:
                curar = 32
            jugador_hp += curar
            curaciones -= 1
            print("Te curaste:", curar)

        elif accion == "p" and parry_disponible and not conjuro_activo:
            daño_jugador = random.randint(18,30)
            print("¡Parry exitoso!")

        elif accion == "k" and conjuro_disponible and conjuro_activo:
            daño_jugador = random.randint(12,20)
            print("Conjuro lanzado!")

        jefe_hp -= daño_jugador

        if daño_jugador > 0:
            print("Le hiciste", daño_jugador, "de daño al jefe")

        if jefe_hp <= 0:
            print("¡Ganaste!")
            break

        # ataque del jefe
        daño_jefe = random.randint(10,18)

        if equipo == 2 and jugador_hp <= 20:
            daño_base += 9
            print("¡Ultimo aliento activado! +9 daño")

            if esquives > 0 and random.randint(1,3) == 1:
                esquives -= 1
                print("¡Esquivaste el ataque!")
                daño_jefe = 0

        jugador_hp -= daño_jefe

        print("El jefe te hizo", daño_jefe, "de daño")

        if jugador_hp <= 0:
            print("\nHas perdido")
            r = input("Presiona (r) para reiniciar: ")
            if r == "r":
                break


while True:

    print("\n====== MENU ======")
    print("(i) iniciar juego")
    print("(e) equipamiento")
    print("==================")

    opcion = input("Selecciona: ").lower()

    if opcion == "i":
        juego(0)

    elif opcion == "e":

        print("\nEquipamiento")
        print("1 Collar sagrado")
        print("2 Último aliento")
        print("3 Conjuro")

        eleccion = int(input("Elige: "))
        juego(eleccion)