<script>
    import { createEventDispatcher, getContext } from "svelte";
    import { area, line, curveLinear, curveCardinal } from "d3-shape";

    const { data, yScale, xScale, xDomain, yDomain, width, height } = getContext("LayerCake");
    const clipUuid = `clip-ND`;
    const clipUrl = `url(#${clipUuid})`;

    export let curve = curveCardinal;
    export let color = "#97C555";

    let fitCurve;
    export let idx = 0;

    $: {
        fitCurve = area()
            .x0((d) => $xScale(d.concentration[idx]))
            .x1($xScale($xDomain[0]))
            .y((d) => $yScale(d.altitude))
            .curve(curve);
    }

    const dispatch = createEventDispatcher();

    function handleMousemove(ds, glyph = "") {
        return function handleMousemoveFn(e) {
            // raise(this);
            // When the element gets raised, it flashes 0,0 for a second so skip that
            if (e.layerX !== 0 && e.layerY !== 0) {
                dispatch(`mousemove${glyph}`, { e, props: ds });
            }
        };
    }
</script>

<clipPath id={clipUuid}>
    <rect x="0" y="0" width={$width} height={$height}></rect>
</clipPath>

<g role="tooltip" on:mouseout={(e) => dispatch("mouseout")} on:blur={(e) => dispatch("mouseout")}>
    <!--{#each $data.levels as level, index}-->
    <!--    <path-->
    <!--        role="tooltip"-->
    <!--        class="path-area"-->
    <!--        d={fitArea(level.data)}-->
    <!--        fill={level.color}-->
    <!--        fill-opacity={level.opacity}-->
    <!--        stroke="#FFFFFF"-->
    <!--        stroke-width="1"-->
    <!--        clip-path={clipUrl}-->
    <!--        on:mouseover={(e) => dispatch("mousemove", { e, props: level })}-->
    <!--        on:focus={(e) => dispatch("mousemove", { e, props: level })}-->
    <!--        on:mousemove={handleMousemove(level)} />-->
    <!--{/each}-->
    <path
        class="opacity-40 hover:opacity-80"
        d={fitCurve($data)}
        stroke={"none"}
        stroke-width="2"
        fill={color}
        clip-path={clipUrl}
        on:mouseover={(e) => dispatch("mousemove", { e, props: idx })}
        on:focus={(e) => dispatch("mousemove", { e, props: idx })}
        on:mousemove={handleMousemove(idx)} />
    <!--{#if $data.base.value < $xDomain[1]}-->
    <!--    <path-->
    <!--        role="tooltip"-->
    <!--        d={baseLine}-->
    <!--        stroke="#444444"-->
    <!--        stroke-dasharray="4 1"-->
    <!--        stroke-width="1"-->
    <!--        fill="none" />-->
    <!--    <path-->
    <!--        role="tooltip"-->
    <!--        d={baseLine}-->
    <!--        stroke="#FFFFFF"-->
    <!--        stroke-width="6"-->
    <!--        fill="none"-->
    <!--        stroke-opacity="0"-->
    <!--        on:mouseover={(e) => dispatch("mousemoveBase", { e, props: $data.base })}-->
    <!--        on:focus={(e) => dispatch("mousemoveBase", { e, props: $data.base })}-->
    <!--        on:mousemove={handleMousemove($data.base, "Base")} />-->
    <!--{/if}-->
</g>

<!--<style>-->
<!--    .nd-area {-->
<!--        fill-opacity-->
<!--    }-->

<!--</style>-->
