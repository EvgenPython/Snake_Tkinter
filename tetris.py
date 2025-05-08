import tkinter as tk
import random

ROWS, COLS = 20, 10
CELL = 30
DELAY = 400

COLORS = ["cyan", "blue", "orange", "yellow", "green", "purple", "red"]

SHAPES = {
    "I": [[(0, -1), (0, 0), (0, 1), (0, 2)]],
    "J": [[(0, -1), (0, 0), (0, 1), (-1, 1)]],
    "L": [[(0, -1), (0, 0), (0, 1), (1, 1)]],
    "O": [[(0, 0), (1, 0), (0, 1), (1, 1)]],
    "S": [[(0, 0), (1, 0), (0, 1), (-1, 1)]],
    "T": [[(0, -1), (0, 0), (-1, 0), (0, 1)]],
    "Z": [[(0, -1), (0, 0), (1, 0), (1, 1)]],
}

class Tetris:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=(COLS+6)*CELL, height=ROWS*CELL, bg="black")
        self.canvas.pack()
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.score = 0
        self.game_over = False
        self.current = self.new_shape()
        self.next_shape = self.new_shape()
        self.root.bind("<Key>", self.key_press)
        self.drop()
    def new_shape(self):
        shape = random.choice(list(SHAPES.keys()))
        color = COLORS[list(SHAPES.keys()).index(shape)]
        blocks = SHAPES[shape[0]]
        return {"blocks": blocks, "x": COLS // 2, "y": 1, "color": color, "name": shape}

    def draw_block(self, x, y, color):
        x0, y0 = x * CELL, y * CELL
        self.canvas.create_rectangle(x0, y0, x0+CELL, y0+CELL, fill=color, outline="gray")

    def drop(self):
        self.canvas.delete("all")
        SIDE_X = (COLS + 2) * CELL
        self.canvas.create_text(SIDE_X, 1*CELL, text="Score:", fill="white", font=("Arial", 16))
        self.canvas.create_text(SIDE_X, 2*CELL, text=f"{self.score}", fill="white", font=("Arial", 16))
        self.canvas.create_text(SIDE_X, 4*CELL, text="Next:", fill="white", font=("Arial", 16))
        for y in range(ROWS):
            for x in range(COLS):
                if self.board[y][x]
    def key_press(self):
        pass



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tetris")
    game = Tetris(root)
    root.mainloop()
