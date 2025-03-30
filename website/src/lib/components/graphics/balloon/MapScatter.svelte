<!--
	@component
	Generates an SVG scatter plot. This component can also work if the x- or y-scale is ordinal, i.e. it has a `.bandwidth` method. See the [timeplot chart](https://layercake.graphics/example/Timeplot) for an example.
 -->
<script>
    import { getContext } from "svelte";
    import { geoPath } from "d3-geo";
    const { width, height } = getContext("LayerCake");

    let {
        rotate = [0, 0, 0],
        projection,
        colors,
        features,
        extent,
        r,
        fillOpacity,
        mouseover,
        mouseout,
        click,
    } = $props();

    let hoverLocation = $state({ location: undefined });

    const projectionFn = $derived(projection().rotate(rotate).fitSize([$width, $height], extent));
    const geoPathFn = $derived(geoPath(projectionFn));
</script>

{#if geoPathFn}
    <clipPath id="clipFeatureRect">
        <rect x={0} y={0} width={$width} height={$height} />
    </clipPath>
    <g class="map-background">
        <rect
            x={0}
            y={0}
            width={$width}
            height={$height}
            fill="#FFFFFF"
            fill-opacity={0}
            onclick={(evt) => {
                click({ evt: evt, location: undefined });
            }} />
    </g>
    <g class="map-group" clip-path="url(#clipFeatureRect)">
        {#each features as feature}
            {@const x = projectionFn([feature.longitude, feature.latitude])}
            <circle
                fill={colors(feature.instrument)}
                fill-opacity={fillOpacity}
                r={feature.location === hoverLocation.location ? r * 2 : r}
                cx={x[0]}
                cy={x[1]}
                onmouseover={(evt) => {
                    hoverLocation = { evt: evt, location: feature.location };
                    mouseover(hoverLocation);
                }}
                onmouseout={(evt) => {
                    hoverLocation = { evt: undefined, location: undefined };
                    mouseout(hoverLocation);
                }}
                onblur={(evt) => {
                    hoverLocation = { evt: undefined, location: undefined };
                    mouseout(hoverLocation);
                }}
                onclick={(evt) => {
                    click({ evt: evt, location: feature.location });
                }} />
        {/each}
    </g>
{/if}
