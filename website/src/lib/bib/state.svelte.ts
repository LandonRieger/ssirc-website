function entry_sort(a, b) {
    let namea;
    let nameb;

    let entrya = a[1];
    let entryb = b[1];
    if (entrya.author[0].name) {
        namea = entrya.author.name;
    } else {
        namea = entrya.author[0].split(",")[0];
    }

    if (entryb.author[0].name) {
        nameb = entryb.author.name;
    } else {
        nameb = entryb.author[0].split(",")[0];
    }

    if (namea === nameb) {
        return entrya.date - entryb.date;
    } else {
        return namea.localeCompare(nameb);
    }
}

export class Bibliography {
    entries = {}; //$state({}); // all the bibliography entries
    citations = $state<any>({}); //$state({});

    constructor(entries: any) {
        this.citations = {};
        this.entries = entries;
        // this.entries: any = $state(entries); // all the bibliography entries
        // this.citations: any = $state({});
    }

    citet(...keys): string {
        try {
            return this.citep("", ...keys);
        } catch {
            console.log("Could not render ", keys);
        }
    }

    cite(...keys: [string]): string {
        try {
            return this.citep("brackets", ...keys);
        } catch {
            console.log("Could not render ", keys);
        }
    }

    citep(format: string, ...keys: [string]): string {
        let html = `${format === "brackets" ? "(" : ""}<span class="italic pr-0.5">`;

        for (let i = 0; i < keys.length; i++) {
            const key = keys[i];
            // add a citation to keep tally of whats been used
            this.citations[key] = this.entries[key];
            let entry = this.entries[key];
            let author = entry.author[0];

            const num_auth = entry.author.length;
            const etal = num_auth > 1 ? " et. al., " : ", ";
            html = html + `<a href=#${key} class="text-gray-600">`;
            if (author.name) {
                html = html + `${author.prefix} ${author.name}${etal}${entry.date}`;
            } else {
                html = html + `${author.split(",")[0]}${etal}${entry.date}`;
            }
            html = html + `</a>`;
            if (i < keys.length - 1) {
                html += "; ";
            }
        }
        html = html + `</span>${format === "brackets" ? ")" : ""}`;

        return html;
    }

    print(sort: boolean = true): { entry: any; id: string }[] {
        if (sort) {
            const sorted_keys = Object.entries(this.citations).sort(entry_sort);

            return sorted_keys.map((key) => ({
                entry: key[1],
                id: key[0],
            }));
        } else {
            return this.citations;
        }
    }
}
