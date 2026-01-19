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
        return this.citep("", ...keys)
    }

    cite(...keys: [string]): string {
        return this.citep("brackets", ...keys)
    }

    citep(format: string, ...keys: [string]): string {
        let html = `${format === "brackets" ? "(" : ""}<span class="italic pr-0.5">`;

        for (let i = 0; i < keys.length; i++) {
            const key = keys[i];
            // add a citation to keep tally of whats been used
            this.citations[key] = this.entries[key];
            let entry = this.entries[key];
            let author = entry.author[0];

            const num_auth = entry.author.length
            const etal = num_auth > 1 ? " et. al., " : "";
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

    print(): { entry: any; id: string }[] {
        return Object.keys(this.citations).map((key) => ({
            entry: this.citations[key],
            id: key,
        }));
    }
}
