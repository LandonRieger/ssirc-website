<script>
    import { Select } from "flowbite-svelte";
    import { onMount } from "svelte";

    export let data;
    export let filteredData;

    let selectedLocation
    let selectedInstrument

    $: uniqueInstruments = data ? [...new Set(data.map((x) => x.instrument))] : [];
    $: uniqueLocations = data ? [...new Set(data.map((x) => x.location))] : [];
    $: instruments = [{ name: "All instruments", value: undefined }].concat(
        uniqueInstruments.map((x) => ({ name: x, value: x })),
    );
    $: locations = [{ name: "All locations", value: undefined }].concat(
        uniqueLocations.map((x) => ({ name: x, value: x })),
    );

    $: filteredData = updateFilters(selectedInstrument);
    $: filteredData = updateFilters(selectedLocation);

    function updateFilters(filters) {
        // console.log('updating filters')
        let filt = selectedInstrument && data ? data.filter((x) => x.instrument === selectedInstrument) : data;
        filt = selectedLocation && filt ? filt.filter((x) => x.location === selectedLocation) : filt;
        return filt;
    }
</script>



<div class="w-64 ml-8">
    <div class="font-bold text-gray-800">Filters</div>
    <Select class="mt-2" placeholder={"Choose an instrument"} items={instruments} bind:value={selectedInstrument} />
    <Select class="mt-2" placeholder={"Choose a location"} items={locations} bind:value={selectedLocation} />
</div>