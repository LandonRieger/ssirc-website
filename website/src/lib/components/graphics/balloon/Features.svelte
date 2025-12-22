<!--
	@component
	Generates an SVG scatter plot. This component can also work if the x- or y-scale is ordinal, i.e. it has a `.bandwidth` method. See the [timeplot chart](https://layercake.graphics/example/Timeplot) for an example.
 -->
 <script>
	import { getContext } from 'svelte';
	import { geoPath } from 'd3-geo';
	const { width, height } = getContext('LayerCake');

	/**
	 * @typedef {Object} Props
	 * @property {Function} projection – A D3 projection function. Pass this in as an uncalled function, e.g. `projection={geoAlbersUsa} projection
	 * @property {any} features
	 * @property {any} extent
	 * @property {String} [fill]
	 * @property {number} [fillOpacity]
	 * @property {String} [stroke]
	 * @property {Number} [strokeWidth]
	 * @property {any} [rotate]
	 */

	/** @type {Props} */
	let {
		projection,
		features,
		extent,
		fill = '#fff',
		fillOpacity = 0.2,
		stroke = '#000',
		strokeWidth = 0.5,
		rotate = [0, 0, 0]
	} = $props();

	let projectionFn = $derived(projection().rotate(rotate).fitSize([$width, $height], extent).precision(0.2));
	let geoPathFn = $derived(geoPath(projectionFn));
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
