export function uuid(short = true) {
    const id = crypto.randomUUID();
    if (short) {
        return id.slice(0, 6);
    } else {
        return id;
    }
}

export function linspace(startValue, stopValue, cardinality) {
    let arr = [];
    let step = (stopValue - startValue) / (cardinality - 1);
    for (let i = 0; i < cardinality; i++) {
        arr.push(startValue + step * i);
    }
    return arr;
}

export function logspace(startValue, stopValue, cardinality) {
    let arr = [];
    let logStart = Math.log(startValue);
    let logStop = Math.log(stopValue);
    let step = (logStop - logStart) / (cardinality - 1);
    for (let i = 0; i < cardinality; i++) {
        arr.push(Math.exp(logStart + step * i));
    }
    return arr;
}

export function range(startValue, stopValue, step) {
    let arr = [];
    let x = startValue;
    while (x <= stopValue) {
        arr.push(x);
        x = x + step;
    }
    return arr;
}

export function intersect(a, b) {
    let setB = new Set(b);
    return [...new Set(a)].filter((x) => setB.has(x));
    // console.log('intersect', a, b, c)
    // return c
}

export function nearestIndex(array, value) {
    let index = 0;
    let minDiff = undefined;
    for (let i = 0; i < array.length; i++) {
        if (Math.abs(array[i] - value) < minDiff || typeof minDiff === "undefined") {
            minDiff = Math.abs(array[i] - value);
            index = i;
        }
    }
    return index;
}

export function formatPower(x) {
    const e = Math.log10(x);
    if (e !== Math.floor(e)) return; // Ignore non-exact power of ten.
    return `10${(e + "").replace(/./g, (c) => "⁰¹²³⁴⁵⁶⁷⁸⁹"[c] || "⁻")}`;
}
