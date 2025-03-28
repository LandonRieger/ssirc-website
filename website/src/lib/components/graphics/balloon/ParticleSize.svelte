<script>
    import { onMount } from "svelte";
    import { Card, Select } from "flowbite-svelte";
    import ProfileSelector from "$lib/components/graphics/balloon/ProfileSelector.svelte";
    import NumberDensityProfile from "$lib/components/graphics/balloon/NumberDensityProfile.svelte";
    import SizeParameterProfile from "$lib/components/graphics/balloon/SizeParameterProfile.svelte";
    import SizeDistribution from "$lib/components/graphics/balloon/SizeDistribution.svelte";
    import { properties as uwProperties } from "$lib/uWyoming.js";
    import { properties as b2sapProperties } from "$lib/b2sap.js";

    let data;
    let profile;
    let size;
    let altData;
    let paramData;
    let selected = { file: "20240312_CO_LOPC_208.500m_11.50km_Srs_ce.szd", location: "Boulder", folder: "UWyoming" };
    let selectedAltitude = 20.0;
    let cursorPosition;

    $: integratedProperties = selected.folder === "UWyoming" ? uwProperties : b2sapProperties;

    let lastFolder = 'UWyoming'
    let plot1 = uwProperties[0].value;
    let plot2 = uwProperties[0].value;

    // Define some data
    $: flights = data
        ? data.map((p) => ({
              time: new Date(p.time),
              y: 0,
              file: p.file,
              folder: p.folder,
              instrument: p.instrument,
              location: p.location,
          }))
        : undefined;
    $: updateData(selected);
    $: updateAltitude(selectedAltitude);

    onMount(async () => {
        data = await getFlights();
        console.log("data", data);
    });

    function updateData(selected) {
        const updateParam = lastFolder !== selected.folder
        lastFolder = selected.folder
        if (selected.file && selected.location) {
            console.log("updating selection with", selected);
            if (selected.folder === "UWyoming") {
                getData(selected.file, selected.location, selected.folder).then((data) => {
                    if (data) {
                        size = data;
                        paramData = data.data.filter((x) => x.altitude === selectedAltitude)[0];
                    } else {
                        paramData = undefined;
                    }
                });
                nd_from_sd(selected.file, selected.location, selected.folder)
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
                                concentration: data.data.filter((x) => x.altitude === selectedAltitude)[0]
                                    .concentration,
                            };
                        } else {
                            altData = undefined;
                        }
                    });
            } else {
                getData(selected.file, selected.location, selected.folder).then((data) => {
                    if (data) {
                        size = data;
                        profile = data;
                        paramData = undefined;
                        altData = {
                            bins: data.metadata.bins,
                            concentration: data.data.filter((x) => x.altitude === selectedAltitude)[0].concentration,
                        };
                        console.log("pops data", data);
                    } else {
                        paramData = undefined;
                        altData = undefined;
                    }
                });
            }
        }
        if (updateParam) {
            plot1 = integratedProperties[0].value
            plot2 = integratedProperties[1].value
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

    async function getData(filename, folder = "Laramie", campaign = "UWyoming") {
        const url = `/api/balloon/flight?filename=${filename}&folder=${folder}&campaign=${campaign}`;
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

    async function nd_from_sd(filename, folder = "Laramie", campaign = "UWyoming") {
        const url = `/api/balloon/flight/nd_from_sd?filename=${filename}&folder=${folder}&campaign=${campaign}`;
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

{#if profile}
    <div class="grid grid-cols-3 gap-4">
        <Card class="md mt-4 flex-col justify-between">
            <div class="font-medium text-gray-800 mb-4">Number Density Concentrations</div>
            <NumberDensityProfile bind:selectedAltitude data={profile["data"]} bins={profile["metadata"]["bins"]} />
        </Card>
        <Card class="md mt-4">
            <div class="col space-y-4">
                <!--                <div class="font-medium text-gray-800">Retrieved Lognormal Properties</div>-->
                <Select class="mt-0" items={integratedProperties} bind:value={plot1} />
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
                <!--                <div class="font-medium text-gray-800">Distribution Moments</div>-->
                <Select class="mt-0" items={integratedProperties} bind:value={plot2} />
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
