<script>
    import { LayerCake, Svg, Html } from "layercake";
    import Features from "$lib/components/graphics/balloon/Features.svelte";
    import MapScatter from "$lib/components/graphics/balloon/MapScatter.svelte";
    import { onMount } from "svelte";
    import { feature } from "topojson-client";
    import { geoOrthographic, geoNaturalEarth1, geoEquirectangular, geoEqualEarth} from "d3-geo";
    import Tooltip from "$lib/components/graphics/shared/Tooltip.svelte";

    let { data, click, colors } = $props();
    let location = $state(undefined);
    let evt = $state(undefined);
    let points = $derived(data ? data.map((x) => ({ ...x, loc: [x.longitude, x.latitude] })) : []);

    let extent = { type: "Sphere" };
    let land = $state(undefined);
    let rotate = [0, 0, 0];

    let projection = geoEquirectangular;
    let flatData = [
        { latitude: -90, longitude: 0 },
        { latitude: 90, longitude: 360 },
    ];

    onMount(async () => {
        const res = await fetch(`http://127.0.0.1:8000/api/map/countries`);
        const countries = await res.json();
        land = feature(countries, countries.objects.land);
    });
</script>

<div class="grid grid-cols-1 w-[600px]">
<div>
    Click on a location to filter results
</div>
<div class="grow">
    {#if land}
        <div class="chart-container">
            <LayerCake
                padding={{ top: 0, right: 0, bottom: 0, left: 0 }}
                x={"longitude"}
                y={"latitude"}
                data={flatData}>
                <Svg>

                    <Features
                        features={land.features}
                        {projection}
                        {extent}
                        {rotate}
                        fillOpacity={1}
                        fill={"#DDD"}
                        stroke={"#DDD"} />
                    <Features
                        features={[{ type: "Sphere" }]}
                        {projection}
                        {extent}
                        {rotate}
                        strokeWidth={1}
                        stroke={"#DDD"} />
                    <MapScatter
                        {projection}
                        {extent}
                        {rotate}
                        r={4}
                        {colors}
                        features={points}
                        mouseover={(h) => {
                            location = h.location;
                            evt = h.evt;
                        }}
                        mouseout={(h) => {
                            location = h.location;
                            evt = h.evt;
                        }}
                        {click} />
                </Svg>
                <Html pointerEvents={false}>
                    {#if location}
                        <Tooltip evt={{ detail: { e: evt } }} xoffset={-50} --width="auto">
                            <div class="key-name mb-2">
                                {location}
                            </div>
                            <hr />
                            <div>{`${data.filter((x) => x.location === location).length} flights`}</div>
                        </Tooltip>
                    {/if}
                </Html>
            </LayerCake>
        </div>
    {/if}
    <!-- {/each} -->
</div>

 </div>

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
