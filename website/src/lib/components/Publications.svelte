<script>
    import BibEntry from "$lib/components/BibEntry.svelte";
    import bibEntries from "./../bib/new_bibfile.bib?raw";
    import { parseBibEntries, groupBibEntriesByYear } from "$lib/readBib.js";
    import { Input, Label, Helper, Button, Listgroup } from "flowbite-svelte";
    import { SearchOutline } from "flowbite-svelte-icons";

    let search;
    let allEntries = parseBibEntries(bibEntries);
    $: filteredEntries = search ? allEntries.filter((x) => x.title.toLowerCase().includes(search)) : allEntries;
    $: entries = groupBibEntriesByYear(filteredEntries);
    $: uniqueYears = filteredEntries.length > 0 ? Object.keys(entries).sort((a, b) => Number(b) - Number(a)) : [2021];
    $: links = uniqueYears.map((x) => {
        return { name: x, href: `#${x}` };
    });
</script>

<div class="flex w-full flex-row">
    <div class="flex-none hidden w-64 lg:text-sm lg:block end-0">
        <div class="flex overflow-y-auto sticky top-20 flex-col justify-between pb-6 mr-6 h-[calc(100vh-5rem)]">
            <div>
                <p class="uppercase font-medium text-gray-700 mb-4">On this page</p>

                <Listgroup active items={links} let:item>
                    {item.name}
                </Listgroup>
            </div>
        </div>
    </div>
    <div class="flex flex-col w-full">
        <h1>Publications</h1>

        <div class="w-full py-4">
            <Input id="search" placeholder="Search" bind:value={search}>
                <SearchOutline slot="left" class="w-6 h-6 text-gray-500 dark:text-gray-400" />
            </Input>
        </div>

        <!--{#each Object.entries(entries) as [year, yearlyEntries]}-->
        {#if filteredEntries.length === 0}
            <div class="text-center font-bold text-lg">
                No Papers Found
            </div>
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
