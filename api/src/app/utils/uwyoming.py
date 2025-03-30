from pathlib import Path
import pandas as pd
import logging
from app import data_dir
import json


CAMPAIGN = "UWyoming"


def get_data_folder():
    return data_dir() / CAMPAIGN / "Locations"


def get_balloon_flight_times(name, base: Path):

    with open(base.parent / 'metadata.json', 'r') as fp:
        data = json.load(fp)
    
    return data


def get_corresponding_nd_file(filename: str, folder: str, base: Path):

    nd_folder = base / folder / "Nr_Full_Profile"
    nd_folder = list(nd_folder.glob('*'))[0]

    # alt_res = nd_folder.name.split('.')[-1]

    ymd = filename.split("_")[0]
    for file in (base / nd_folder).glob("*.*m"):
        if ymd == file.name.split("_")[0]:
            return {"file": file.name, "location": folder, "folder": CAMPAIGN}

    return {"file": None, "folder": None}


def read_header(filename):
    reading_header = False
    mode = None
    offset = 101
    with open(filename, "r") as f:
        for idx, line in enumerate(f):

            if mode is None:
                mode = line.split()[0]

            elif len(line) > 10 and "Tim" in line[0:10]:
                offset = idx
                reading_header = True
                header1 = line.split()
            elif reading_header:
                header2 = line.split()
                reading_header = False

            elif len(line) > 15 and "Balloon release" == line[0:15]:
                split = line.split()[2:]
                # split.remove(',')
                start = pd.Timestamp(
                    f"{split[4][0:4]}-{split[3]}-{split[2]} {split[0]}:00"
                )
                try:
                    latitude = float(split[7])
                except:
                    split.remove(",")
                    latitude = float(split[7])
                north = split[8][0] == "N"
                longitude = float(split[9])
                west = split[10][0] == "W"
                if not north:
                    latitude *= -1
                if west:
                    longitude *= -1
    if mode == "Cumulative":
        header = [(f"{a} {b}") for a, b in zip(header1, header2)]
    else:
        header = header1

    if mode == "Cumulative":
        header[0:7] = [
            "time",
            "potential_temp",
            "altitude",
            "pressure",
            "temperature",
            "relative_humidity",
            "ozone",
        ]
    elif mode == "Unimodal/bimodal":
        header = [
            "time",
            "fit",
            "potential_temp",
            "altitude",
            "pressure",
            "temperature",
            "surface_area",
            "volume",
            "error",
            "No1",
            "Ro1",
            "So1",
            "No2",
            "Ro2",
            "So2",
        ]

    data = {
        "header": header,
        "mode": mode,
        "start_time": start,
        "latitude": float(latitude),
        "longitude": float(longitude),
        "offset": offset
    }
    if mode == "Cumulative":
        data["bins"] = [
            float(h.split(">")[1].split("cm")[0]) for h in header[7:] if h[0] == "N"
        ]
        dups = [
            False,
        ] + [a == b for a, b in zip(data["bins"][0:], data["bins"][1:])]
        if any(dups):
            for idx, dup in enumerate(dups):
                if dup:
                    data["bins"][idx - 1] -= 0.01
        header[7:] = [f"radius_{b}" for b in data["bins"]]
        if len(header1) > len(header):
            header.extend(["latitude", "longitude"])
        data["header"] = header

    return data


def read_file(filename):
    header = read_header(filename)
    offset = header["offset"]
    hsize = 2 if header["mode"] == "Cumulative" else 1
    data = pd.read_csv(
        filename, sep="\s+", skiprows=offset, header=hsize, names=header["header"]
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
            "time": (pd.Timedelta(row.time, "m") + header["start_time"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "potential_temp": float(row.potential_temp),
            "pressure": float(row.pressure),
        }
        if header["mode"] == "Cumulative":
            tmp["concentration"] = [float(x) for x in row.iloc[colidx].values]
        else:
            for key in ["No1", "Ro1", "So1", "No2", "Ro2", "So2"]:
                tmp[key] = float(row[key])
        ds.append(tmp)
    json["data"] = ds
    json["metadata"]["start_time"] = json["metadata"]["start_time"].strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return json


def generate_metadata():

    basedir = get_data_folder()
    meta = []
    for folder in [f.name for f in basedir.glob("*")]:

        directory = basedir / folder / "SizeDist_Stratosphere"
        files = directory.glob("*.szd")

        for file in files:
            data = read_file(file.as_posix())
            meta.append(
                {
                    'time': data['metadata']['start_time'],
                    'latitude': data['metadata']['latitude'],
                    'longitude': data['metadata']['longitude'],
                    'instrument': file.name.split('_')[2],
                    "file": file.name,
                    "folder": CAMPAIGN,
                    "location": folder,
                }
            )

    with open(basedir.parent / 'metadata.json', 'w') as fp:
        json.dump(meta, fp, indent=4)

    return meta


if __name__ == "__main__":

    generate_metadata()
