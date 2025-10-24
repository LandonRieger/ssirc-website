<script>
    import { onMount } from "svelte";
    import { Card, Select } from "flowbite-svelte";
    import ProfileSelector from "$lib/components/graphics/balloon/ProfileSelector.svelte";
    import NumberDensityProfile from "$lib/components/graphics/balloon/NumberDensityProfile.svelte";
    import SizeParameterProfile from "$lib/components/graphics/balloon/SizeParameterProfile.svelte";
    import SizeDistribution from "$lib/components/graphics/balloon/SizeDistribution.svelte";
    import { properties as uwProperties } from "$lib/uWyoming.js";
    import { properties as b2sapProperties } from "$lib/b2sap.js";
    import { properties as balneoProperties } from "$lib/balneo.js";
    import Map from "$lib/components/graphics/balloon/Map.svelte";
    import Filters from "$lib/components/graphics/balloon/Filters.svelte";
    import { getData, getFlights, nd_from_sd } from "$lib/loading.js";
    import { schemeTableau10 } from "d3-scale-chromatic";
    import { scaleOrdinal } from "d3-scale";

    // const colors = [schemeTableau10[0], schemeTableau10[1], schemeTableau10[2], schemeTableau10[4], schemeTableau10[5]];

    // const urlPrefix = "https://ssirc-website.onrender.com/"
    // const urlPrefix = "http://127.0.0.1:8000/";

    let data;
    let profile;
    let size;
    let altData;
    let paramData;
    let selected = {
        file: "20240312_CO_LOPC_208.500m_11.50km_Srs_ce.szd",
        location: "Boulder",
        folder: "UWyoming",
        time: new Date("2024-03-12"),
        instrument: "LOPC",
    };
    let selectedAltitude = 20.0;
    let selectedInstrument;
    let selectedLocation;
    let filteredData;

    const props = {"UWyoming": uwProperties, "B2SAP": b2sapProperties, "BalneO": balneoProperties};
    $: integratedProperties = props[selected.folder]; //selected.folder === "UWyoming" ? uwProperties : b2sapProperties;

    let lastFolder = "UWyoming";
    let plot1 = uwProperties[0].value;
    let plot2 = uwProperties[1].value;

    // Define some data
    $: flights = data ? data.map((p) => ({ ...p, time: new Date(p.time) })) : undefined;
    $: filteredData = updateLocationFilter(flights);
    $: updateData(selected);
    $: updateAltitude(selectedAltitude);
    $: uniqueInstruments = flights ? [...new Set(flights.map((x) => x.instrument))] : [];
    // $: uniqueLocations = flights ? [...new Set(flights.map((x) => x.location))] : [];
    $: colors = scaleOrdinal(uniqueInstruments, [
        schemeTableau10[0],
        schemeTableau10[1],
        schemeTableau10[2],
        schemeTableau10[4],
        schemeTableau10[5],
    ]);

    onMount(async () => {
        data = await getFlights();
    });

    function updateData(selected) {
        const updateParam = lastFolder !== selected.folder;
        lastFolder = selected.folder;
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
                            return getData(newFile.file, newFile.location, newFile.folder, "Nr");
                        } else {
                            console.log("ND file could not be found");
                            return null;
                        }
                    })
                    .then((data) => {
                        profile = data;
                        if (data) {
                            try {
                                altData = {
                                    bins: data.metadata.bins,
                                    concentration: data.data.filter((x) => x.altitude === selectedAltitude)[0]
                                        .concentration,
                                };
                            } catch {
                                altData = undefined;
                            }
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
                        try {
                            altData = {
                                bins: data.metadata.bins,
                                concentration: data.data.filter((x) => x.altitude === selectedAltitude)[0]
                                    .concentration,
                            };
                        } catch {
                            altData = undefined;
                        }
                        console.log("pops data", data);
                    } else {
                        paramData = undefined;
                        altData = undefined;
                    }
                });
            }
        }
        if (updateParam) {
            if (integratedProperties.length > 1) {
                plot1 = integratedProperties[0].value;
                plot2 = integratedProperties[1].value;
            } else {
                plot1 = integratedProperties[0].value;
                plot2 = integratedProperties[0].value;
            }
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

    function updateLocationFilter(flights) {
        // console.log('updating filters')
        let filt = selectedInstrument && flights ? flights.filter((x) => x.instrument === selectedInstrument) : flights;
        filt = selectedLocation && filt ? filt.filter((x) => x.location === selectedLocation) : filt;
        return filt;
    }
</script>

<!--<div>-->
<!--    click on a flight to see profile information. You can click on different altitudes in a profile to see detailed size-->
<!--    information.-->
<!--</div>-->

{#if flights}
    <Card class="max-w-screen-xl">
        <!-- <Card> -->
        <div class="row flex">
            <Map
                data={filteredData}
                {colors}
                click={(evt) => {
                    selectedLocation = evt.location;
                    filteredData = updateLocationFilter(flights);
                }}></Map>
            <Filters
                data={flights}
                {colors}
                select={(v) => {
                    selectedInstrument = v;
                    filteredData = updateLocationFilter(flights);
                }} />
        </div>
        {#if flights}
            <div class="mt-4">
                <ProfileSelector data={filteredData} bind:selected {colors} />
            </div>
        {/if}
    </Card>
    <div class="flex flex-row mt-4">
        <div class="font-bold text-gray-600">
            {selected.instrument} flight on {selected.time.toLocaleDateString("en-US", {
                year: "numeric",
                month: "long",
                day: "numeric",
            })} out of
            {selected.location}
        </div>
        <div class="ml-4 h-[1px] bg-gray-200 grow my-auto"></div>
    </div>

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
                        parameterNames={plot1.parameterNames}
                        minValue={plot1.minValue}
                        maxValue={plot1.maxValue}
                    />
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
                        parameterNames={plot2.parameterNames}
                        minValue={plot1.minValue}
                        maxValue={plot1.maxValue}
                    />
                </div>
            </Card>
        </div>
    {/if}

    {#if altData}
        <div class="flex flex-row mt-4">
            <div class="font-bold text-gray-600">
                Size distribution at {selectedAltitude} km
            </div>
            <div class="ml-4 h-[1px] bg-gray-200 grow my-auto"></div>
        </div>
        <Card class="max-w-screen-xl mt-4">
            <SizeDistribution data={altData} params={paramData} />
        </Card>
    {/if}
{/if}
