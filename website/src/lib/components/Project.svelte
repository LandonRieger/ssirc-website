<script>
    import { Badge } from "flowbite-svelte";

    // import { render } from "svelte/server";
    let { title, leads, ongoing = false, newproject = false, children = undefined } = $props();
</script>

<div class="font-bold text-lg">
    {title}{#if ongoing}<Badge border rounded color="green" class="ml-4">ONGOING</Badge>{/if}
    {#if newproject}<Badge border rounded color="green" class="ml-4">NEW</Badge>{/if}
</div>
<div class="flex flex-row space-x-4">
    {#each leads as lead}
        <div class="italic font-bold text-sm">{lead}</div>
    {/each}
</div>
<!-- <div class="content"> -->
{#if children}
    <div class="pb-4 space-y-2 hyphens-auto text-justify">
        {@render children()}
    </div>
{/if}
<!-- </div> -->
