<script>
    import { Html, LayerCake, Svg } from "layercake";
    import AxisX from "$lib/components/graphics/shared/AxisX.svelte";
    import AxisY from "$lib/components/graphics/shared/AxisY.svelte";
    import ScatterSwarm from "$lib/components/graphics/shared/ScatterSwarm.svelte";
    import { utcFormat } from "d3-time-format";
    import Tooltip from "$lib/components/graphics/shared/Tooltip.svelte";
    import { Select } from "flowbite-svelte";

    export let data;
    export let selected;
    let evt;
    let hideTooltip = true;
    let selectedInstrument = undefined;
    let selectedLocation = undefined;
    let filteredData = data;

    $: uniqueInstruments = [...new Set(data.map((x) => x.instrument))];
    $: uniqueLocations = [...new Set(data.map((x) => x.location))];
    $: instruments = [{ name: "All instruments", value: undefined }].concat(
        uniqueInstruments.map((x) => ({ name: x, value: x })),
    );
    $: locations = [{ name: "All locations", value: undefined }].concat(
        uniqueLocations.map((x) => ({ name: x, value: x })),
    );
    $: filteredData = updateFilters(selectedInstrument);
    $: filteredData = updateFilters(selectedLocation);

    function updateFilters(filters) {
        let filt = selectedInstrument ? data.filter((x) => x.instrument === selectedInstrument) : data;
        filt = selectedLocation ? filt.filter((x) => x.location === selectedLocation) : filt;
        return filt;
    }
</script>

<div class="flex flex-row">
    <div class="chart-container">
        <LayerCake
            data={filteredData}
            x="time"
            y="y"
            yDomain={[0, 1]}
            xDomain={[new Date("1989-01-01"), new Date("2025-01-01")]}
            padding={{ top: 5, right: 0, bottom: 20, left: 20 }}>
            <!-- Components go here -->
            <Svg>
                <AxisX gridlines={true} format={utcFormat("%Y")} />
                <AxisY gridlines={true} ticks={0} />
                <ScatterSwarm
                    colorDomain={uniqueInstruments}
                    on:mousemove={(event) => (evt = hideTooltip = event)}
                    on:mouseout={() => (hideTooltip = true)}
                    on:click={(event) =>
                        (selected = {
                            file: event.detail.props.file,
                            location: event.detail.props.location,
                            folder: event.detail.props.folder,
                        })} />
            </Svg>
            <Html pointerEvents={false}>
                {#if hideTooltip !== true}
                    <Tooltip {evt} xoffset={-50} --width="auto" let:detail>
                        <div class="key-value text-sm font-bold">{detail.props.time.toLocaleDateString('en-US', {month:"short", year: "numeric", day: "numeric"})}</div>
                        <hr class="mb-2" />
                        <p class="key-name">instrument</p>
                        <p class="key-value">{detail.props.instrument}</p>
                    </Tooltip>
                {/if}
            </Html>
        </LayerCake>
    </div>
    <div class="w-64 ml-4">
        <div class="font-bold text-gray-800">Filters</div>
        <Select class="mt-2" items={instruments} bind:value={selectedInstrument} />
        <Select class="mt-2" items={locations} bind:value={selectedLocation} />
    </div>
</div>

<style>
    /*
    The wrapper div needs to have an explicit width and height in CSS.
    It can also be a flexbox child or CSS grid element.
    The point being it needs dimensions since the <LayerCake> element will
    expand to fill it.
  */
    .chart-container {
        width: 100%;
        height: 130px;
    }
</style>
