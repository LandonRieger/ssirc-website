export const properties = [
    {
        name: "Volume Density",
        value: {
            xLabel: "Volume Density",
            units: "&#181m<sup>3</sup>cm<sup>-3</sup>",
            maps: [(x) => x.volume],
            parameterNames: ["Total"],
        },
    },
    {
        name: "Surface Area Density",
        value: {
            xLabel: "Surface Area Density",
            units: "&#181m<sup>2</sup>cm<sup>-3</sup>",
            maps: [(x) => x.surface_area],
            parameterNames: ["Total"],
        },
    },
    {
        name: "Effective Radius",
        value: {
            xLabel: "Effective Radius",
            units: "&#181m",
            maps: [(x) => x.effective_radius],
            parameterNames: ["Total"],
        },
    },
    {
        name: "Number Density",
        value: {
            xLabel: "Number Density",
            units: "cm<sup>-3</sup>",
            maps: [(x) => x.No],
            parameterNames: ["Total"],
        },
    },
    {
        name: "Extinction",
        value: {
            xLabel: "Extinction",
            units: "km<sup>-1</sup>",
            maps: [(x) => x.extinction],
            parameterNames: ["Extinction at 532nm"],
        },
    },
];
