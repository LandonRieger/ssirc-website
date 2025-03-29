<script>
    import { LayerCake, Svg, Html, Canvas } from "layercake";
    // import MapTilesCanvas from './MapTiles.canvas.svelte';
    // import MapTilesCanvas from "$lib/components/graphics/balloon/MapTiles.canvas.svelte";
    import Features from "$lib/components/graphics/balloon/Features.svelte";
    import MapScatter from "$lib/components/graphics/balloon/MapScatter.svelte";
    // import ColormapSelector from '../base/ColormapSelector.svelte';
    // import { scaleSequential, scaleSequentialLog, scaleLinear, scaleLog } from "d3-scale";
    import { onMount, createEventDispatcher } from "svelte";
    // import { config } from '$lib/config.js';
    import { feature } from "topojson-client";
    // import RegionSelector from './RegionSelector.svelte';
    import { timer } from "d3-timer";
    import { geoOrthographic, geoNaturalEarth1, geoEquirectangular } from "d3-geo";
    import { schemeCategory10, schemeTableau10 } from "d3-scale-chromatic";
    const colors = [schemeTableau10[0], schemeTableau10[1], schemeTableau10[2], schemeTableau10[4], schemeTableau10[5]]

    // import { Toggle, Range, Label } from "flowbite-svelte";
    // import { interpolateRdBu, interpolateSpectral } from "d3-scale-chromatic";

    export let data;
    export let colorDomain;

    $: points = data ? data.map((x) => ({...x, loc: [x.longitude, x.latitude]})) : [];
    // export let attrs = undefined;

    const dispatch = createEventDispatcher();
    let extent = { type: "Sphere" };
    let land;
    let rotate = [0, 0, 0];
    let mapMode = "zoom";

    function extract_variable(attr, varname) {
        if (attr[varname] !== undefined) {
            return attr[varname];
        }
        if (Array.isArray(attr)) {
            if (attr[0][varname] !== undefined) {
                return attr[0][varname];
            }
            return;
        }
        return;
    }

    let projection = geoEquirectangular;
    $: projection === geoOrthographic ? rotation_timer.restart(rotateGlobe) : stop_timer();

    $: flatData = [
        { latitude: -90, longitude: 0 },
        { latitude: 90, longitude: 360 },
    ];

    function stop_timer() {
        rotation_timer.stop();
        rotate = [0, 0, 0];
    }

    function rotateGlobe(elapsed) {
        rotate = [0.005 * elapsed, -0.002 * elapsed, 0.001 * elapsed];
    }

    function selectRegion(d) {
        console.log("select region", d.detail);
        if (mapMode === "zoom") {
            if (d.detail.bounds) {
                extent = {
                    type: "Feature",
                    geometry: { type: "MultiPoint", coordinates: d.detail.bounds },
                };
            } else {
                extent = { type: "Sphere" };
            }
            console.log("new extent", extent);
        } else {
            dispatch("regionchange", { d, props: { bounds: d.detail.bounds } });
        }
    }

    const rotation_timer = timer(rotateGlobe);

    onMount(async () => {
        const res = await fetch(`http://127.0.0.1:8000/api/map/countries`);
        const countries = await res.json();
        land = feature(countries, countries.objects.land);
    });
</script>

<!-- <div class="flex flex-row gap-4"> -->
<div class="grow">
    {#if land}
        <div class="chart-container">
            <LayerCake
                padding={{ top: 20, right: 60, bottom: 0, left: 0 }}
                x={"longitude"}
                y={"latitude"}
                data={flatData}>
                <Svg>
                    <Features
                        features={[{ type: "Sphere" }]}
                        {projection}
                        {extent}
                        {rotate}
                        strokeWidth={2}
                        stroke={"#444"} />
                    <Features features={land.features} {projection} {extent} {rotate} fill={"#DDDDDD"} stroke={"#000"} />
                    <MapScatter {projection} {extent} {rotate} r={4} colorScale={colors} {colorDomain} features={points} />
                </Svg>
            </LayerCake>
        </div>
    {/if}
    <!-- {/each} -->
</div>

<!-- </div> -->

<style>
    /*
      The wrapper div needs to have an explicit width and height in CSS.
      It can also be a flexbox child or CSS grid element.
      The point being it needs dimensions since the <LayerCake> element will
      expand to fill it.
    */
    .chart-container {
        width: 100%;
        height: 300px;
    }
    /* .axis-title {
        transform: translate(0%, -100%);
    } */
</style>
