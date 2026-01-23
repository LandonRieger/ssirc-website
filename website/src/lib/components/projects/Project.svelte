<script>
    import { Badge } from "flowbite-svelte";

    // import { render } from "svelte/server";
    let { title, leads, ongoing = false, newproject = false, children = undefined } = $props();
</script>

<div>
    <div class="flex align-middle">
        <div class="font-bold text-lg">
            {title}
        </div>
        {#if ongoing}
            <div class="flex-none">
                <Badge size="sm" border color="green" class="ml-2">ONGOING</Badge>
            </div>
        {/if}
        {#if newproject}
            <div class="flex-none">
                <Badge size="sm" border color="green" class="ml-2">NEW</Badge>
            </div>
        {/if}
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
</div>
