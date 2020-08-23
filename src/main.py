import json
from board import Board

def load_data_files() -> dict:
    try:
        fd = open("./data/game-data.json")
        data = dict(json.load(fd))
        fd.close()
    except FileNotFoundError as fnf:
        print(fnf.args)
        exit(1)
    
    return data

def invoke_board() -> None:
    pass
        

    