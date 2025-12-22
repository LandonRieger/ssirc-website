<script>
    let { name, location = undefined } = $props();
</script>

<div class="flex flex-row">
<div class="text-gray-600 text-sm font-bold">
    {name}
</div>
{#if location}
    <div class="pl-2 text-gray-500 text-xs font-light">
        {location}
    </div>
{/if}
</div>