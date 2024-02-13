import math
import random
from os import system as cmd
import platform

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

    def clear_console(self):
        system = platform.system()
        if system == 'Windows':
            cmd('cls')
        elif system == 'Darwin':
            cmd('clear')
        elif system == 'Linux':
            cmd('clear')
        else:
            print('\n' * 20)

    def print_board(self):
        print("2048: Please Full Screen Your Console")
        for row in self.board:
            for item in row:
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
            for _ in range(min(num_fours, len(zeros))):
                x, y = zeros.pop()
                self.board[x][y] = 4

        if chance_of_four == 4:
            num_twos = 1

        for _ in range(min(num_twos, len(zeros))):
            x, y = zeros.pop()
            self.board[x][y] = 2

    def update_game(self):
        if not any(0 in sublist for sublist in self.board):
            print("GAME OVER")
            CAN_RUN = False
            return CAN_RUN

        self.clear_console()
        print()
        self.print_board()
        command = self.get_direction()

        if  command in ["W", "UP", "U"]:
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

        CAN_RUN = True
        return CAN_RUN

class AI(Game):
    def __init__(self, id, game):

        self.id = id

        self.game = game
        self.board = game.board
        self.grid_size = len(self.board)

        self.high_score = 0
        self.score = 0

        self.inputs = self.board
        mean = sum([val for sublst in self.board for val in sublst])//(len(self.board)*len(self.board[0]))
        deviations = [mean - dp for sublst in self.board for dp in sublst]
        pos_devs = [dev for dev in deviations if dev > mean]
        neg_devs = [dev for dev in deviations if dev < mean]

        sqrd = [dev*dev for dev in deviations]
        summed = sum(sqrd)
        variance = summed / ((len(self.board) * len(self.board[0])) - 1)

        stddev = math.sqrt(variance)
        self.weights = [[random.gauss(mean, stddev) for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.biases = [[random.randint(-1, 1) for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for output in random.sample([0, -1, 1, -0.5, 0.5] , len([0, -1, 1, -0.5, 0.5])):
            self.output = output
            self._update_game(self.output)

        #EXPERIMENTAL
        keys = {"keys":["action","state","fitness"]}
        values = [0 for key in keys["keys"]] ##TODO

        self.memory = {}
        for idx, key in enumerate(keys["keys"]):
            self.memory[key] = values[idx]

        self.memoryies = [self.memory]

        self.sigmoid = lambda x: 1 / (1 + math.exp(-x))
        self.sigmoid_deriv = lambda x: self.sigmoid(x) * (1 - self.sigmoid(x))

        self.relu = lambda x: max(0.0, x)
        self.relu_deriv = lambda x: 1 if x > 0 else 0

        self.tanh = lambda x: math.tanh(x)
        self.tanh_deriv = lambda x: 1 - math.tanh(x)**2

        self.swish = lambda x: x * 1/(1+math.exp(-x))
        self.swish_deriv = lambda x: (1/(1+math.exp(-x))) + x * 1/(1+math.exp(-x)) * (1-1/(1+math.exp(-x)))

        self.softplus = lambda x: math.log(math.exp(x) + 1)
        self.softplus_deriv = lambda x: self.sigmoid(x)

        self.max_tanh = lambda x: max(0.0, self.tanh(x))
        self.max_tanh_deriv = lambda x: 1 if x > 0 else math.tanh(x)

    def __str__(self):
        return f"AI{self.id}"

    def matmul(self):
        res = 0
        for row in self.inputs:
            for input in row:
                for row in (self.weights):
                    for idx, weight in enumerate(self.weights):
                        res += sum((input*weight) + self.biases[idx])
        return res

    def forward(self):
        try:
            output = self.tanh(self.matmul())
        except ValueError:
            output = 0

        return output

    def _update_game(self, output):
        if not any(0 in sublst for sublst in self.board):
            total_score = self.summed_board(self.board)

            prev_high_score = self.high_score
            if total_score > self.high_score:
                self.high_score = total_score
                print(f"New HighScore For Model:{self.id}: Prev_HighScore Was: {prev_high_score} New HighScore! IS :{self.high_score}\n")
                self.board = [[0 for _ in range(len(self.board))] for _ in range(len(self.board))]
                for _ in range(random.randint(1, 3)):
                    self.add_ran_tiles()

                CAN_RUN = True
                return CAN_RUN

        self.clear_console()
        print(f"Model: {self.id}, action: {output}: Score:{self.score}: HighScore: {self.high_score}\n")

        if output == 1:
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

        if output == -1:
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

        if output == 0.5:
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

        if output == -0.5:
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

        if round(output) == 0:
            self.output = 0

        self.backprop(output)

        CAN_RUN = True
        return CAN_RUN

    def calc_fitness(self):
        if not self.output in [0, -1, 1, -0.5, 0.5]:
            return -math.inf

        return self.score - self.high_score

    def summed_board(self, board):
        total_sum = 0
        for item in board:
            if isinstance(item, list):
                total_sum += self.summed_board(item)
            else:
                total_sum += item

        return total_sum

    def loss(self):
        y_pred = self.summed_board(self.board)
        y_true = self.high_score

        return (y_true - y_pred) * (y_true - y_pred)

    def backprop(self, output):
        loss = self.loss()
        od = 1-(math.tanh(output)**2)

        for vec in self.weights:
            for weight in vec:
                weight -= loss * output * od

        for vec in self.biases:
            for bias in vec:
                bias -= loss * output * od

if __name__ == '__main__':
    Game().clear_console()

    while True:
        print()
        controller = input("Enter: PLAYER or AI:\n ")
        controller = controller.upper()

        if controller in ["PLAYER", "AI"]:
            break
        else:
             print(f"{controller} is not allowed")

    while controller == "AI":
        print()
        num_ais = input("Enter Number of Ais to Run:\n ")
        try:
            num_ais = int(num_ais)
            if num_ais <= 0:
                Game().clear_console()
                print("Must be at least 1 Ai")
            else:
                print()
                break
        except ValueError:
            Game().clear_console()
            print("Must be a number Not of letters: ")

    while controller in ["PLAYER", "AI"]:
        print()
        grid_size = input("Enter Grid Size >= 4: ¡WARNING! large grid_sizes NOT ADVISED!}\n")
        try:
            grid_size = int(grid_size)
            if grid_size <= 3:
                print("grid_size must be at least 4")
            else:
                print()
                break
        except ValueError:
            print("Grid Size must be an integer")

    ###Objects (women)
    game = Game(grid_size)

    CAN_RUN = True
    while (controller == "PLAYER") and CAN_RUN:
        CAN_RUN = game.update_game()

    AIs = []
    CAN_RUN = True
    while (controller == "AI") and CAN_RUN:
        if len(AIs) == 0:
            for n in range(num_ais):
                AIs.append(AI(n+1, game))
        for ai in AIs:
            try:
                ai.output = ai.forward()
                CAN_RUN = ai._update_game(ai.output)
                if not CAN_RUN:
                    break
            except Exception as e:
                print(f"ERROR: {e}")
                CAN_RUN = False
                break
