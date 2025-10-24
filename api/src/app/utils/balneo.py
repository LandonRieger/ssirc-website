from pathlib import Path
from app import data_dir
import json
from app.utils.icartt import ICARTT, Mode
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
            "wind_direction",
        ]
        self.moment_fields = ["temperature", "pressure"]
        self.instrument = "POPC"
        self.mode = Mode.Differential

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
                    bins.append(float(line.split("d>")[1]))
        self.bins = bins


def get_data_folder():
    cdir = Path(__file__).parent.parent.parent.parent
    return data_dir() / CAMPAIGN / "Locations"


def get_balloon_flight_times(name, base: Path):

    with open(base.parent / "metadata.json", "r") as fp:
        data = json.load(fp)

    return data


def read_file(filename: str | Path):
    return BalneO(filename).read_file()


if __name__ == "__main__":
    cdir = Path(__file__).parent.parent / 'data' / CAMPAIGN / "Locations"
    balneo = BalneO(
        cdir / "Bauru" / "BRAVO-POPC30_SONDE_20220820034144_R0_BAURU-BR.ict"
    )
    data = balneo.read_file()
    print(data)

    generate_metadata(basedir=get_data_folder(), campaign=CAMPAIGN, Reader=BalneO)
