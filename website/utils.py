import os
import bibtexparser


def generate_publication_html(bib_file, target_year: int = None):

    with open(bib_file, encoding='utf-8') as bib:
        bib_entries = bibtexparser.load(bib)

    if target_year:
        html_file = os.path.join(os.path.dirname(__file__), 'templates', 'references', f'references_{target_year}.html')
    else:
        html_file = os.path.join(os.path.dirname(__file__), 'templates', 'references', 'references.html')

    html = "<div class='list-group mb-5'>\n"
    for entry in bib_entries.entries:
        authors = entry['author'].split(' and ')
        if authors[0].count(',') > 1:
            nauth = [a.strip() for a in authors[0].split(',')]
            if ' ' in nauth[0]:
                authors = ['. '.join([b[0] for b in auth.split(' ')[:-1]]) + f'. {auth.split(" ")[-1]}' for auth in nauth]
            else:
                if ' and ' in entry['author']:
                    authors = [f'{nauth[1].strip()} {nauth[0]}',] + nauth[2:] + [authors[1]]
                else:
                    authors = [f'{nauth[1].strip()} {nauth[0]}',] + nauth[2:]

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

        try:
            year = entry['year']
        except:
            year = ''

        if target_year is not None:
            if int(year) != target_year:
                continue

        title = entry['title']
        try:
            doi = entry['doi']
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

        html += f'<a href="http://doi.org/{doi}" class="list-group-item">'
        html += f'<div class ="d-flex w-100 justify-content-between" >'
        html += f'<h5 class="mb-0">{title}</h5>'
        html += f'<small>{year}</small></div><p class="mb-0">'

        for aidx, author in enumerate(authors):
            if aidx >= 5:
                html += f'et. al., '
                break
            html += f'{author}, '

        html = html[:-2]  # strip the trailing ", "
        html += f'</p>'
        if volume == '':
            html += f'<small>{journal}, {pages}</small>'
        else:
            html += f'<small>{journal}, {volume}, {pages}</small>'
        html += f'</a>\n'
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


if __name__ == '__main__':
    # bib_file = os.path.join(os.path.dirname(__name__), 'static', 'bib', 'references.bib')
    bib_file = os.path.join(os.path.dirname(__name__), 'static', 'bib', 'new_bibfile.bib')
    for year in range(2007, 2018):
        generate_publication_html(bib_file, target_year=year)

    # bib_file = os.path.join(os.path.dirname(__name__), 'static', 'bib', 'ssirc.bib')
    # format_ssirc_bib(bib_file)