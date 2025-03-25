import os
# import bibtexparser
import pandas as pd
from pathlib import Path
import json
import numpy as np
import datetime
import re


def format_authors(entry):
    authors = entry['author'].split(' and ')
    if authors[0].count(',') > 1:
        nauth = [a.strip() for a in authors[0].split(',')]
        if ' ' in nauth[0]:
            authors = ['. '.join([b[0] for b in auth.split(' ')[:-1]]) + f'. {auth.split(" ")[-1]}' for auth in nauth]
        else:
            if ' and ' in entry['author']:
                authors = [f'{nauth[1].strip()} {nauth[0]}', ] + nauth[2:] + [authors[1]]
            else:
                authors = [f'{nauth[1].strip()} {nauth[0]}', ] + nauth[2:]

        if '' in authors:
            authors.remove('')
        if 'others' in authors:
            authors.remove('others')
    else:
        if 'others' in authors:
            authors.remove('others')
        try:
            authors = [f'{a.split(",")[1].strip()} {a.split(",")[0].strip()}' for a in authors]
        except:
            pass
        authors = ['. '.join([b[0] for b in auth.split(' ')[:-1]]) + f'. {auth.split(" ")[-1]}' for auth in authors]
    return authors


def generate_publication_html(bib_file, target_year: int = None):

    with open(bib_file, encoding='utf-8') as bib:
        bib_entries = bibtexparser.load(bib)

    if target_year:
        html_file = os.path.join(os.path.dirname(__file__), 'templates', 'references', f'references_{target_year}.html')
    else:
        html_file = os.path.join(os.path.dirname(__file__), 'templates', 'references', 'references.html')

    html = "<div class='list-group mb-3'>\n"
    for entry in bib_entries.entries:
        try:
            year = entry['year']
        except:
            year = ''

        if target_year is not None:
            if int(year) != target_year:
                continue

        authors = format_authors(entry)
        title = entry['title']

        try:
            doi = entry['doi']
        except:
            try:
                doi = entry['DOI']
            except:
                doi = ""

        try:
            volume = entry['volume']
        except:
            volume = ''

        try:
            pages = entry['pages'].replace('--', '-')
        except:
            pages = ''

        try:
            journal = entry['journal']
        except:
            journal = entry['booktitle']

        author_str = ''
        for aidx, author in enumerate(authors):
            if aidx >= 5:
                author_str += f'et. al., '
                break
            author_str += f'{author}, '

        author_str = author_str[:-2]  # strip the trailing ", "
        if volume == '':
            footer = f'<small>{journal}, {pages}</small>'
        else:
            footer = f'<small>{journal}, {volume}, {pages}</small>'

        # html_div = f"""
        # <a href="http://doi.org/{doi}" class="list-group-item">
        # <div class="d-flex w-100 justify-content-between">
        # <h5 class="mb-0">{title}</h5>
        # <small>{year}</small>
        # </div>
        # <p class="mb-0">
        # {author_str}
        # </p>
        # {footer}
        # </a>
        # """
        html_div = f"""
        <div class="list-group-item">
        <a class="mb-0 paper-title" href="http://doi.org/{doi}">{title}</a>
        <p class="mb-0">
        {author_str}
        </p>
        {footer}
        </div>
        """
        html += html_div

    html += f'</div>'

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)


def format_ssirc_bib(bib_file):

    with open(bib_file, 'r', encoding='utf-8') as file:
        data = file.readlines()

    for lidx, line in enumerate(data):
        if (('@article' in line) or ('@inbook' in line) or ('@inproceedings' in line)) and lidx > 2:
            data[lidx-2] += '}\n'

    with open(os.path.join(os.path.dirname(bib_file), 'new_bibfile.bib'), 'w', encoding='utf-8') as newfile:
        newfile.writelines(data)


def convert_balloon_table(filename):

    data = pd.read_excel(filename, skiprows=2).fillna("")
    data = data.rename(columns={
        "max altitutude (km)": "Altitude Range [km]",
        "campaign base (-)lat, (-)lon": "Campaign Base",
        "Additional measured parameters (excluding temp. etc) aside from aerosol concentration": "Additional Parameters",
        "scientific focus (free: e.g. event, long term record, UTLS, volcanic plume, wildfires, ATAL, polar vortex)": "Scientific Focus",
        "link to data (if no link available: contact PI)": "Link to Data",
        "diameter range lower end (µm)": "Size Range start",
        "size range upper end (µm)": "Size Range end",
        "instrument name": "Instrument",
        "number of flights": "Number of Flights",
        "email of PI": "PI Contact"
    })

    rows = []
    for idx, row in data.iterrows():
        tmp = {key: val for key, val in row.items()}

        if tmp["Number of Flights"] == "":
            continue

        tmp['comments'] = "" if type(tmp['comments']) is float else tmp['comments']

        for key in ["Size Range start", "Size Range end"]:
            if type(tmp[key]) is str:
                tmp[key] = tmp[key].strip().strip('-').strip('>')

        try:
            lat, lon = tmp['Campaign Base'].split('[')[1].split(']')[0].split(',')
            tmp['Campaign Base'] = tmp['Campaign Base'].split('[')[0].strip()
            lat = lat.strip()
            lon = lon.strip()
            try:
                lat = float(lat.split(' ')[0]) * (-1 if lat.split(' ')[1] == "S" else 1)
                lon = float(lon.split(' ')[0]) * (-1 if lon.split(' ')[1] == "W" else 1)
            except:
                lat = float(lat.split(' ')[0])
                lon = float(lon.split(' ')[0])
        except:
            lat = None
            lon = None

        tmp["Latitude"] = lat
        tmp["Longitude"] = lon
        tmp['Ongoing'] = False
        for key in ['record start date', 'record end date']:
            if type(tmp[key]) is datetime.datetime:
                tmp[key] = tmp[key].isoformat()
            elif type(tmp[key]) is int:
                tmp[key] = datetime.datetime(tmp[key], 1 ,1).isoformat()
            elif type(tmp[key]) is str:
                tmp[key] = tmp[key].strip()
                if tmp[key].lower() == 'on going' or tmp[key].lower() == 'ongoing':
                    tmp[key] = datetime.datetime.now().isoformat()
                    tmp['Ongoing'] = True
                else:
                    if ',' in tmp[key]:
                        tmp[key] = datetime.datetime(int(tmp[key].split(',')[0]), 1, 1).isoformat()
                    if '/' in tmp[key]:
                        time = [int(t) for t in tmp[key].split('/')]
                        tmp[key] = datetime.datetime(time[2], time[1], time[0]).isoformat()
                    else:
                        tmp[key] = pd.Timestamp(tmp[key]).to_pydatetime().isoformat()

        tmp["PI Contact"] = re.split(';|,', tmp["PI Contact"])
        rows.append(tmp)

    json_file = Path(__file__).parent / "src" / "lib" / "data" / filename.name.replace("xlsx", "json")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':

    filename = Path(__file__).parent.parent / "data" / "TableWG31-jpv_td_GwB_AB.xlsx"
    convert_balloon_table(filename)

    # bib_file = os.path.join(os.path.dirname(__name__), 'static', 'bib', 'references.bib')
    # bib_file = os.path.join(os.path.dirname(__name__), 'static', 'bib', 'new_bibfile.bib')
    # for year in range(2007, 2022):
    #     generate_publication_html(bib_file, target_year=year)

    # bib_file = os.path.join(os.path.dirname(__name__), 'static', 'bib', 'ssirc.bib')
    # format_ssirc_bib(bib_file)