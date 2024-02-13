class Nothing:
    def __init__(self):
        self.__class__.__name__ = "Nothing"
        self.toSee
        self.here

    @classmethod
    def toSee(cls, nothing, toSee, here):
        print(nothing.__name__ + toSee.toSee.__name__ + here.here.__name__)

    @classmethod
    def here(cls):
        return str("h" + "e" + "r" + "e")

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


if __name__ == "main":

    __ = Nothing.toSee.here
    print("suck my ... DADDY")
