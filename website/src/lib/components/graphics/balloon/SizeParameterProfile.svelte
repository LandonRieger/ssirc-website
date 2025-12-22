<script>
    import { LayerCake, Svg, Html } from "layercake";
    import AxisX from "$lib/components/graphics/shared/AxisX.svelte";
    import AxisY from "$lib/components/graphics/shared/AxisY.svelte";
    import Tooltip from "$lib/components/graphics/shared/Tooltip.svelte";
    import LineD3 from "$lib/components/graphics/shared/LineD3.svelte";
    import Highlight from "$lib/components/graphics/balloon/Highlight.svelte";
    import HLine from "$lib/components/graphics/shared/HLine.svelte";
    import { format } from "d3-format";
    import { schemeCategory10, schemeTableau10 } from "d3-scale-chromatic";

    
  /**
   * @typedef {Object} Props
   * @property {any} data
   * @property {any} [parameters]
   * @property {any} [parameterNames]
   * @property {any} [yDomain] - export let xDomain = [0, 1];
   * @property {string} [xLabel]
   * @property {string} [units]
   * @property {any} [cursorPosition]
   * @property {any} [selectedAltitude]
   * @property {any} [minValue]
   * @property {any} [maxValue]
   */

  /** @type {Props} */
  let {
    data,
    parameters = ["Ro1", "Ro2"],
    parameterNames = ["Fine Mode", "Coarse Mode"],
    yDomain = [10, 35],
    xLabel = "",
    units = "",
    cursorPosition = $bindable({ x: null, y: null }),
    selectedAltitude = $bindable(null),
    minValue = null,
    maxValue = null
  } = $props();

     //Math.min(
    // ...data.filter((x) => x.altitude > yDomain[0]).map((x) => Math.min(...parameters.map((p) => p(x)))),
    // );
    let highValue = $derived(Math.max(...data.filter((x) => x.altitude > yDomain[0]).map((x) => Math.max(...parameters.map((p) => p(x))))) * 1.1);
    let xDomain = $derived([
        minValue ? minValue : lowValue < 0 ? 0 : lowValue,
        maxValue ? maxValue : highValue,
    ]);
    let evt = $state();
    let hideTooltip = $state(true);
    const colors = ["#5778a4", "#b03510", "#444444"];
    // const colors = schemeTableau10
    const textColors = ["text-[#5778a4]", "text-[#b03510]", "text-[#444444]"];
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
                <Tooltip {evt} xoffset={-50} --width="170px" >
                    {#snippet children({ detail })}
                    <div class="text-sm font-gray-800 font-bold">{xLabel}</div>
                      <hr class="my-2" />
                      <div class="grid grid-col gap-y-2">
                          {#each parameters as param, idx}
                              <div>
                                  <div class={`key-name ${textColors[idx]}`}>
                                      {parameterNames[idx]}
                                  </div>
                                  <div class="key-value">
                                      {format("0.3f")(param(data.filter((x) => x.altitude === cursorPosition.y)[0]))}
                                      {@html units}
                                  </div>
                              </div>
                          {/each}
                      </div>
                                    {/snippet}
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
