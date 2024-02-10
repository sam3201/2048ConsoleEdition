import random
import os
import sys
import platform

class AI:
    def __init__(self, board):
        self.board = board

        self.inputs = []
        self.weights = []
        self.biases = []

        #EXPERIMENTAL
        self.memory = []

    def matmul(self):
        pass

    def forward(self):
        pass

    def backprop(self):
        pass

class Cell:
    def __init__(self, val, grid_size):
        self.val = val
        self.grid_size = grid_size

    def val_size(self, val):
        if isinstance(val, int):
            return len(str(val))
        elif isinstance(val, str):
            return len(val)
        else:
            print(f"Val: {val} is of type: {type(val)}")
            return quit()

    def print_cell(self):
        str_size = self.val_size(self.val)
        if str_size % 2 == 0:
            middle = str_size // 2
        else:
            middle = (str_size // 2) + 1

        spaces = (self.grid_size - str_size) // 2
        left_spaces = " " * spaces
        right_spaces = " " * ((self.grid_size - str_size - spaces) + 1)

        print("=" * (self.grid_size + 4))
        for _ in range(spaces):
            print("=" + " " * (self.grid_size + 2) + "=")
        print("=" + " " + left_spaces + str(self.val) + right_spaces + "=")
        for _ in range(spaces):
            print("=" + " " * (self.grid_size + 2) + "=")
        print("=" * (self.grid_size + 4))

class Game:
    def __init__(self, grid_size=4, ai=None):

        self.grid_size = grid_size

        self.board = [[0 if row == random.randint(1,9) else 4 if row == random.randint(1,100) else 0 for row in range(self.grid_size) ] for _ in range(self.grid_size)]

        if not 0 in self.board:
            for _ in range(random.randint(1, 3)):
                self.board[random.randint(0, self.grid_size - 1)][random.randint(0, self.grid_size - 1)] = 2

        if random.randint(1,5) == 5:
            if not 4 in self.board:
                for _ in range(random.randint(1,4)):
                    ranX = random.randint(0, self.grid_size - 1)
                    ranY = random.randint(0, self.grid_size - 1)
                    if not self.board[ranX][ranY] == 2:
                        self.board[ranX][ranY] = 4

        self.clear_console()
        self.print_board()

    def clear_console(self):
        system = platform.system()
        if system == 'Windows':
            os.system('cls')
        elif system == 'Darwin':
            os.system('clear')
        elif system == 'Linux':
            os.system('clear')
        else:
            print('\n' * 20)

    def print_board(self):
        print("2048: Please Full Screen Your Console")
        for row in self.board:
            for item in row:
                """"
                cell = Cell(item, self.grid_size)
                cell.print_cell()
                """
                print(str(item) + " ", end=" ")
            print(" ")
        print("\n")

    def get_direction(self):
        command = input('Please Enter Directional Command: (W A S D) (UP, DOWN, LEFT, RIGHT) (U, D, L, R) (Q, QUIT):\n')
        command = command.upper()

        if not command in ["W", "A", "S", "D", "UP", "DOWN", "LEFT", "RIGHT", "U", "D", "L", "R", "Q"]:
            print(f"{command} is Not a valid command")
            return self.get_direction()
        else:
            return command

    def add_ran_tiles(self, num_twos=random.randint(1,2), num_fours=1):
        zeros = [(x, y) for x in range(self.grid_size) for y in range(self.grid_size) if self.board[x][y] == 0]
        random.shuffle(zeros)

        chance_of_four = random.randint(1, 4)
        if chance_of_four == 4:
            for _ in range(num_fours):
                x, y = zeros.pop()
                self.board[x][y] = 4

        if chance_of_four == 4:
            num_twos = 1

        for _ in range(num_twos):
            x, y = zeros.pop()
            self.board[x][y] = 4

    def update_game(self):
        if not any(0 in sublist for sublist in self.board):
            i = 0
            while i < random.randint(1, 2048):
                print("GAME OVER")
                CAN_RUN = False
                return CAN_RUN

        command = self.get_direction()

        if command in ["W", "UP", "U"]:
            for col in range(self.grid_size):
                for row in range(1, self.grid_size):
                    curr = self.board[row][col]
                    if curr == 0:
                        continue
                    row_above = row - 1
                    while row_above >= 0 and self.board[row_above][col] == 0:
                        self.board[row_above][col] = curr
                        self.board[row][col] = 0
                        row -= 1
                        row_above -= 1
                    if row_above >= 0 and self.board[row_above][col] == curr:
                        self.board[row_above][col] += curr
                        self.board[row][col] = 0

            self.add_ran_tiles()

        if command in ["S", "DOWN", "D"]:
            for col in range(self.grid_size):
                for row in range(self.grid_size - 2, -1, -1):
                    curr = self.board[row][col]
                    if curr == 0:
                        continue
                    row_below = row + 1
                    while row_below < self.grid_size and self.board[row_below][col] == 0:
                        self.board[row_below][col] = curr
                        self.board[row][col] = 0
                        row += 1
                        row_below += 1
                    if row_below < self.grid_size and self.board[row_below][col] == curr:
                        self.board[row_below][col] += curr
                        self.board[row][col] = 0

            self.add_ran_tiles()

        if command in ["A", "LEFT", "L"]:
            for row in range(self.grid_size):
                for col in range(1, self.grid_size):
                    curr = self.board[row][col]
                    if curr == 0:
                        continue
                    col_left = col - 1
                    while col_left >= 0 and self.board[row][col_left] == 0:
                        self.board[row][col_left] = curr
                        self.board[row][col] = 0
                        col -= 1
                        col_left -= 1
                    if col_left >= 0 and self.board[row][col_left] == curr:
                        self.board[row][col_left] += curr
                        self.board[row][col] = 0

            self.add_ran_tiles()

        if command in ["D", "RIGHT", "R"]:
            for row in range(self.grid_size):
                for col in range(self.grid_size - 2, -1, -1):
                    curr = self.board[row][col]
                    if curr == 0:
                        continue
                    col_right = col + 1
                    while col_right < self.grid_size and self.board[row][col_right] == 0:
                        self.board[row][col_right] = curr
                        self.board[row][col] = 0
                        col += 1
                        col_right += 1
                    if col_right < self.grid_size and self.board[row][col_right] == curr:
                        self.board[row][col_right] += curr
                        self.board[row][col] = 0

                self.add_ran_tiles()

        if command in ["Q", "QUIT"]:
            CAN_RUN = False
            return CAN_RUN

        print()
        self.print_board()

        CAN_RUN = True
        return CAN_RUN


if __name__ == '__main__':
    Game().clear_console()

    #Get grid_size from user input
    while True:
        grid_size = input("Enter Grid Size >= 4: ")
        try:
            grid_size = int(grid_size)
            if grid_size <= 3:
                print("grid_size must be at least 4")
            else:
                break
        except ValueError:
            print("Grid Size must be an integer")

    ###Objects (women)
    game = Game(grid_size)
    ai = AI(game.board)

    CAN_RUN = True
    while CAN_RUN:
        CAN_RUN = game.update_game()
