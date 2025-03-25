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
</script>

<Table striped={false} hoverable={true}>
    <TableHead>
        <TableHeadCell sort={(a, b) => a["record start date"] - b["record start date"]}>Duration</TableHeadCell>
        <TableHeadCell>Ongoing</TableHeadCell>
        <TableHeadCell sort={(a, b) => a["Instrument"].localeCompare(b["Instrument"])}>Instrument</TableHeadCell>
        <TableHeadCell>Latitude</TableHeadCell>
        <TableHeadCell>Longitude</TableHeadCell>
        <TableHeadCell>Location</TableHeadCell>
    </TableHead>
    <TableBody tableBodyClass="divide-y">
        {#each data as row, i}
            <TableBodyRow on:click={() => toggleRow(i)}>
                <TableBodyCell
                    >{new Date(row["record start date"]).toLocaleDateString("en-US", options)}
                    <span class=" font-light text-gray-600">to</span>
                    {new Date(row["record end date"]).toLocaleDateString("en-US", options)}</TableBodyCell>
                <TableBodyCell><Indicator color={row["Ongoing"] ? "green" : "red"}></Indicator></TableBodyCell>
                {#each headers as key}
                    <TableBodyCell
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
