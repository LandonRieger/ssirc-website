<script>
    import { Html, LayerCake, Svg } from "layercake";
    import AxisX from "$lib/components/graphics/shared/AxisX.svelte";
    import AxisY from "$lib/components/graphics/shared/AxisY.svelte";
    import ScatterSwarm from "$lib/components/graphics/shared/ScatterSwarm.svelte";
    import { utcFormat } from "d3-time-format";
    import Tooltip from "$lib/components/graphics/shared/Tooltip.svelte";
    import { Select } from "flowbite-svelte";
    import { utcYears } from "d3-time";

    export let data;
    export let selected;
    export let colorDomain;
    let evt;
    let hideTooltip = true;
    // let selectedInstrument = undefined;
    // let selectedLocation = undefined;
    // let filteredData = data;

    // $: uniqueInstruments = [...new Set(data.map((x) => x.instrument))];
    // $: uniqueLocations = [...new Set(data.map((x) => x.location))];
    // $: instruments = [{ name: "All instruments", value: undefined }].concat(
    //     uniqueInstruments.map((x) => ({ name: x, value: x })),
    // );
    // $: locations = [{ name: "All locations", value: undefined }].concat(
    //     uniqueLocations.map((x) => ({ name: x, value: x })),
    // );
    // $: filteredData = updateFilters(selectedInstrument);
    // $: filteredData = updateFilters(selectedLocation);

    // function updateFilters(filters) {
    //     let filt = selectedInstrument ? data.filter((x) => x.instrument === selectedInstrument) : data;
    //     filt = selectedLocation ? filt.filter((x) => x.location === selectedLocation) : filt;
    //     return filt;
    // }
</script>

<div class="flex flex-row grow">
    <div class="chart-container">
        <LayerCake
            {data}
            x="time"
            y="y"
            yDomain={[0, 1]}
            xDomain={[new Date("1989-01-01"), new Date("2025-01-01")]}
            padding={{ top: 5, right: 0, bottom: 20, left: 20 }}>
            <!-- Components go here -->
            <Svg>
                <AxisX
                    gridlines={true}
                    format={utcFormat("%Y")}
                    ticks={utcYears(new Date("1989-01-01"), new Date("2026-01-01"), 2)} />
                <AxisY gridlines={true} ticks={0} />
                <ScatterSwarm
                    {colorDomain}
                    on:mousemove={(event) => (evt = hideTooltip = event)}
                    on:mouseout={() => (hideTooltip = true)}
                    on:click={(event) =>
                        (selected = {
                            file: event.detail.props.file,
                            location: event.detail.props.location,
                            folder: event.detail.props.folder,
                            time: event.detail.props.time,
                        })} />
            </Svg>
            <Html pointerEvents={false}>
                {#if hideTooltip !== true}
                    <Tooltip {evt} xoffset={-50} --width="auto" let:detail>
                        <div class="key-name mb-2">
                            {detail.props.time.toLocaleDateString("en-US", {
                                month: "short",
                                year: "numeric",
                                day: "numeric",
                            })}
                        </div>
                        <hr class="mb-2" />
                        <div class="grid grid-col gap-y-2">
                            <div>
                                <div class="key-name">instrument</div>
                                <div class="key-value">{detail.props.instrument}</div>
                            </div>
                            <div>
                                <div class="key-name">Location</div>
                                <div class="key-value">{detail.props.location}</div>
                            </div>
                        </div>
                    </Tooltip>
                {/if}
            </Html>
        </LayerCake>
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
