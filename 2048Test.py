class Nothing:
    def __init__(self):
        self.__class__.__name__ = "Nothing"
        self.toSee = "to see"
        self.here = "here"

    @classmethod
    def toSee(cls, nothing, toSee, here):
        print(nothing.__name__ + toSee.toSee.__name__ + here.here.__name__)

    @classmethod
    def here(cls):
        return str("h" + "e" + "r" + "e")

if __name__ == "main":

    __ = Nothing.toSee.here
    print("suck my ... DADDY")
