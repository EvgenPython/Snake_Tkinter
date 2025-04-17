from X_O_Tk import *
from snake import *

class Games:
    def __init__(self, root):
        self.win = root
        self.title = "Game"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    gema = SnakeGame(root)
    root.mainloop()