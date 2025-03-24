<script>
    import { LayerCake, Svg, Html } from "layercake";
    import AxisX from "$lib/components/graphics/shared/AxisX.svelte";
    import AxisY from "$lib/components/graphics/shared/AxisY.svelte";
    import Tooltip from "$lib/components/graphics/shared/Tooltip.svelte";
    import { scaleLog, scaleLinear } from "d3-scale";
    import { format } from "d3-format";
    import AreaD3 from "$lib/components/graphics/shared/AreaD3.svelte";
    import { interpolateViridis } from "d3-scale-chromatic";
    import Highlight from "$lib/components/graphics/balloon/Highlight.svelte";
    import HLine from "$lib/components/graphics/shared/HLine.svelte";

    export let data;
    export let bins;
    export let yDomain = [10, 35];
    export let cursorPosition = { x: null, y: null };
    export let selectedAltitude = null;

    let evt;
    let hideTooltip = true;

    // let superscript = "⁰¹²³⁴⁵⁶⁷⁸⁹",
    // formatPower = function(d) { return (d + "").split("").map(function(c) { return superscript[c]; }).join(""); },
    // formatTick = function(d) { return 10 + formatPower(Math.round(Math.log(d) / Math.LN10)); };
</script>

<div class="chart-container">
    <LayerCake
        {data}
        x="concentration"
        y="altitude"
        padding={{ top: 5, right: 0, bottom: 40, left: 40 }}
        xDomain={[1e-6, 1000]}
        {yDomain}
        xScale={scaleLog()}>
        <!-- Components go here -->
        <Svg>
            <AxisX gridlines={true} ticks={5} format={format("1.0e")} />
            <AxisY gridlines={true} />
            <Highlight
                bind:position={cursorPosition}
                snapY={true}
                on:click={(e) => {
                    console.log('selecting altitude', e.detail.props.y)
                    selectedAltitude = e.detail.props.y;
                }} />
            {#each data[0].concentration as idx, c (c)}
                <AreaD3
                    idx={c}
                    on:mousemove={(event) => (evt = hideTooltip = event)}
                    on:mouseout={() => (hideTooltip = true)}
                    color={interpolateViridis(c / data[0].concentration.length)} />
            {/each}
            <HLine y={cursorPosition.y} />
        </Svg>
        <Html pointerEvents={false}>
            <div class="x-axis-label text-gray-800 text-nowrap" data-id="x-axis-label" style="top: 104%; left: 50%">
                Concentration <span class="text-sm text-gray-500">[cm<sup>-3</sup>]</span>
            </div>
            <div class="y-axis-label text-gray-800" data-id="axis-label" style="top: 50%; left: 0%">
                Altitude <span class="text-sm text-gray-500">[km]</span>
            </div>
            {#if hideTooltip !== true}
                <Tooltip {evt} xoffset={-50} --width="auto" let:detail>
                    <p class="key-name">radius</p>
                    <p class="key-value">> {bins[detail.props]} &#181m</p>
                </Tooltip>
            {/if}
        </Html>
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
    }
</style>
