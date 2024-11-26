import pytoml
import os


def read_toml(file: str):
    if os.path.exists(file):
        with open(file, "r") as f:
            return pytoml.load(f)
    else:
        raise FileNotFoundError("Could not find file")
