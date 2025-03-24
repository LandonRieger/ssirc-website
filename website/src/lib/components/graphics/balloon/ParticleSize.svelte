<script>
    import { onMount } from "svelte";
    import { Card, Select } from "flowbite-svelte";
    import ProfileSelector from "$lib/components/graphics/balloon/ProfileSelector.svelte";
    import NumberDensityProfile from "$lib/components/graphics/balloon/NumberDensityProfile.svelte";
    import SizeParameterProfile from "$lib/components/graphics/balloon/SizeParameterProfile.svelte";
    import SizeDistribution from "$lib/components/graphics/balloon/SizeDistribution.svelte";

    let data;
    let profile;
    let size;
    let altData;
    let paramData;
    let selected = { file: "20240312_CO_LOPC_208.500m_11.50km_Srs_ce.szd", location: "Boulder" };
    let selectedAltitude = 20.0;
    let cursorPosition;

    const integratedProperties = [
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
    ];

    const derivedProperties = [
        {
            name: "Median Radius",
            value: {
                xLabel: "Median Radius",
                units: "&#181m",
                maps: [(x) => x.Ro1 ? x.Ro1 : 0, (x) => x.Ro2 ? x.Ro2 : 0],
                parameterNames: ["Fine Mode", "Coarse Mode"],
            },
        },
        {
            name: "Width",
            value: {
                xLabel: "Width",
                units: "",
                maps: [(x) => x.So1 ? x.So1 : 0, (x) => x.So2 ? x.So2 : 0],
                parameterNames: ["Fine Mode", "Coarse Mode"],
            },
        },
        {
            name: "Number Density",
            value: {
                xLabel: "Number Density",
                units: "cm<sup>-3</sup>",
                maps: [(x) => x.No1 ? x.No1 : 0, (x) => x.No2 ? x.No2 : 0],
                parameterNames: ["Fine Mode", "Coarse Mode"],
            },
        },
    ];

    let plot1 = derivedProperties[0].value;
    let plot2 = integratedProperties[0].value;

    // Define some data
    $: flights = data
        ? data.map((p) => ({
              time: new Date(p.time),
              y: 0,
              file: p.file,
              folder: p.folder,
              instrument: p.instrument,
              location: p.folder,
          }))
        : undefined;
    $: updateData(selected);
    $: updateAltitude(selectedAltitude);

    onMount(async () => {
        data = await getFlights();
    });

    function updateData(selected) {
        if (selected.file && selected.location) {
            console.log("updating selection with", selected);
            getData(selected.file, selected.location).then((data) => {
                if (data) {
                    size = data;
                    paramData = data.data.filter((x) => x.altitude === selectedAltitude)[0];
                } else {
                    paramData = undefined;
                }
            });
            nd_from_sd(selected.file, selected.location)
                .then((ndFile) => {
                    return ndFile;
                })
                .then((newFile) => {
                    if (newFile) {
                        return getData(newFile.file, newFile.folder);
                    } else {
                        console.log("ND file could not be found");
                        return null;
                    }
                })
                .then((data) => {
                    profile = data;
                    if (data) {
                        altData = {
                            bins: data.metadata.bins,
                            concentration: data.data.filter((x) => x.altitude === selectedAltitude)[0].concentration,
                        };
                    } else {
                        altData = undefined;
                    }
                });
        }
    }

    async function updateAltitude(altitude) {
        if (profile) {
            altData = {
                bins: profile.metadata.bins,
                concentration: profile.data.filter((x) => x.altitude === altitude)[0].concentration,
            };
        } else {
            altData = undefined;
        }
        if (size) {
            paramData = size.data.filter((x) => x.altitude === altitude)[0];
        } else {
            paramData = undefined;
        }
    }

    async function getFlights() {
        const url = `/api/balloon/flights`;
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

    async function getData(filename, folder = "Laramie") {
        // if (filename == selected.file) {
        //     return;
        // }
        const url = `/api/balloon/flight?filename=${filename}&folder=${folder}`;
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

    async function nd_from_sd(filename, folder = "Laramie") {
        const url = `/api/balloon/flight/nd_from_sd?filename=${filename}&folder=${folder}`;
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

    function reff(Ro, So) {
        return So > 0 ? Ro * Math.exp((5 / 2) * Math.log(So) ** 2) : 0.0;
    }

    function volume(No, Ro, So) {
        return So > 0 ? (4 / 3) * Math.PI * No * Ro ** 3 * Math.exp((9 / 2) * Math.log(So) ** 2) : 0.0;
    }

    function area(No, Ro, So) {
        return So > 0 ? 4 * Math.PI * No * Ro ** 2 * Math.exp(2 * Math.log(So) ** 2) : 0.0;
    }
</script>

<div>
    click on a flight to see profile information. You can click on different altitudes in a profile to see detailed size
    information.
</div>
{#if flights}
    <Card class="max-w-screen-xl">
        <ProfileSelector data={flights} bind:selected />
    </Card>
{/if}

{#if profile && size}
    <div class="grid grid-cols-3 space-x-4">
        <Card class="md mt-4 flex-col justify-between">
            <div class="font-medium text-gray-800 mb-4">Number Density Concentrations</div>
            <NumberDensityProfile
                bind:selectedAltitude
                data={profile["data"]}
                bins={profile["metadata"]["bins"]} />
        </Card>
        <Card class="md mt-4">
            <div class="col space-y-4">
                <div class="font-medium text-gray-800">Retrieved Lognormal Properties</div>
                <Select class="mt-2" items={derivedProperties} bind:value={plot1} />
                <SizeParameterProfile
                    bind:selectedAltitude
                    data={size["data"]}
                    xLabel={plot1.xLabel}
                    units={plot1.units}
                    parameters={plot1.maps}
                    parameterNames={plot1.parameterNames} />
            </div>
        </Card>
        <Card class="md mt-4">
            <div class="col space-y-4">
                <div class="font-medium text-gray-800">Distribution Moments</div>
                <Select class="mt-2" items={integratedProperties} bind:value={plot2} />
                <SizeParameterProfile
                    bind:selectedAltitude
                    data={size["data"]}
                    xLabel={plot2.xLabel}
                    units={plot2.units}
                    parameters={plot2.maps}
                    parameterNames={plot2.parameterNames} />
            </div>
        </Card>
    </div>
{/if}

{#if altData}
    <Card class="max-w-screen-xl mt-4">
        <SizeDistribution data={altData} params={paramData} />
    </Card>
{/if}
