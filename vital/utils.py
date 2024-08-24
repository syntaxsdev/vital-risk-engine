import toml
import os

def read_toml(file: str):
    if os.path.exists(file):    
        return toml.load(file)
    else:
        raise FileNotFoundError("Could not find file")