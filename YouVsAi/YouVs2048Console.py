###Import ¡UnderScore! Necessaties
from os import name, system as cmd #to call clear console

#Objects from main file
globalsUNDERSCORE_NecessatiesDict = {}
with open("2048.py", "r") as f:
    exec(f.read(), globalsUNDERSCORE_NecessatiesDict)

#Game and AI Objects
Game = globalsUNDERSCORE_NecessatiesDict["Game"]
AI = globalsUNDERSCORE_NecessatiesDict["AI"]

if __name__ == "__main__":
    _ = None

    #game = Game(4)
    #ai = AI(1, game)
    """

    try:
        ai.output = ai.forward()
        CAN_RUN = ai._update_game(ai.output)
    except Exception as e:
        print(f"ERROR: {e}")
        CAN_RUN = False

    """
