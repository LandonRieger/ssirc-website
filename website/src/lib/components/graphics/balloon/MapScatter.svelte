<!--
	@component
	Generates an SVG scatter plot. This component can also work if the x- or y-scale is ordinal, i.e. it has a `.bandwidth` method. See the [timeplot chart](https://layercake.graphics/example/Timeplot) for an example.
 -->
<script>
    import { getContext } from "svelte";
    import { geoPath } from "d3-geo";
    const { width, height } = getContext("LayerCake");
    import { scaleOrdinal } from "d3-scale";

    /** @type {Function} projection – A D3 projection function. Pass this in as an uncalled function, e.g. `projection={geoAlbersUsa}`. */
    export let projection;
    export let colorScale
    export let colorDomain
    export let features;
    export let extent;
    export let r;
    /** @type {String} [fill='#0cf'] – The circle's fill color. */
    export let fill = "#000";
    export let fillOpacity = .8;

    /** @type {String} [stroke='#000'] – The circle's stroke color. */
    export let stroke = "#000";

    /** @type {Number} [strokeWidth=0] – The circle's stroke width. */
    export let strokeWidth = 0.5;
    export let rotate = [0, 0, 0];

    $: color = scaleOrdinal(colorDomain, colorScale);
    $: projectionFn = projection().rotate(rotate).fitSize([$width, $height], extent);
    $: geoPathFn = geoPath(projectionFn);
</script>

{#if geoPathFn}
    <clipPath id="clipFeatureRect">
        <rect x={0} y={0} width={$width} height={$height} />
    </clipPath>
    <g class="map-group" clip-path="url(#clipFeatureRect)">
        {#each features as feature}
        {@const x = projectionFn([feature.longitude, feature.latitude])}
            <circle fill={color(feature.instrument)}  fill-opacity={fillOpacity} {r} cx={x[0]} cy={x[1]} />
        {/each}
    </g>
{/if}
