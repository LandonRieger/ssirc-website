<!--
  @component
  Generates an SVG line shape using the `line` function from [d3-shape](https://github.com/d3/d3-shape).
 -->
<script>
    import { getContext } from "svelte";
    import { line, curveLinear } from "d3-shape";
    import {uuid} from "$lib/utils.js";

    const { data, xGet, xScale, yGet, width, height } = getContext("LayerCake");

    const clipUuid = `clip-${uuid()}`;
    const clipUrl = `url(#${clipUuid})`;

    

    
  /**
   * @typedef {Object} Props
   * @property {String} [stroke] - The shape's fill color. This is technically optional because it comes with a default value but you'll likely want to replace it with your own color.
   * @property {Function} [curve] - An optional D3 interpolation function. See [d3-shape](https://github.com/d3/d3-shape#curves) for options. Pass this function in uncalled, i.e. without the open-close parentheses.
   */

  /** @type {Props} */
  let { stroke = "#ab00d6", curve = curveLinear } = $props();

    let path = $derived(line().x($xGet).y($yGet).curve(curve));
    // .defined($y)
</script>

<clipPath id={clipUuid}>
    <rect x="0" y="0" width={$width} height={$height}></rect>
</clipPath>

<path class="path-line" d={path($data)} {stroke} clip-path={clipUrl}></path>

<style>
    .path-line {
        fill: none;
        stroke-linejoin: round;
        stroke-linecap: round;
        stroke-width: 2;
    }
</style>
