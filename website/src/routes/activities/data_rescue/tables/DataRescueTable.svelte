<script lang="ts">
    import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Popover } from "flowbite-svelte";
    import BibEntry from "$lib/components/BibEntry.svelte";

    let { data, refs } = $props();
    const fontsize = "text-xs";
</script>

<!--<h3>Early Post-Pinatubo datasets</h3>-->
<Table shadow={true}>
    <TableHead class="bg-amber-900 text-white">
        <TableHeadCell>Type</TableHeadCell>
        <TableHeadCell>PI</TableHeadCell>
        <TableHeadCell>Period and coverage</TableHeadCell>
        <TableHeadCell class="w-64">References</TableHeadCell>
    </TableHead>
    <TableBody>
        {#each data.campaigns as campaign}
            <TableBodyRow>
                <TableHeadCell colspan={4} class="bg-amber-700 text-white p-2">{campaign.title}</TableHeadCell>
            </TableBodyRow>
            {#each campaign.data as row}
                <TableBodyRow>
                    <TableBodyCell class="whitespace-normal px-3 py-2 text-gray-900 {fontsize}">
                        <div class="space-y-1">
                            {#each row.instrument as inst}
                                <div>{inst}</div>
                            {/each}
                        </div></TableBodyCell>
                    <TableBodyCell class="whitespace-normal w-48 px-3 py-2 text-gray-900 {fontsize}"
                        >{row.pi}</TableBodyCell>
                    <TableBodyCell class="whitespace-normal px-3 py-2 text-gray-900 {fontsize}">
                        {#each row.periods as date}
                            <div>{date}</div>
                        {/each}
                    </TableBodyCell>
                    <TableBodyCell class="whitespace-normal w-52 px-3 py-2 text-gray-900 {fontsize}">
                        {#each row.references as ref}
                            <div>
                                <button id={ref}>{@html refs.citet(ref)}</button>
                                <Popover triggeredBy={`#${ref}`} class="max-w-96 flex flex-grow" title={undefined}
                                    ><BibEntry entry={refs.entries[ref]}></BibEntry></Popover>
                            </div>
                        {/each}
                    </TableBodyCell>
                </TableBodyRow>
            {/each}
        {/each}
    </TableBody>
</Table>
