<script>
    import { LayerCake, Svg, Html } from "layercake";
    import AxisX from "$lib/components/graphics/shared/AxisX.svelte";
    import AxisY from "$lib/components/graphics/shared/AxisY.svelte";
    import Tooltip from "$lib/components/graphics/shared/Tooltip.svelte";
    import LineD3 from "$lib/components/graphics/shared/LineD3.svelte";
    import Highlight from "$lib/components/graphics/balloon/Highlight.svelte";
    import HLine from "$lib/components/graphics/shared/HLine.svelte";
    import { format } from "d3-format";

    export let data;
    export let parameters = ["Ro1", "Ro2"];
    export let parameterNames = ["Fine Mode", "Coarse Mode"];
    // export let xDomain = [0, 1];
    export let yDomain = [10, 35];
    export let xLabel = "";
    export let units = "";
    export let cursorPosition = { x: null, y: null };
    export let selectedAltitude = null;

    $: minValue = 0 //Math.min(
        // ...data.filter((x) => x.altitude > yDomain[0]).map((x) => Math.min(...parameters.map((p) => p(x)))),
    // );
    $: xDomain = [
        minValue < 0 ? 0 : minValue,
        Math.max(...data.filter((x) => x.altitude > yDomain[0]).map((x) => Math.max(...parameters.map((p) => p(x))))) * 1.1,
    ];
    let evt;
    let hideTooltip = true;
    const colors = ["#1261b5", "#b03510", "#444444"];
    const textColors = ["text-[#1261b5]", "text-[#b03510]", "text-[#444444]"];
    // const colors = ["bg-blue-500", "#b03510", "#444444"];
</script>

<div class="chart-container">
    <LayerCake
        {data}
        x={parameters[0]}
        y="altitude"
        padding={{ top: 5, right: 0, bottom: 40, left: 40 }}
        {xDomain}
        {yDomain}
        position="absolute">
        <Svg>
            <AxisX gridlines={true} ticks={5} />
            <AxisY gridlines={true} />
            <LineD3 stroke={colors[0]} />
        </Svg>
        <Html pointerEvents={false}>
            <div class="x-axis-label text-gray-800 text-nowrap" data-id="x-axis-label" style="top: 104%; left: 50%">
                {xLabel} <span class="text-sm text-gray-500">[{@html units}]</span>
            </div>
            <div class="y-axis-label text-gray-800" data-id="axis-label" style="top: 50%; left: 0%">
                Altitude <span class="text-sm text-gray-500">[km]</span>
            </div>
            {#if hideTooltip !== true}
                <Tooltip {evt} xoffset={-50} --width="170px" let:detail>
                    <div class="text-sm font-gray-800 font-bold">{xLabel}</div>
                    <hr class="my-2" />
                    {#each parameters as param, idx}
                        <p class={`text-sm font-bold leading-none uppercase mb-0 ${textColors[idx]}`}>
                            {parameterNames[idx]}
                        </p>
                        <p class="key-value">
                            {format("0.3f")(param(data.filter((x) => x.altitude === cursorPosition.y)[0]))}
                            {@html units}
                        </p>
                    {/each}
                </Tooltip>
            {/if}
        </Html>
    </LayerCake>
    {#each parameters.slice(1) as param, idx}
        <LayerCake
            {data}
            x={param}
            y="altitude"
            padding={{ top: 5, right: 0, bottom: 40, left: 40 }}
            {xDomain}
            {yDomain}
            position="absolute">
            <Svg>
                <LineD3 stroke={colors[idx + 1]} />
            </Svg>
        </LayerCake>
    {/each}
    <LayerCake
        {data}
        x={parameters[0]}
        y="altitude"
        padding={{ top: 5, right: 0, bottom: 40, left: 40 }}
        {xDomain}
        {yDomain}
        position="absolute">
        <Svg>
            <Highlight
                bind:position={cursorPosition}
                snapY={true}
                on:click={(e) => {
                    selectedAltitude = e.detail.props.y;
                }}
                on:mousemove={(event) => (evt = hideTooltip = event)}
                on:mouseout={() => (hideTooltip = true)} />
            <HLine y={cursorPosition.y} />
        </Svg>
    </LayerCake>
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
        height: 500px;
        position: relative;
    }
</style>
