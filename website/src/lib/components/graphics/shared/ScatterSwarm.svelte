<!--
  @component
  Generates an SVG line shape using the `line` function from [d3-shape](https://github.com/d3/d3-shape).
 -->
<script>
    // import { run } from "svelte/legacy";

    import { createEventDispatcher, getContext, untrack } from "svelte";
    import { forceSimulation, forceX, forceY, forceCollide } from "d3-force";

    const { data, height, xScale, xGet, x, yScale, width } = getContext("LayerCake");

    /**
     * @typedef {Object} Props
     * @property {number} [r]
     * @property {number} [xStrength]
     * @property {number} [yStrength]
     * @property {any} colors
     */

    /** @type {Props} */
    let { r = 4, xStrength = 0.95, yStrength = 0.075, colors } = $props();

    const dispatch = createEventDispatcher();
    let nodes = $state([]);

    let simulation = $derived.by(() => {
        if (!$width || !$height || !$data.length) return null;
        // make a copy of the data for mutation
        const sim = forceSimulation($data.map((/** @type {any} */ d) => ({ ...d })))
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

        return sim;
    });

    $effect(() => {
        if (!simulation) {
            nodes = [];
            // console.log("no simulation, returning");
            return;
        }

        untrack(() => {
            // Run the simulation for a fixed number of iterations
            const maxIterations = Math.ceil(Math.log(simulation.alphaMin()) / Math.log(1 - simulation.alphaDecay()));

            for (let i = 0; i < maxIterations; ++i) {
                simulation.tick();
            }
            // Update nodes state to trigger reactivity
            nodes = [...simulation.nodes()];
            // console.log("updating nodes", nodes);

        });
    });


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
    {#each nodes as ds}
        <circle
            cx={ds.x}
            cy={ds.y}
            {r}
            fill={colors(ds.instrument)}
            stroke="none"
            onmouseover={(e) => dispatch("mousemove", { e, props: ds })}
            onfocus={(e) => dispatch("mousemove", { e, props: ds })}
            onmousemove={handleMousemove(ds)}
            onclick={handleClick(ds)}></circle>
    {/each}
</g>
