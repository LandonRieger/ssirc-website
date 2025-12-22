<!--
  @component
  Generates an SVG line shape using the `line` function from [d3-shape](https://github.com/d3/d3-shape).
 -->
<script>
    import { createEventDispatcher, getContext } from "svelte";
    import { line, curveLinear } from "d3-shape";
    import { scaleOrdinal } from "d3-scale";
    import { schemeCategory10 } from "d3-scale-chromatic";
    const { data, height, xScale, xGet } = getContext("LayerCake");

    /**
     * @typedef {Object} Props
     * @property {String} [stroke] - The shape's fill color. This is technically optional because it comes with a default value but you'll likely want to replace it with your own color.
     * @property {any} [colorDomain]
     * @property {Function} [curve] - An optional D3 interpolation function. See [d3-shape](https://github.com/d3/d3-shape#curves) for options. Pass this function in uncalled, i.e. without the open-close parentheses.
     */

    /** @type {Props} */
    let {
        stroke = "#ab00d6",
        colorDomain = [...new Set($data.map((x) => x.instrument))],
        curve = curveLinear,
    } = $props();
    const dispatch = createEventDispatcher();

    let color = $derived(scaleOrdinal(colorDomain, schemeCategory10));

    function handleMousemove(ds, glyph = "") {
        return function handleMousemoveFn(e) {
            // raise(this);
            // When the element gets raised, it flashes 0,0 for a second so skip that
            if (e.layerX !== 0 && e.layerY !== 0) {
                dispatch(`mousemove${glyph}`, { e, props: ds });
            }
        };
    }

    function handleClick(ds) {
        return function handleClickFn(e) {
            dispatch("click", { e, props: ds });
        };
    }
</script>

<g role="tooltip" onmouseout={(e) => dispatch("mouseout")} onblur={(e) => dispatch("mouseout")}>
    {#each $data as ds}
        <rect
            class="path-line"
            x={$xScale(ds.time)}
            y={0}
            height={$height}
            width="2"
            fill={color(ds.instrument)}
            stroke="none"
            onmouseover={(e) => dispatch("mousemove", { e, props: ds })}
            onfocus={(e) => dispatch("mousemove", { e, props: ds })}
            onmousemove={handleMousemove(ds)}
            onclick={handleClick(ds)}></rect>
    {/each}
</g>

<!--<style>-->
<!--    .path-line {-->
<!--        fill: none;-->
<!--        stroke-linejoin: round;-->
<!--        stroke-linecap: round;-->
<!--        stroke-width: 2;-->
<!--    }-->
<!--</style>-->
