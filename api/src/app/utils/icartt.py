from pathlib import Path
import pandas as pd
import logging
import numpy as np
from enum import Enum
from typing import Type
import json


class Mode(Enum):
    Cumulative = "Cumulative"
    Differential = "Differential"


class ICARTT:

    def __init__(self, filename: str | Path):
        self.mode = Mode.Cumulative
        self.offset = 61
        self.filename = filename
        self.bins = []
        self.start = None
        self.nan_value = -99999
        self.instrument = "POPS"
        self.base_header = [
            "time_start",
            "time_end",
            "time_mid",
            "altitude",
            "longitude",
            "latitude",
            "pressure",
            "temperature",
            "potential_temp",
            "concentration",
            "surface_area",
            "volume",
            "effective_radius",
            "extinction",
        ]

        self.moment_fields = [
            "concentration",
            "surface_area",
            "volume",
            "effective_radius",
            "extinction",
        ]

    def get_bins(self):
        with open(self.filename, "r") as f:
            for idx, line in enumerate(f):
                if line[0:14] == "OTHER_COMMENTS":
                    if "bin edges" in line.lower():
                        self.bins = [
                            float(b.strip()) / 1000
                            for b in line.split(":")[2].split(",")
                        ][:-1]

    def get_offset(self):
        with open(self.filename, "r") as f:
            for idx, line in enumerate(f):

                if line.strip() == "R0: QA/QC data":  # b2sap
                    self.offset = idx
                    return

    def start_time(self):
        with open(self.filename, "r") as f:
            for idx, line in enumerate(f):

                if idx == 6:
                    tmp = line.split(",")
                    self.start = pd.Timestamp(f"{tmp[0]}-{tmp[1]}-{tmp[2]}")

    def read_header(self):

        self.get_bins()
        self.get_offset()
        self.start_time()
        header = [h for h in self.base_header]
        header.extend([f"radius_{b :1.3f}" for b in self.bins])

        data = {
            "header": header,
            "mode": self.mode,
            "start_time": self.start,
            "bins": self.bins,
            "offset": self.offset,
        }
        return data

    def read_file(self):
        header = self.read_header()
        offset = header["offset"]
        hsize = 1
        data = pd.read_csv(
            self.filename,
            sep=",",
            skiprows=offset,
            header=hsize,
            names=header["header"],
        )
        data = data.replace(self.nan_value, np.nan)
        json = {"metadata": header}
        ds = []
        colidx = [
            idx for idx, col in enumerate(data.columns) if "radius" == col.split("_")[0]
        ]
        last_alt = -100
        header["latitude"] = float(data.latitude.mean())
        header["longitude"] = float(
            data.longitude.mean()
        )

        for idx in data.index:
            row = data.loc[idx]
            alt = float(row.altitude)

            # only sample ascending
            if alt < last_alt:
                continue

            last_alt = alt
            tmp = {
                "altitude": alt,
                "time": (
                    pd.Timedelta(row.time_start, "s") + header["start_time"]
                ).strftime("%Y-%m-%d %H:%M:%S"),
                "potential_temp": float(row.potential_temp),
            }
            for field in self.moment_fields:
                tmp[field] = float(row[field]) if not np.isnan(row[field]) else None
            #     "pressure": float(row.pressure),
            #     "volume": float(row.volume),
            #     "surface_area": float(row.surface_area),
            #     "effective_radius": float(row.effective_radius),
            #     "No": float(row.concentration),
            #     "extinction": float(row.extinction),
            # }
            if header["mode"] == Mode.Cumulative:
                vals = [float(x) for x in row.iloc[colidx].values]
                tmp["concentration"] = [float(x) if not np.isnan(x) else None for x in np.cumsum(vals[::-1])[::-1]]
            elif header["mode"] == Mode.Differential:
                tmp["concentration"] = [float(x) if not np.isnan(x) else None for x in row.iloc[colidx].values]
            else:
                raise ValueError(f"{header['mode']} mode not supported")
            ds.append(tmp)
        json["data"] = ds
        json["metadata"]["start_time"] = json["metadata"]["start_time"].strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        return json


def generate_metadata(
    basedir: str | Path, campaign: str, Reader: Type[ICARTT] = ICARTT
):

    basedir = Path(basedir)
    meta = []
    for folder in [f.name for f in basedir.glob("*")]:

        directory = basedir / folder
        files = directory.glob("*.ict")

        for file in files:
            reader = Reader(file)
            data = reader.read_file()
            meta.append(
                {
                    "time": data["metadata"]["start_time"],
                    "latitude": data["metadata"]["latitude"],
                    "longitude": data["metadata"]["longitude"],
                    "instrument": reader.instrument,
                    "file": file.name,
                    "folder": campaign,
                    "location": folder,
                }
            )

    with open(basedir.parent / "metadata.json", "w") as fp:
        json.dump(meta, fp, indent=4)

    return meta


if __name__ == "__main__":
    icartt = ICARTT(
        r"C:\Users\RiegerL\Software\ssirc-website\api\src\app\data\B2SAP\Locations\Boulder\NOAA-POPS-B2SAP_GMLBalloon_20230328_R0.ict"
    )
    data = icartt.read_file()
    print(data)
