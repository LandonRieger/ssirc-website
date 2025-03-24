from pathlib import Path
import pandas as pd
import logging


def get_balloon_flight_times(name):

    data = []

    if name.lower() == "wopc":
        cdir = Path(__file__).parent.parent.parent
        base = cdir / 'data' / "Locations"
        laramie = r"Laramie/SizeDist_Stratosphere"
        lauder = r"Lauder/SizeDist_Stratosphere"
        boulder = r"Boulder/SizeDist_Stratosphere"

        for folder in [laramie, lauder, boulder]:

            directory = base / folder
            files = directory.glob("*.szd")
            for file in files:
                date = file.name.split("_")[0]
                date = pd.Timestamp(f"{date[0:4]}-{date[4:6]}-{date[6:]}").isoformat()
                data.append(
                    {
                        'time': date,
                        'file': file.name,
                        'folder': Path(folder).parent,
                        'instrument': file.name.split('_')[2]
                    }
                )

    return data


def get_corresponding_nd_file(filename: str, folder: str):

    cdir = Path(__file__).parent.parent.parent
    base = cdir / 'data' / "Locations"
    nd_folder = base / folder / "Nr_Full_Profile" / "Average_0.5_km"

    ymd = filename.split('_')[0]
    for file in (base / nd_folder).glob("*.500m"):
        if ymd == file.name.split("_")[0]:
            logging.error(f'returning file {file}')
            return {"file": file.name, "folder": folder}

    return {"file": None, "folder": None}


def read_wyoming_header(filename):
    reading_header = False
    mode = None
    with open(filename, 'r') as f:
        for line in f:

            if mode is None:
                mode = line.split()[0]

            elif len(line) > 10 and 'Tim' in line[0:10]:
                reading_header = True
                header1 = line.split()
            elif reading_header:
                header2 = line.split()
                reading_header = False

            elif len(line) > 15 and 'Balloon release' == line[0:15]:
                split = line.split()[2:]
                # split.remove(',')
                start = pd.Timestamp(f'{split[4][0:4]}-{split[3]}-{split[2]} {split[0]}:00')
                try:
                    latitude = float(split[7])
                except:
                    split.remove(',')
                    latitude = float(split[7])
                north = split[8][0] == 'N'
                longitude = float(split[9])
                west = split[10][0] == 'W'
                if not north:
                    latitude *= -1
                if west:
                    longitude *= -1
    if mode == 'Cumulative':
        header = [(f'{a} {b}') for a, b in zip(header1, header2)]
    else:
        header = header1

    if mode == 'Cumulative':
        header[0:7] = ['time', 'potential_temp', 'altitude', 'pressure', 'temperature', 'relative_humidity', 'ozone']
    elif mode == 'Unimodal/bimodal':
        header = ['time', 'fit', 'potential_temp', 'altitude', 'pressure', 'temperature', 'surface_area', 'volume', 'error', 'No1', 'Ro1', 'So1', 'No2', 'Ro2', 'So2']

    data = {'header': header, 'mode': mode, 'start_time': start, 'latitude': float(latitude), 'longitude': float(longitude)}
    if mode == 'Cumulative':
        data['bins'] = [float(h.split('>')[1].split('cm')[0]) for h in header[7:] if h[0] == 'N']
        dups = [False, ] + [a == b for a, b in zip(data['bins'][0:], data['bins'][1:])]
        if any(dups):
            for idx, dup in enumerate(dups):
                if dup:
                    data['bins'][idx - 1] -= 0.01
        header[7:] = [f'radius_{b}' for b in data['bins']]
        if len(header1) > len(header):
            header.extend(['latitude', 'longitude'])
        data['header'] = header

    return data


def read_wyoming_file(filename):
    header = read_wyoming_header(filename)
    offset = 101 if header['mode'] == 'Cumulative' else 104
    hsize = 1 if header['mode'] == 'Cumulative' else 0
    data = pd.read_csv(filename, sep='\s+', skiprows=offset, header=hsize, names=header['header'])

    json = {'metadata': header}
    ds = []
    colidx = [idx for idx, col in enumerate(data.columns) if 'radius' == col.split('_')[0]]
    for idx in data.index:
        row = data.loc[idx]
        tmp = {'altitude': float(row.altitude),
               'time': (pd.Timedelta(row.time, 'm') + header['start_time']).strftime('%Y-%m-%d %H:%M:%S'),
               'potential_temp': float(row.potential_temp),
               'pressure': float(row.pressure)}
        if header['mode'] == 'Cumulative':
            tmp['concentration'] = [float(x) for x in row.iloc[colidx].values]
        else:
            for key in ['No1', 'Ro1', 'So1', 'No2', 'Ro2', 'So2']:
                tmp[key] = float(row[key])
        ds.append(tmp)
    json['data'] = ds
    json['metadata']['start_time'] = json['metadata']['start_time'].strftime('%Y-%m-%d %H:%M:%S')

    return json


if __name__ == '__main__':
    cdir = Path(__file__).parent.parent.parent
    base = cdir / 'data' / "Locations"
    laramie_wopc = r"Locations/Boulder/Nr_Full_Profile/Average_0.5_km"
    # laramie_wopc = r"Locations/Boulder/SizeDist_Stratosphere"
    # filename = base / laramie_wopc / '19900524_WY_WOPC_13m.500m'
    # filename = base / laramie_wopc / '19891117_WY_WOPC_8p.500m_11.00km_Srs_ce.szd'
    # filename = base / laramie_wopc / '20240312_CO_LOPC_208.500m_11.50km_Srs_ce.szd'
    filename = base / laramie_wopc / '20200913_WY_LOPC_206.500m'
    # get_corresponding_nd_file('20240312_CO_LOPC_208.500m_11.50km_Srs_ce.szd', 'Boulder')
    get_balloon_flight_times('wopc')
    read_wyoming_file(filename)
