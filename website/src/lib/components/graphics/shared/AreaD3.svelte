<script>
    import { run } from 'svelte/legacy';

    import { createEventDispatcher, getContext } from "svelte";
    import { area, line, curveLinear, curveCardinal } from "d3-shape";
    import { nearestIndex } from "$lib/utils.js";

    const { data, yScale, xScale, xDomain, yDomain, width, height, padding, y, x } = getContext("LayerCake");
    const clipUuid = `clip-ND`;
    const clipUrl = `url(#${clipUuid})`;
    const dispatch = createEventDispatcher();

    /**
     * @typedef {Object} Props
     * @property {any} [curve]
     * @property {string} [color]
     * @property {number} [idx]
     */

    /** @type {Props} */
    let { curve = curveLinear, color = "#97C555", idx = 0 } = $props();

    let fitCurve = $state();
    let fitCurveZero = $state();

    let yValues = $derived($data.map((d) => $y(d)));

    run(() => {
        fitCurve = area()
            .x0((d) => $xScale(d.concentration[idx]))
            .x1((d) => (idx < d.concentration.length - 1 ? $xScale(d.concentration[idx + 1]) : $xScale($xDomain[0])))
            .y((d) => $yScale(d.altitude))
            .curve(curve);
        fitCurveZero = area()
            .x0((d) => $xScale(d.concentration[idx]))
            .x1((d) => $xScale($xDomain[0]))
            .y((d) => $yScale(d.altitude))
            .curve(curve);
    });

    function handleMousemove(ds, glyph = "") {
        return function handleMousemoveFn(e) {
            // raise(this);
            // When the element gets raised, it flashes 0,0 for a second so skip that
            if (e.layerX !== 0 && e.layerY !== 0) {
                // dispatch(`mousemove${glyph}`, { e, props: ds });
                dispatch("mousemove", { e, props: {"idx": idx, "data": getXYPosition(e) }})
            }
        };
    }

    function getXYPosition(ds) {
        let xPoint;
        let yPoint;
        yPoint = $yScale.invert(ds.offsetY - $padding.top);
        const idx = nearestIndex(yValues, yPoint);
        yPoint = yValues[idx];
        xPoint = $x($data[idx]);
        return { "x": xPoint, "y": yPoint };
    }
</script>

<clipPath id={clipUuid}>
    <rect x="0" y="0" width={$width} height={$height}></rect>
</clipPath>

<g role="tooltip" onmouseout={(e) => dispatch("mouseout")} onblur={(e) => dispatch("mouseout")}>
    <path
        class="opacity-0 hover:opacity-100"
        d={fitCurveZero($data)}
        stroke={"none"}
        stroke-width="2"
        fill={color}
        clip-path={clipUrl}
        onmouseover={(e) => dispatch("mousemove", { e, props: {"idx": idx, "data": getXYPosition(e) }})}
        onfocus={(e) => dispatch("mousemove", { e, props: {"idx": idx, "data": getXYPosition(e) }})}
        onmousemove={handleMousemove(idx)} />
    <path
        class="opacity-80 pointer-events-none"
        d={fitCurve($data)}
        stroke={"none"}
        stroke-width="2"
        fill={color}
        clip-path={clipUrl} />
</g>
