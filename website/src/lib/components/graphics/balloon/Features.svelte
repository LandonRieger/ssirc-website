<!--
	@component
	Generates an SVG scatter plot. This component can also work if the x- or y-scale is ordinal, i.e. it has a `.bandwidth` method. See the [timeplot chart](https://layercake.graphics/example/Timeplot) for an example.
 -->
 <script>
	import { getContext } from 'svelte';
	import { geoPath } from 'd3-geo';
	const { width, height } = getContext('LayerCake');

	/** @type {Function} projection – A D3 projection function. Pass this in as an uncalled function, e.g. `projection={geoAlbersUsa}`. */
	export let projection;

	export let features;
	export let extent;

	/** @type {String} [fill='#0cf'] – The circle's fill color. */
	export let fill = '#fff';
	export let fillOpacity = 0.2;

	/** @type {String} [stroke='#000'] – The circle's stroke color. */
	export let stroke = '#000';

	/** @type {Number} [strokeWidth=0] – The circle's stroke width. */
	export let strokeWidth = 0.5;
	export let rotate = [0, 0, 0];

	$: projectionFn = projection().rotate(rotate).fitSize([$width, $height], extent).precision(0.2);
	$: geoPathFn = geoPath(projectionFn);
</script>

{#if geoPathFn}
	<clipPath id="clipFeatureRect">
		<rect x={0} y={0} width={$width} height={$height} />
	</clipPath>
	<g class="map-group" clip-path="url(#clipFeatureRect)">
		{#each features as feature}
			<path
				class="feature-path"
				{fill}
				fill-opacity={fillOpacity}
				{stroke}
				stroke-width={strokeWidth}
				d={geoPathFn(feature)}
			></path>
		{/each}
	</g>
{/if}
