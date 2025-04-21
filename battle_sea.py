import tkinter as tk
import random

CELL_SIZE = 30
GRID_SIZE = 10

SHIP_SIZES = {4: 1, 3: 2, 2: 3, 1: 4}


class Cell:
    def __init__(self, canvas, x, y, owner, click_callback=None):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.owner = owner
        self.hit = False
        self.has_ship = False
        self.click_callback = click_callback
        x1, y1, = x * CELL_SIZE, y * CELL_SIZE
        x2, y2 = x1 * CELL_SIZE, y1 * CELL_SIZE
        self.rect = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
        # self.canvas.tag_bin(self.rect, "<Button-1>", self.on_click)

    def on_click(self):
        if self.click_callback and self.owner == "comp":
            self.click_callback(self)

    def mark_hit(self, hit):
        self.hit = True
        color = "red" if hit else "gray"
        self.canvas.itemconfig(self.rect, color)


class Board:
    def __init__(self, root, owner, x_offset, click_callback=None):
        self.canvas = tk.Canvas(root, width=CELL_SIZE * GRID_SIZE, height=CELL_SIZE * GRID_SIZE)
        self.canvas.place(x=x_offset, y=50)
        self.owner = owner
        self.grid = [[Cell(self.canvas, x, y, owner, click_callback) for y in range(GRID_SIZE)] for x in
                     range(GRID_SIZE)]

class SeaBattleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sea")
        self.player_board = Board(root, "player", x_offset=50)
        self.comp_board = Board(root, "comp", x_offset=400)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x400")
    game = SeaBattleGame(root)
    root.mainloop()
