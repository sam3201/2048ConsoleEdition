###Import ¡UnderScore! Necessaties
globalsUNDERSCOREdict = {}

with open("2048.py", "r") as f:
    exec(f.read(), globalsUNDERSCOREdict)

Game = globalsUNDERSCOREdict["Game"]
AI = globalsUNDERSCOREdict["AI"]
from os import system as cmd

try:
    import pygame
except Exception as e:
    print(e)


if __name__ == "__main__":
    _ = None
    game = Game(grid_size=4)
    game.print_board()
