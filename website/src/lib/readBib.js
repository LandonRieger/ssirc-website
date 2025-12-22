function replaceGlyphs(text) {
    let glyphs = {"\\AA": "&Aring", '\\"u': "&uuml;"};
    for (let glyph in glyphs) {
        text = text.replaceAll(glyph, glyphs[glyph])
    }
    return text
}


function parseEntry(entry) {
    const fields = ["author", "title", "journal", "doi", "year"];
    let data = {};
    data["key"] = entry.split(",", 1)[0];
    console.log("Parsing entry:", data["key"]);
    for (let field of fields) {
        try {
            data[field] = entry.split(`${field} =`)[1];
            data[field] = data[field].match(new RegExp("{([^}]+)}"))[1];
        } catch (error) {
            data[field] = undefined;
        }
    }
    // if (data.author) {
    //     data.author = replaceGlyphs(data.author);
    // }
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
    return data;
}

export function parseBibEntries(entries) {

    let entryList = [];
    entries = entries.split(/@article|@in/);

    for (let entry of entries) {
        let data = parseEntry(entry);
        if (data.title) {
            entryList.push(data);
        }
    }
    return entryList;
}

export function groupBibEntriesByYear(entries) {
    // entries.sort((a, b) => b.year - a.year)
    let uniqueYears = [...new Set(entries.map(a => a.date))];
    let entriesByYear = {}
    for (let year of uniqueYears) {
        entriesByYear[year.toString()] = []
    }
    for (let entry of entries) {
        entriesByYear[entry.date.toString()].push(entry)
    }
    return entriesByYear
}