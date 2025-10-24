export const properties = [
    {
        name: "Temperature",
        value: {
            xLabel: "Temperature",
            units: "C",
            maps: [(x) => x.temperature],
            parameterNames: ["temperature"],
            minValue: -70.0,
            maxValue: 20.0,
        },
    },
];
