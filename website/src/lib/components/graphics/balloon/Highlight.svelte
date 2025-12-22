<script>
    import { createEventDispatcher, getContext } from "svelte";
    import { nearestIndex } from "$lib/utils.js";

    const { data, width, height, xScale, padding, yScale, yGet, y } = getContext("LayerCake");

    const dispatch = createEventDispatcher();

    /**
     * @typedef {Object} Props
     * @property {any} position
     * @property {boolean} [snapY]
     * @property {boolean} [snapX]
     */

    /** @type {Props} */
    let { position = $bindable(), snapY = false, snapX = false } = $props();

    let yValues = $derived($data.map((d) => $y(d)));
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
    onmouseenter={(e) => {
        setXYPosition(e);
    }}
    onfocus={(e) => {
        setXYPosition(e);
    }}
    onmousemove={(e) => {
        setXYPosition(e);
        dispatch("mousemove", { e, props: position });
    }}
    onclick={(e) => {
        setXYPosition(e);
        dispatch("click", { e, props: position });
    }}
    onmouseleave={(e) => {
        nullPosition();
        dispatch("mouseout", { e, props: position });
    }}
    onblur={nullPosition}>
</rect>
<!--</g>-->
