#################################################################################
# Copyright (C) 2026 Binryan-void y Patagonian Boy
#
# Este programa es software libre: puedes redistribuirlo y/o modificarlo
# bajo los terminos de la Licencia Publica General GNU publicada por la 
# Free Software Foundation, ya sea la version 3 de la Licencia o 
# (a tu eleccion) cualquier version posterior
#
# Este programa se distribuye con la esperanza de que sea util, pero 
# SIN GARANTIA ALGUNA; ni siquiera garantia implicita de 
# MERCANTILIDAD o APTITUD PARA UN PROPOSITO DETERMINADO.
# Consulte la Licencia Publica General GNU para obtener mas detalles.
#
# Deberias haber recibido una copia de la Licencia Publica General GNU 
# junto con este programa. Si no es asi, consulta <https://www.gnu.org/licenses/>.
##################################################################################

import tkinter as tk
import random

# Configuración inicial
WIDTH = 400
HEIGHT = 400
SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de la Serpiente")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.running = True

        self.root.bind("<KeyPress>", self.change_direction)
        self.update()

    def create_food(self):
        x = random.randint(0, (WIDTH - SIZE) // SIZE) * SIZE
        y = random.randint(0, (HEIGHT - SIZE) // SIZE) * SIZE
        return (x, y)

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym

    def move(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= SIZE
        elif self.direction == "Down":
            head_y += SIZE
        elif self.direction == "Left":
            head_x -= SIZE
        elif self.direction == "Right":
            head_x += SIZE

        new_head = (head_x, head_y)

        # Colisiones
        if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in self.snake):
            self.running = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.create_food()
        else:
            self.snake.pop()

    def update(self):
        if self.running:
            self.move()
            self.canvas.delete("all")

            # Dibujar comida
            self.canvas.create_rectangle(self.food[0], self.food[1],
                                         self.food[0] + SIZE, self.food[1] + SIZE,
                                         fill="red")

            # Dibujar serpiente
            for x, y in self.snake:
                self.canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill="green")

            self.root.after(100, self.update)
        else:
            self.canvas.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER", fill="white", font=("Arial", 24))

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
