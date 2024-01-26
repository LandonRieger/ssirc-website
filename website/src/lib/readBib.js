export function parseBibEntries(entries) {
    let fields = ["author", "title", "journal", "doi", "year"];

    let data = {};
    let entryList = [];

    entries = entries.split("@article");

    for (let entry of entries) {
        data = {};
        for (let field of fields) {
            try {
                data[field] = entry.split(`${field} =`)[1];
                data[field] = data[field].match(new RegExp("{([^}]+)}"))[1];
            } catch (error) {
                data[field] = undefined;
            }
        }
        if (data.doi === undefined) {
            try {
                data["doi"] = entry.split("DOI")[1];
                data["doi"] = data["doi"].match(new RegExp("{([^}]+)}"))[1];
            } catch (error) {
                data["doi"] = undefined;
            }
        }
        if (data.doi) {
            data.doi = data.doi.replace('https://doi.org/', '')
        }

        if (data.year) {
            data.year = Number(data.year);
        }
        if (data.title) {
            entryList.push(data);
        }
    }
    return entryList;
}

export function groupBibEntriesByYear(entries) {
    // entries.sort((a, b) => b.year - a.year)
    let uniqueYears = [...new Set(entries.map(a => a.year))];
    let entriesByYear = {}
    for (let year of uniqueYears) {
        entriesByYear[year.toString()] = []
    }
    for (let entry of entries) {
        entriesByYear[entry.year.toString()].push(entry)
    }
    return entriesByYear
}