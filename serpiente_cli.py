import curses
import random

def juego(ventana):
    curses.curs_set(0)  # Ocultar cursor
    ventana.nodelay(1)  # No bloquear al esperar input
    ventana.timeout(100)  # Velocidad del juego (ms)

    sh, sw = ventana.getmaxyx()  # Tamaño de la ventana
    x = sw//4
    y = sh//2
    serpiente = [[y, x]]
    comida = [sh//2, sw//2]
    ventana.addch(comida[0], comida[1], curses.ACS_PI)

    dx = 1
    dy = 0

    while True:
        tecla = ventana.getch()
        if tecla == curses.KEY_UP and dy == 0:
            dx, dy = 0, -1
        elif tecla == curses.KEY_DOWN and dy == 0:
            dx, dy = 0, 1
        elif tecla == curses.KEY_LEFT and dx == 0:
            dx, dy = -1, 0
        elif tecla == curses.KEY_RIGHT and dx == 0:
            dx, dy = 1, 0

        # Nueva cabeza
        nueva_cabeza = [serpiente[0][0] + dy, serpiente[0][1] + dx]
        serpiente.insert(0, nueva_cabeza)

        # Colisión con bordes o consigo misma
        if (nueva_cabeza[0] in [0, sh] or
            nueva_cabeza[1] in [0, sw] or
            nueva_cabeza in serpiente[1:]):
            curses.endwin()
            print("Game Over! Puntuación:", len(serpiente) - 1)
            break

        # Comer comida
        if nueva_cabeza == comida:
            comida = [random.randint(1, sh-2), random.randint(1, sw-2)]
            ventana.addch(comida[0], comida[1], curses.ACS_PI)
        else:
            # Quitar cola
            cola = serpiente.pop()
            ventana.addch(cola[0], cola[1], ' ')

        ventana.addch(serpiente[0][0], serpiente[0][1], curses.ACS_CKBOARD)

curses.wrapper(juego)
ventana.addstr(0, 2, f"Puntuación: {len(serpiente) - 1}")
