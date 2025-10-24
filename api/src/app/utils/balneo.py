from pathlib import Path
import pandas as pd
import logging
import numpy as np
from app import data_dir
import json
from app.utils.icartt import ICARTT
from app.utils.b2sap import generate_metadata


CAMPAIGN = "BalneO"

class BalneO(ICARTT):

    def __init__(self, filename: str | Path):
        super().__init__(filename)

        self.base_header = [
            "time_start",
            "time_end",
            "altitude",
            "flow",
            "temperature",
            "pressure",
            "potential_temp",
            "relative_humidity",
            "latitude",
            "longitude",
            "wind_speed",
            "wind_direction"
        ]
        self.moment_fields = []

    def get_offset(self):
        with open(self.filename, "r") as f:
            for idx, line in enumerate(f):

                if "REVISION" in line:  # balneo
                    self.offset = idx
                    return
            
    def get_bins(self):
        bins = []
        with open(self.filename, "r") as f:
            for idx, line in enumerate(f):
                if line[0:3] == "bin" and "d>" in line:
                    bins.append(float(line.split('d>')[1]))
        self.bins = bins

        
def get_data_folder():
    cdir = Path(__file__).parent.parent.parent.parent
    return data_dir() / CAMPAIGN / "Locations"


if __name__ == "__main__":
    balneo = BalneO(r"C:\Users\RiegerL\Software\ssirc-website\api\src\app\data\Balneo\Locations\Bauru\BRAVO-POPC30_SONDE_20220530114836_R0_BAURU-BR.ict")
    data = balneo.read_file()
    print(data)

    generate_metadata(basedir = get_data_folder(), campaign=CAMPAIGN, Reader = BalneO)
