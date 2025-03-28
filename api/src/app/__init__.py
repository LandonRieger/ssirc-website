from pathlib import Path


def data_dir():
    return Path(__file__).parent.parent.parent.parent / "data"
