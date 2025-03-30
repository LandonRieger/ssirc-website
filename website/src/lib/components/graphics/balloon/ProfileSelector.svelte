<script>
    import { Html, LayerCake, Svg } from "layercake";
    import AxisX from "$lib/components/graphics/shared/AxisX.svelte";
    import AxisY from "$lib/components/graphics/shared/AxisY.svelte";
    import ScatterSwarm from "$lib/components/graphics/shared/ScatterSwarm.svelte";
    import { utcFormat } from "d3-time-format";
    import Tooltip from "$lib/components/graphics/shared/Tooltip.svelte";
    import { utcYears } from "d3-time";

    let {data, selected = $bindable(), colors} = $props()
    let evt = $state(undefined);
    let hideTooltip = $state(true);
</script>

<div>Click on a profile to load results</div>
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
                    {colors}
                    on:mousemove={(event) => (evt = hideTooltip = event)}
                    on:mouseout={() => (hideTooltip = true)}
                    on:click={(event) =>
                        (selected = {
                            ...event.detail.props
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
