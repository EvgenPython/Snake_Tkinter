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
        self.canvas.tag_bind(self.rect, "<Button-1>", self.on_click)

    def on_click(self, event):
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

    def place_all_ships(self):
        for size, count in SHIP_SIZES.items():
            for _ in range(count):
                placed = False
                while not placed:
                    placed = self.try_place_ship(size)

    def try_place_ship(self, size):
        orientation = random.choice(["H", "V"])
        if orientation == "H":
            x = random.randint(0, GRID_SIZE - size)
            y = random.randint(0, GRID_SIZE - 1)
            coords = [(x + i, y) for i in range(size)]
        else:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - size)
            coords = [(x, y + i) for i in range(size)]

        if any(self.grid[cx][cy].has_ship for cx, cy in coords):
            return False

        for cx, cy in coords:  # [(1,2),  (3,4), (4,5)]
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                        if self.grid[nx][ny].has_ship and (nx, ny) not in coords:
                            return False
        for cx, cy in coords:
            self.grid[cx][cy].has_ship = True
            if self.owner == "player":
                self.grid[cx][cy].canvas.itemconfig(self.grid[cx][cy].rect, fill="green")
        return True

    def all_ships_destroy(self):
        all()

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
