import tkinter as tk
import random

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

DIRECTIONS = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0),
}
SPEEDS = {
    "Легкий": 200,
    "Середній": 150,
    "Важкий": 100,
}


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.menu_frame = tk.Frame(root)
        self.level_var = tk.StringVar(value="Середній")
        self.score = 0
        self.running = False
        self.paused = False
        self.after_id = None
        self.create_menu()

    def create_menu(self):
        self.clear_canvas()
        tk.Label(self.menu_frame, text="Snake", font=("Arial", 22)).pack(pady=10)
        tk.Button(self.menu_frame, text="Start", font=("Arial", 14), command=self.start_game).pack(pady=5)
        tk.OptionMenu(self.menu_frame, self.level_var, *SPEEDS.keys()).pack(pady=5)
        tk.Button(self.menu_frame, text="Exit", font=("Arial", 14), command=self.root.destroy).pack(pady=5)
        self.menu_frame.pack()

    def clear_canvas(self):
        pass

    def start_game(self):
        self.menu_frame.pack_forget()
        self.running = True
        self.paused = False
        self.score = 0
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = "Right"
        self.food = None
        self.canvas.delete("all")
        self.draw_border()
        self.draw_snake()
        self.spawn_food()
        self.draw_score()
        self.root.bind("<Key>", self.change_direction)
        self.root.bind("<Escape>", self.toggle_pause)
        self.update()

    def draw_border(self):
        self.canvas.create_rectangle(10, 10, WIDTH - 5, HEIGHT - 5, outline="white", width=2)

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.draw_cell(x, y, "green", tag="snake")

    def spawn_food(self):
        self.canvas.delete("food")
        while True:
            x = random.randint(1, (WIDTH // CELL_SIZE) - 2)
            y = random.randint(1, (HEIGHT // CELL_SIZE) - 2)
            if (x,y) not in self.snake:
                self.food = x, y
                self.draw_cell(x,y, "red",  tag="food")
                break

    def draw_score(self):
        self.canvas.delete("score")
        self.canvas.create_text(50, 50, text=f"Score: {self.score}", fill="white", font=("Arial", 14), tag="score")

    def change_direction(self, event):
        new_direction = event.keysym
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction in DIRECTIONS and new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def toggle_pause(self, event=None):
        if not self.running:
            return
        self.paused = not self.paused
        if self.paused:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="Pause", fill="yellow", font=("Arial", 20), tag="pause")
        else:
            self.canvas.delete("pause")
            self.update()

    def update(self):
        if not self.running or self.paused:
            return
        self.move_snake()
        if self.running:
            self.draw_snake()
            self.draw_score()
            speed = SPEEDS[self.level_var.get()]
            self.after_id = self.root.after(speed, self.update)
    def move_snake(self):
        dx, dy =  DIRECTIONS[self.direction]
        head_x, head_y = self.snake[0]
        new_head = (head_x + dx, head_y+dy)
        # укуси сама себя
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.spawn_food()
        else:
            self.snake.pop()

    def draw_cell(self, x, y, color, tag=""):
        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE
        x2 = x1 * CELL_SIZE
        y2 = y1 * CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tag=tag)


if __name__ == "__main__":
    root = tk.Tk()
    gema = SnakeGame(root)
    root.mainloop()
