from os import system as cmd
from platform import system

if __name__ == "main":
    os = system()

    if os == 'Windows':
        cmd("python -m venv venv")
        cmd("venv\\Scripts\activate && pip install -r requirements.txt")
    if os == 'Darwin':
        cmd("python3 -m venv venv")
        cmd("source venv/bin/activate && pip3 install -r requirements.txt")
    if os == 'Linux':
        pass
    else:
        raise Exception("Create a Virtual Env and manually install python libraries")
