<!--
  @component
  Generates an SVG line shape using the `line` function from [d3-shape](https://github.com/d3/d3-shape).
 -->
<script>
    import { getContext } from "svelte";
    const { yScale, width } = getContext("LayerCake");
    export let stroke = "#444444";
    export let y;
    export let pointerEvents = "none";
    export let strokeWidth = "1";

    $: yData = $yScale(y);
</script>

{#if y}
    <line
        x1="0"
        y1={yData}
        x2={$width}
        y2={yData}
        {stroke}
        stroke-width={strokeWidth}
        pointer-events={pointerEvents}
        stroke-dasharray="4" />
{/if}
