from os import system as cmd
from platform import system

if __name__ == "main":
    sys = system()

    def clear():
        if sys == 'Windows':
            cmd('cls')
        elif sys == 'Darwin':
            cmd('clear')
        elif sys == 'Linux':
            cmd('clear')
        else:
            print('\n' * 20)

    if sys == 'Windows':
        cmd("python -m venv venv")
        cmd("venv\\Scripts\activate && pip install -r requirements.txt")
    if sys == 'Darwin':
        cmd("python3 -m venv venv")
        cmd("source venv/bin/activate && pip3 install -r requirements.txt")
    if sys == 'Linux':
        pass
    else:
        raise Exception("Create a Virtual Env and manually install python libraries")
