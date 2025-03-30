<script>
    import { Indicator } from "flowbite-svelte";

    let { data, select, colors } = $props();
    let selectedInstrument = $state(undefined);

    const uniqueInstruments = $derived(data ? [...new Set(data.map((x) => x.instrument))] : []);
    const instruments = $derived(
        [{ name: "All instruments", value: undefined }].concat(uniqueInstruments.map((x) => ({ name: x, value: x }))),
    );
    const activeClass = "bg-gray-100";
</script>

<div class="flex flex-col grow ml-8">
    <div>Click on an instrument to filter results</div>

    <div class="grid grid-cols-1">
        {#each instruments as inst}
            <div
                role="button"
                class={`justify-left px-4 py-2 hover:font-bold ${selectedInstrument === inst.value ? activeClass : ""}`}
                onclick={() => {
                    selectedInstrument = inst.value;
                    select(inst.value);
                }}>
                <div class="flex">
                    <div class="content-center">
                        <svg viewBox="0 0 20 20" width="20" height="20" xmlns="http://www.w3.org/2000/svg"
                            ><circle cx="10" cy="10" r={7} fill={inst.value ? colors(inst.value) : "#444"} /></svg>
                    </div>
                    <div class="ml-4 leading-none text-gray-800">
                        {inst.name}
                    </div>
                </div>
            </div>
        {/each}
    </div>
</div>
