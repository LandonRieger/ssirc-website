function reff(Ro, So) {
    return So > 0 ? Ro * Math.exp((5 / 2) * Math.log(So) ** 2) : 0.0;
}

function volume(No, Ro, So) {
    return So > 0 ? (4 / 3) * Math.PI * No * Ro ** 3 * Math.exp((9 / 2) * Math.log(So) ** 2) : 0.0;
}

function area(No, Ro, So) {
    return So > 0 ? 4 * Math.PI * No * Ro ** 2 * Math.exp(2 * Math.log(So) ** 2) : 0.0;
}

export const properties = [
    {
        name: "Volume Density",
        value: {
            xLabel: "Volume Density",
            units: "&#181m<sup>3</sup>cm<sup>-3</sup>",
            maps: [
                (x) => volume(x.No1, x.Ro1, x.So1),
                (x) => volume(x.No2, x.Ro2, x.So2),
                (x) => volume(x.No1, x.Ro1, x.So1) + volume(x.No2, x.Ro2, x.So2),
            ],
            parameterNames: ["Fine Mode", "Coarse Mode", "Combined"],
        },
    },
    {
        name: "Surface Area Density",
        value: {
            xLabel: "Surface Area Density",
            units: "&#181m<sup>2</sup>cm<sup>-3</sup>",
            maps: [
                (x) => area(x.No1, x.Ro1, x.So1),
                (x) => area(x.No2, x.Ro2, x.So2),
                (x) => area(x.No1, x.Ro1, x.So1) + area(x.No2, x.Ro2, x.So2),
            ],
            parameterNames: ["Fine Mode", "Coarse Mode", "Combined"],
        },
    },
    {
        name: "Effective Radius",
        value: {
            xLabel: "Effective Radius",
            units: "&#181m",
            maps: [
                (x) => reff(x.Ro1, x.So1),
                (x) => reff(x.Ro2, x.So2),
                (x) =>
                    (3 * (volume(x.No1, x.Ro1, x.So1) + volume(x.No2, x.Ro2, x.So2))) /
                    (area(x.No1, x.Ro1, x.So1) + area(x.No2, x.Ro2, x.So2)),
            ],
            parameterNames: ["Fine Mode", "Coarse Mode", "Combined"],
        },
    },
    {
        name: "Median Radius",
        value: {
            xLabel: "Median Radius",
            units: "&#181m",
            maps: [(x) => (x.Ro1 ? x.Ro1 : 0), (x) => (x.Ro2 ? x.Ro2 : 0)],
            parameterNames: ["Fine Mode", "Coarse Mode"],
        },
    },
    {
        name: "Width",
        value: {
            xLabel: "Width",
            units: "",
            maps: [(x) => (x.So1 ? x.So1 : 0), (x) => (x.So2 ? x.So2 : 0)],
            parameterNames: ["Fine Mode", "Coarse Mode"],
        },
    },
    {
        name: "Number Density",
        value: {
            xLabel: "Number Density",
            units: "cm<sup>-3</sup>",
            maps: [(x) => (x.No1 ? x.No1 : 0), (x) => (x.No2 ? x.No2 : 0)],
            parameterNames: ["Fine Mode", "Coarse Mode"],
        },
    },
];
