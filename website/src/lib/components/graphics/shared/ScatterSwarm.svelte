<!--
  @component
  Generates an SVG line shape using the `line` function from [d3-shape](https://github.com/d3/d3-shape).
 -->
<script>
    import { createEventDispatcher, getContext } from "svelte";
    import { scaleOrdinal } from "d3-scale";
    import { schemeCategory10 } from "d3-scale-chromatic";
    import { forceSimulation, forceX, forceY, forceCollide } from "d3-force";

    const { data, height, xScale, xGet, x, yScale } = getContext("LayerCake");

    export let colorDomain = [...new Set($data.map((x) => x.instrument))];
    export let r = 4;
    export let xStrength = 0.95;
    export let yStrength = 0.075;

    const dispatch = createEventDispatcher();

    $: nodes = $data.map((d) => ({ ...d }));
    $: color = scaleOrdinal(colorDomain, schemeCategory10);
    $: simulation = forceSimulation(nodes)
        .force(
            "x",
            forceX()
                .x((d) => $xGet(d))
                .strength(xStrength),
        )
        .force(
            "y",
            forceY()
                .y($height / 2)
                .strength(yStrength),
        )
        .force("collide", forceCollide(r))
        .stop();

    $: {
        for (
            let i = 0, n = Math.ceil(Math.log(simulation.alphaMin()) / Math.log(1 - simulation.alphaDecay()));
            i < n;
            ++i
        ) {
            simulation.tick();
        }
    }

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

<g role="tooltip" on:mouseout={(e) => dispatch("mouseout")} on:blur={(e) => dispatch("mouseout")}>
    {#each simulation.nodes() as ds}
        <circle
            cx={ds.x}
            cy={ds.y}
            {r}
            fill={color(ds.instrument)}
            stroke="none"
            on:mouseover={(e) => dispatch("mousemove", { e, props: ds })}
            on:focus={(e) => dispatch("mousemove", { e, props: ds })}
            on:mousemove={handleMousemove(ds)}
            on:click={handleClick(ds)}></circle>
    {/each}
</g>
