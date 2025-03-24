<script>
    import { LayerCake, Svg, Html } from "layercake";
    import AxisX from "$lib/components/graphics/shared/AxisX.svelte";
    import AxisY from "$lib/components/graphics/shared/AxisY.svelte";
    import Tooltip from "$lib/components/graphics/shared/Tooltip.svelte";
    import { scaleLog, scaleLinear } from "d3-scale";
    import { logspace } from "$lib/utils.js";
    import Column from "$lib/components/graphics/shared/Column.svelte";
    import LineD3 from "$lib/components/graphics/shared/LineD3.svelte";
    import { format } from "d3-format";

    export let data;
    export let params;
    let evt;
    let hideTooltip = true;

    const xDomain = [0.1, 3];
    const r = logspace(xDomain[0], xDomain[1], 300);
    const xScale = scaleLog();
    const yScale = scaleLog();
    function logNormal(r, rg, sigma) {
        return (
            (1 / (r * Math.log(sigma) * Math.sqrt(2 * Math.PI))) *
            Math.exp((-1 * (Math.log(r) - Math.log(rg)) ** 2) / (2 * Math.log(sigma) ** 2))
        );
    }
    $: binned = formatData(data);
    // $: yDomain = [0.0001, Math.max(...binned.map((x) => x.concentration)) * 1.1];
    $: yDomain = [1e-6, Math.max(...binned.map((x) => x.concentration)) * 1.1];
    $: logData = params
        ? r.map((x) => ({
              radius: x,
              y:
                  params.No2 > 0
                      ? params.No1 * logNormal(x, params.Ro1, params.So1) +
                        params.No2 * logNormal(x, params.Ro2, params.So2)
                      : params.No1 * logNormal(x, params.Ro1, params.So1),
          }))
        : undefined;

    function formatData(ds) {
        let bins = [];
        let width = 0.0;
        let conc = 0.0;
        for (let i = ds.bins.length - 1; i >= 0; i--) {
            if (i === ds.bins.length - 1) {
                width = ds.bins[i];
                conc = ds.concentration[i] < 0 ? 0 : ds.concentration[i];
                bins[i] = { bins: [ds.bins[i], ds.bins[i] * 2], concentration: conc / width };
            } else {
                width = ds.bins[i + 1] - ds.bins[i];
                conc = ds.concentration[i] - ds.concentration[i + 1];
                conc = conc < 0 ? 0 : conc;
                bins[i] = {
                    bins: [ds.bins[i], ds.bins[i + 1]],
                    concentration: conc / width,
                };
            }
        }
        return bins;
    }
</script>

<div class="chart-container">
    <LayerCake
        data={binned}
        position="absolute"
        x="bins"
        y="concentration"
        padding={{ top: 5, right: 0, bottom: 40, left: 55 }}
        {xDomain}
        {yDomain}
        {yScale}
        {xScale}>
        <!-- Components go here -->
        <Svg>
            <AxisX gridlines={true} ticks={5} />
            <AxisY gridlines={true} format={format("1.0e")} />
            <Column fill={"#1261b5"} strokeWidth={1} stroke={"#FFF"} />
        </Svg>
        <Html pointerEvents={false}>
            <div class="x-axis-label text-gray-800" data-id="x-axis-label" style="top: 109%; left: 50%">
                Diameter <span class="text-sm text-gray-500">[&#181m]</span>
            </div>
            <div class="y-axis-label text-gray-800" data-id="axis-label" style="top: 50%; left: -10px">
                Concentration <span class="text-sm text-gray-500">[cm<sup>-3</sup>&#181m<sup>-1</sup>]</span>
            </div>
            <!--{#if hideTooltip !== true}-->
            <!--    <Tooltip {evt} xoffset={-50} &#45;&#45;width="250px" let:detail>-->
            <!--        <div>radius > {bins[detail.props]} um</div>-->
            <!--    </Tooltip>-->
            <!--{/if}-->
        </Html>
    </LayerCake>

    {#if logData}
        <LayerCake
            data={logData}
            position="absolute"
            x="radius"
            y="y"
            padding={{ top: 5, right: 0, bottom: 40, left: 40 }}
            {xDomain}
            {yDomain}
            {yScale}
            {xScale}>
            <!-- Components go here -->
            <Svg>
                <LineD3 stroke={"#000"} />
            </Svg>
        </LayerCake>
    {/if}
</div>

<style>
    /*
    The wrapper div needs to have an explicit width and height in CSS.
    It can also be a flexbox child or CSS grid element.
    The point being it needs dimensions since the <LayerCake> element will
    expand to fill it.
  */
    .chart-container {
        position: relative;
        width: 100%;
        height: 350px;
    }
</style>
