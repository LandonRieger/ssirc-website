<script>
    import {
        Table,
        TableBody,
        TableBodyCell,
        TableBodyRow,
        TableHead,
        TableHeadCell,
        Indicator,
        Card,
    } from "flowbite-svelte";
    import { slide } from "svelte/transition";
    import CampaignDetail from "$lib/components/CampaignDetail.svelte";
    import SortableCellHeader from "$lib/components/util/SortableCellHeader.svelte";
    import { onMount } from "svelte";

    export let data;

    let headers = ["Instrument", "Latitude", "Longitude", "Campaign Base"];
    let openRow;
    let sortBy = { col: "record start date", ascending: true };
    const toggleRow = (i) => {
        openRow = openRow === i ? null : i;
    };

    const options = {
        year: "numeric",
        month: "short",
    };

    const cellClass = "p-2";

    $: sort = (column, ascending = null) => {
        if (ascending !== null) {
            sortBy.ascending = ascending;
        } else if (sortBy.col === column) {
            sortBy.ascending = !sortBy.ascending;
        } else {
            sortBy.col = column;
            sortBy.ascending = true;
        }

        // Modifier to sorting function for ascending or descending
        const sortModifier = sortBy.ascending ? 1 : -1;
        // const sort = ;
        data = data.sort((a, b) =>
            a[column] < b[column] ? -1 * sortModifier : a[column] > b[column] ? 1 * sortModifier : 0,
        );
    };

    onMount(() => sort("record end date", false));

</script>


    <Table striped={false} hoverable={true}>
        <TableHead>
            <!--            <TableHeadCell class="px-2" on:click={() => sort("record start date")}-->
            <!--                ><SortableCellHeader name="Duration" sortName={"record start date"} {sortBy} /></TableHeadCell>-->
            <TableHeadCell class="px-2" on:click={() => sort("record start date")}>
                <SortableCellHeader name="Start" sortName={"record start date"} {sortBy} />
            </TableHeadCell>
            <TableHeadCell class="px-2" on:click={() => sort("record end date")}>
                <SortableCellHeader name="End" sortName={"record end date"} {sortBy} />
            </TableHeadCell>
            <TableHeadCell class="px-2" on:click={() => sort("Number of Flights")}>
                <SortableCellHeader name="Flights" sortName={"Number of Flights"} {sortBy} />
            </TableHeadCell>
            <TableHeadCell class="text-center px-2" on:click={() => sort("Ongoing")}
                ><SortableCellHeader name="Ongoing" sortName={"Ongoing"} {sortBy} /></TableHeadCell>
            <TableHeadCell class="px-2" on:click={() => sort("Instrument")}
                ><SortableCellHeader name="Instrument" sortName={"Instrument"} {sortBy} /></TableHeadCell>
            <TableHeadCell class="px-2" on:click={() => sort("Latitude")}
                ><SortableCellHeader name="Latitude" sortName={"Latitude"} {sortBy} /></TableHeadCell>
            <TableHeadCell class="px-2" on:click={() => sort("Longitude")}
                ><SortableCellHeader name="Longitude" sortName={"Longitude"} {sortBy} /></TableHeadCell>
            <TableHeadCell class="px-2" on:click={() => sort("Campaign Base")}
                ><SortableCellHeader name="Location" sortName={"Campaign Base"} {sortBy} /></TableHeadCell>
        </TableHead>
        <TableBody tableBodyClass="divide-y">
            {#each data as row, i}
                <TableBodyRow on:click={() => toggleRow(i)}>
                    <!--                    <TableBodyCell class={cellClass}-->
                    <!--                        >{new Date(row["record start date"]).toLocaleDateString("en-US", options)}-->
                    <!--                        <span class=" font-light text-gray-600">to</span>-->
                    <!--                        {new Date(row["record end date"]).toLocaleDateString("en-US", options)}</TableBodyCell>-->
                    <TableBodyCell class={cellClass}
                        >{new Date(row["record start date"]).toLocaleDateString("en-US", options)}</TableBodyCell>
                    <TableBodyCell class={cellClass}
                        >{row["Ongoing"]
                            ? "-"
                            : new Date(row["record end date"]).toLocaleDateString("en-US", options)}</TableBodyCell>
                    <TableBodyCell class={cellClass}>{row["Number of Flights"]}</TableBodyCell>
                    <TableBodyCell class={`flex ${cellClass} justify-center`}
                        ><Indicator color={row["Ongoing"] ? "green" : "red"}></Indicator></TableBodyCell>
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
                        <TableBodyCell colspan="8" class="p-0">
                            <div transition:slide={{ duration: 300, axis: "y" }}>
                                <CampaignDetail data={row} />
                            </div>
                        </TableBodyCell>
                    </TableBodyRow>
                {/if}
            {/each}
        </TableBody>
    </Table>
