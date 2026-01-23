<script>
    import BibEntry from "$lib/components/BibEntry.svelte";
    import bibEntries from "./../bib/references.yaml?raw";
    import { parse, stringify } from "yaml";
    import { groupBibEntriesByYear } from "$lib/readBib.js";
    import { Input, Label, Helper, Button } from "flowbite-svelte";
    import { SearchOutline } from "flowbite-svelte-icons";
    import ListGroup from "$lib/components/ListGroup.svelte";
    let allEntries = Object.values(parse(bibEntries));
    let search = $state();

    let filteredEntries = $derived(
        search ? allEntries.filter((x) => x.title.toLowerCase().includes(search)) : allEntries,
    );
    let entries = $derived(groupBibEntriesByYear(filteredEntries));
    let uniqueYears = $derived(
        filteredEntries.length > 0 ? Object.keys(entries).sort((a, b) => Number(b) - Number(a)) : [2021],
    );
    let links = $derived(
        uniqueYears.map((x) => {
            return { label: x, id: `${x}` };
        }),
    );
</script>

<div class="flex w-full flex-row">
    <div class="w-64 flex-none">
        <ListGroup {links}></ListGroup>
    </div>
    <div class="flex flex-col w-full">
        <h1>Publications</h1>

        <div class="w-full py-4">
            <Input id="search" placeholder="Search" bind:value={search}>
                {#snippet right()}
                    <SearchOutline class="w-6 h-6 text-gray-500 dark:text-gray-400" />
                {/snippet}
            </Input>
        </div>

        <!--{#each Object.entries(entries) as [year, yearlyEntries]}-->
        {#if filteredEntries.length === 0}
            <div class="text-center font-bold text-lg">No Papers Found</div>
        {:else}
            {#each uniqueYears as year}
                <h2 id={year}>{year}</h2>
                {@const yearlyEntries = entries[year]}
                {#if yearlyEntries}
                    {#each yearlyEntries as entry}
                        <div class="pb-4">
                            <BibEntry {entry} />
                        </div>
                    {/each}
                {/if}
            {/each}
        {/if}
    </div>
</div>
