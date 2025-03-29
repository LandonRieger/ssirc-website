<!--
  @component
  Generates an SVG column chart.
 -->
<script>
  import { getContext } from 'svelte';

  const { data, xGet, yGet, x, yRange, xScale, y, height, width } = getContext('LayerCake');

  /** @type {String} [fill='#00e047'] - The shape's fill color. */
  export let fill = '#00e047';

  /** @type {String} [stroke='#000'] - The shape's stroke color. */
  export let stroke = '#000';

  /** @type {Number} [strokeWidth=0] - The shape's stroke width. */
  export let strokeWidth = 0;

  /** @type {boolean} [false] - Show the numbers for each column */
  export let showLabels = false;

  const clipUuid = `clip-SizeDistribution`;
  const clipUrl = `url(#${clipUuid})`;

  $: columnWidth = d => {
    const vals = $xGet(d);
    return Math.abs(vals[1] - vals[0]);
  };

  $: columnHeight = d => {
    return $yRange[0] - $yGet(d);
  };
</script>

<clipPath id={clipUuid}>
    <rect x="0" y="0" width={$width} height={$height}></rect>
</clipPath>

<g class="column-group">
  {#each $data as d, i}
    {@const colHeight = columnHeight(d)}
    {@const xGot = $xGet(d)}
    {@const xPos = Array.isArray(xGot) ? xGot[0] : xGot}
    {@const colWidth = $xScale.bandwidth ? $xScale.bandwidth() : columnWidth(d)}
    {@const yValue = $y(d)}
    {#if !isNaN($yGet(d)) } 
    <rect
      class="group-rect"
      data-id={i}
      data-range={$x(d)}
      data-count={yValue}
      x={xPos}
      y={$yGet(d)}
      width={colWidth > 0 ? colWidth : 0}
      height={colHeight > 0 ? colHeight : 0}
      {fill}
      {stroke}
      stroke-width={strokeWidth}
      clip-path={clipUrl}
    />

    {#if showLabels && yValue}
      <text x={xPos + colWidth / 2} y={$height - colHeight - 5} text-anchor="middle">{yValue}</text>
    {/if}
    {/if}
  {/each}
</g>

<style>
  text {
    font-size: 12px;
  }
</style>