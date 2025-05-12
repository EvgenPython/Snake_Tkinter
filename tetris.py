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
        self.drop() # тут drop()
    def new_shape(self):
        shape = random.choice(list(SHAPES.keys()))
        color = COLORS[list(SHAPES.keys()).index(shape)]
        blocks = SHAPES[shape][0]
        return {"blocks": blocks, "x": COLS // 2, "y": 1, "color": color, "name": shape}

    def draw_block(self, x, y, color):
        x0, y0 = x * CELL, y * CELL
        self.canvas.create_rectangle(x0, y0, x0+CELL, y0+CELL, fill=color, outline="gray")

    def draw(self):
        self.canvas.delete("all")
        SIDE_X = (COLS + 2) * CELL
        self.canvas.create_text(SIDE_X, 1*CELL, text="Score:", fill="white", font=("Arial", 16))
        self.canvas.create_text(SIDE_X, 2*CELL, text=f"{self.score}", fill="white", font=("Arial", 16))
        self.canvas.create_text(SIDE_X, 4*CELL, text="Next:", fill="white", font=("Arial", 16))
        for y in range(ROWS):
            for x in range(COLS):
                if self.board[y][x]:
                    self.draw_block(x,y, self.board[y][x])
        for dx, dy in self.current["blocks"]:
            x = self.current['x'] + dx
            y = self.current['y'] + dy
            if y >= 0:
                self.draw_block(x, y, self.current["color"])

        for dx, dy in self.next_shape["blocks"]:
            x = COLS + 1 + dx
            y = 6 + dy
            self.draw_block(x, y, self.next_shape["color"])

    def valid_position(self, x, y, blocks):
        for dx, dy in blocks:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                return False
            if new_y >= 0 and self.board[new_y][new_x]:
                return False
        return True

    def move(self, dx, dy):
        if self.valid_position(self.current['x'] + dx, self.current['y'] + dy, self.current["blocks"]):
            self.current['x'] += dx
            self.current['y'] += dy
            return True
        return False

    def rotate(self):
        if self.current["blocks"] == SHAPES["O"][0]:
            return
        old_blocks = self.current["blocks"]
        rotated = [(-dy, dx) for dx, dy in old_blocks]
        if self.valid_position(self.current['x'], self.current['y'], rotated):
            self.current['blocks'] = rotated

    def drop(self):
        if not self.game_over:
            if not self.move(0, 1):
                self.freeze()
            self.draw()
            self.root.after(DELAY, self.drop)
    def freeze(self):
        pass
    def key_press(self):
        self.draw()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tetris")
    game = Tetris(root)
    root.mainloop()
