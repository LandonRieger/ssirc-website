from pathlib import Path
import pandas as pd
import logging
import numpy as np
from app import data_dir
import json
from app.utils.icartt import ICARTT, Mode, generate_metadata


CAMPAIGN = "B2SAP"


class B2SAP(ICARTT):
    def __init__(self):
        self.mode = Mode.Cumulative
        self.offset = 61

def get_data_folder():
    cdir = Path(__file__).parent.parent.parent.parent
    return data_dir() / CAMPAIGN / "Locations"


def get_balloon_flight_times(name, base: Path):

    with open(base.parent / 'metadata.json', 'r') as fp:
        data = json.load(fp)
    
    return data


if __name__ == "__main__":

    generate_metadata(basedir = get_data_folder(), campaign=CAMPAIGN, Reader = B2SAP)
