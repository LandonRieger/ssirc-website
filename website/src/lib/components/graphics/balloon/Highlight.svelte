<script>
    import { createEventDispatcher, getContext } from "svelte";
    import { nearestIndex } from "$lib/utils.js";

    const { data, width, height, xScale, padding, yScale, yGet, y } = getContext("LayerCake");

    const dispatch = createEventDispatcher();

    export let position;
    export let snapY = false;
    export let snapX = false;

    $: yValues = $data.map((d) => $y(d));
    function setXYPosition(ds) {
        let xPoint;
        let yPoint;
        if (snapX) {
            xPoint = $xScale.invert(ds.offsetX - $padding.left);
        } else {
            xPoint = $xScale.invert(ds.offsetX - $padding.left);
        }
        if (snapY) {
            yPoint = $yScale.invert(ds.offsetY - $padding.top);
            const idx = nearestIndex(yValues, yPoint);
            yPoint = yValues[idx];
        } else {
            yPoint = $yScale.invert(ds.offsetY - $padding.top);
        }
        position = { x: xPoint, y: yPoint };
    }

    function handleClick() {
        return function handleClickFn(e) {
            dispatch("click", { e, props: position });
        };
    }

    function nullPosition() {
        position = { x: null, y: null };
    }
</script>

<!--<g >-->
<rect
    class="ring-0 focus:ring-0 border-0 focus:border-0 focus:outline-none"
    x={0}
    y={0}
    height={$height}
    width={$width}
    fill={"#FFF"}
    fill-opacity="0"
    stroke="none"
    on:mouseenter={(e) => {
        setXYPosition(e);
    }}
    on:focus={(e) => {
        setXYPosition(e);
    }}
    on:mousemove={(e) => {
        setXYPosition(e);
        dispatch("mousemove", { e, props: position });
    }}
    on:click={(e) => {
        setXYPosition(e);
        dispatch("click", { e, props: position });
    }}
    on:mouseleave={(e) => {
        nullPosition();
        dispatch("mouseout", { e, props: position });
    }}
    on:blur={nullPosition}>
</rect>
<!--</g>-->
