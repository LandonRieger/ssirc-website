<script>
    // import { render } from "svelte/server";
    let { title, leads, children } = $props();
</script>

<div class="font-bold text-lg">{title}</div>
<div class="flex flex-row space-x-4">
    {#each leads as lead}
        <div class="italic font-bold text-sm">{lead}</div>
    {/each}
</div>
<!-- <div class="content"> -->
 <div class="pb-4">
{@render children()}
</div>
<!-- </div> -->
