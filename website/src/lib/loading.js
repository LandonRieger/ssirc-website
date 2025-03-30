const urlPrefix = "http://127.0.0.1:8000/";

export async function getFlights() {
    const url = `${urlPrefix}api/balloon/flights`;
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(error.message);
    }
}

export async function getData(filename, folder = "Laramie", campaign = "UWyoming", mode = null) {
    let url = `${urlPrefix}api/balloon/flight?filename=${filename}&folder=${folder}&campaign=${campaign}`;
    if (mode) {
        url = `${url}&mode=${mode}`;
    }
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(error.message);
    }
}

export async function nd_from_sd(filename, folder = "Laramie", campaign = "UWyoming") {
    const url = `${urlPrefix}api/balloon/flight/nd_from_sd?filename=${filename}&folder=${folder}&campaign=${campaign}`;
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        return await response.json();
        // return json;
    } catch (error) {
        console.error(error.message);
    }
}