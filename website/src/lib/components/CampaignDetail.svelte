<script>
    import { Button } from "flowbite-svelte";
    import EnvelopeOutline from "flowbite-svelte-icons/EnvelopeOutline.svelte";

    let { data } = $props();
    let detailHeaders = ["Additional Parameters", "Scientific Focus", "relevant publications (doi)", "comments"];
    let lat = $derived(data["Latitude"]);
    let latStr = $derived(lat < 0 ? `${Math.abs(lat)}&deg S` : `${lat}&deg N`);
    let lon = $derived(data["Longitude"]);
    let lonStr = $derived(lon < 0 ? `${Math.abs(lon)}&deg W` : `${lon}&deg E`);
</script>

<div class="p-6 bg-gray-50">
    <div class="text-2xl font-bold pb-4">
        {data["Number of Flights"]}
        <span class="font-light"
            >{data["Number of Flights"] == 1 ? "Flight" : "Flights"} {#if lat}[{@html latStr}, {@html lonStr}]{/if}</span>
    </div>

    <div class="grid grid-cols-2 gap-y-4">
        {#each detailHeaders as hKey}
            {#if data[hKey]}
                <div class="px-2">
                    <div class="font-bold text-lime-600 uppercase">
                        {hKey}
                    </div>
                    <div class="pl-4 text-normal font-normal text-gray-900 text-wrap">{data[hKey]}</div>
                </div>
            {/if}
        {/each}
        {#if data["Size Range start"]}
            <div class="px-2">
                <div class="font-bold text-lime-600 uppercase">Particle Size</div>
                <div class="pl-4 text-normal font-normal text-gray-900 text-wrap">
                    {data["Size Range start"]} - {data["Size Range end"]}&#181m
                </div>
            </div>
        {/if}
        {#if data["Altitude Range [km]"]}
            <div class="px-2">
                <div class="font-bold text-lime-600 uppercase">Altitude Range</div>
                <div class="pl-4 text-normal font-normal text-gray-900 text-wrap">
                    {data["Altitude Range [km]"]}km
                </div>
            </div>
        {/if}
    </div>
    <div class="my-4 bg-gray-200 h-[1px]"></div>

    <div class="flex flex-row justify-between">
        <div>
            <div class="font-bold text-lime-600 uppercase">PI Contact</div>
            {#each data["PI Contact"] as pi}
                <div class="pl-4 flex place-items-center">
                    <EnvelopeOutline class="w-4 h-4 font-light" />
                    <a class="pl-3 text-normal text-mono font-normal text-gray-900" href={`mailto:${pi}`}>{pi}</a>
                </div>
            {/each}
        </div>
        {#if data["Link to Data"].includes("http")}
            <a href={data["Link to Data"]}>
                <Button color="dark">Download Data</Button>
            </a>
        {/if}
    </div>
</div>
