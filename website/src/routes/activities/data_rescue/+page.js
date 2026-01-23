// import * as data from "$lib/data/data_rescue/postagung.json";
import jsonData from "$lib/data/data_rescue/postagung.json" with { type: "json" };

export function load() {
    return jsonData;
}
