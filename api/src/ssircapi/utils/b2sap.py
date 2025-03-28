from pathlib import Path
import pandas as pd
import logging
import numpy as np


CAMPAIGN = "B2SAP"


def get_data_folder():
    cdir = Path(__file__).parent.parent.parent.parent
    return cdir / "data" / CAMPAIGN / "Locations"


def get_balloon_flight_times(name, base: Path):

    data = []
    # base = get_data_folder()
    hawaii = "Hawaii"

    for folder in [
        "Hawaii",
        "Alaska",
        "La Reunion",
        "Boulder",
        "Antarctica",
        "Lauder",
        "Costa Rica",
    ]:

        directory = base / folder
        files = directory.glob("*.ict")
        for file in files:
            date = file.name.split("_")[2]
            date = pd.Timestamp(f"{date[0:4]}-{date[4:6]}-{date[6:]}").isoformat()
            data.append(
                {
                    "time": date,
                    "file": file.name,
                    "folder": CAMPAIGN,
                    "location": folder,
                    "instrument": file.name.split("-")[1],
                }
            )

    return data


def read_header(filename):

    mode = "Cumulative"
    offset = 61
    with open(filename, "r") as f:
        for idx, line in enumerate(f):

            if idx == 6:
                tmp = line.split(",")
                start = pd.Timestamp(f"{tmp[0]}-{tmp[1]}-{tmp[2]}")

            if line[0:14] == "OTHER_COMMENTS":
                bins = [float(b.strip()) / 1000 for b in line.split(":")[2].split(",")][
                    :-1
                ]

            if line.strip() == "R0: QA/QC data":
                offset = idx

    header = [
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
    header.extend([f"radius_{b :1.3f}" for b in bins])

    data = {
        "header": header,
        "mode": mode,
        "start_time": start,
        "bins": bins,
        "offset": offset,
    }

    return data


def read_file(filename):
    header = read_header(filename)
    offset = header["offset"]
    hsize = 1
    data = pd.read_csv(
        filename, sep=",", skiprows=offset, header=hsize, names=header["header"]
    )

    json = {"metadata": header}
    ds = []
    colidx = [
        idx for idx, col in enumerate(data.columns) if "radius" == col.split("_")[0]
    ]
    last_alt = -100
    for idx in data.index:
        row = data.loc[idx]
        alt = float(row.altitude)

        # only sample ascending
        if alt < last_alt:
            continue

        last_alt = alt
        tmp = {
            "altitude": alt,
            "time": (pd.Timedelta(row.time_start, "s") + header["start_time"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "potential_temp": float(row.potential_temp),
            "pressure": float(row.pressure),
            "volume": float(row.volume),
            "surface_area": float(row.surface_area),
            "effective_radius": float(row.effective_radius),
            "No": float(row.concentration),
            "extinction": float(row.extinction),
        }
        if header["mode"] == "Cumulative":
            vals = [float(x) for x in row.iloc[colidx].values]
            tmp["concentration"] = [float(x) for x in np.cumsum(vals[::-1])[::-1]]
        else:
            raise ValueError(f"{header['mode']} mode not supported")
        ds.append(tmp)
    json["data"] = ds
    json["metadata"]["start_time"] = json["metadata"]["start_time"].strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return json


if __name__ == "__main__":

    data = read_file(
        "/data/B2SAP/Locations/Hawaii/NOAA-POPS-B2SAP_GMLBalloon_20220504_R0.ict"
    )
    data
