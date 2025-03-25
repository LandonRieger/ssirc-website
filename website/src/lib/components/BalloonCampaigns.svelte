<script>
    import {
        Table,
        TableBody,
        TableBodyCell,
        TableBodyRow,
        TableHead,
        TableHeadCell,
        Modal,
        ImagePlaceholder,
        Indicator,
        Card
    } from "flowbite-svelte";
    import { slide } from "svelte/transition";
    import CampaignDetail from "$lib/components/CampaignDetail.svelte";

    export let data;

    let headers = ["Instrument", "Latitude", "Longitude", "Campaign Base"];
    let openRow;
    const toggleRow = (i) => {
        openRow = openRow === i ? null : i;
    };

    const options = {
        year: "numeric",
        month: "short",
    };

    const cellClass = "p-2"
</script>

<Card size="xl">
    <div class="pb-4">Click on a row to see more detailed information about a campaign.</div>
<Table striped={false} hoverable={true}>
    <TableHead>
        <TableHeadCell class="px-2" sort={(a, b) => a["record start date"] - b["record start date"]}>Duration</TableHeadCell>
        <TableHeadCell class="text-center px-2" >Ongoing</TableHeadCell>
        <TableHeadCell class="px-2" sort={(a, b) => a["Instrument"].localeCompare(b["Instrument"])}>Instrument</TableHeadCell>
        <TableHeadCell class="px-2">Latitude</TableHeadCell>
        <TableHeadCell class="px-2">Longitude</TableHeadCell>
        <TableHeadCell class="px-2">Location</TableHeadCell>
    </TableHead>
    <TableBody tableBodyClass="divide-y">
        {#each data as row, i}
            <TableBodyRow on:click={() => toggleRow(i)}>
                <TableBodyCell class={cellClass}
                    >{new Date(row["record start date"]).toLocaleDateString("en-US", options)}
                    <span class=" font-light text-gray-600">to</span>
                    {new Date(row["record end date"]).toLocaleDateString("en-US", options)}</TableBodyCell>
                <TableBodyCell class={`flex ${cellClass} justify-center`}><Indicator color={row["Ongoing"] ? "green" : "red"}></Indicator></TableBodyCell>
                {#each headers as key}
                    <TableBodyCell class={cellClass}
                        >{row[key]
                            ? typeof row[key] === "string" && row[key].length > 30
                                ? `${row[key].slice(0, 27)}...`
                                : row[key]
                            : ""}</TableBodyCell>
                {/each}
            </TableBodyRow>
            {#if openRow === i}
                <TableBodyRow>
                    <TableBodyCell colspan="6" class="p-0">
                        <div transition:slide={{ duration: 300, axis: "y" }}>
                            <CampaignDetail data={row} />
                        </div>
                    </TableBodyCell>
                </TableBodyRow>
            {/if}
        {/each}
    </TableBody>
</Table>
</Card>