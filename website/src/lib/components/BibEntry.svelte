<script>
    export let entry;
</script>

{#if entry.title}
    <div>
        <div class="text-sm font-semibold">
            {@html entry.title}
        </div>
        <div class="font-normal text-sm">
            {entry.author}
        </div>
        <div class="text-sm text-gray-600">
            {entry.journal}, <a class="text-blue-600" href={`https://doi.org/${entry.doi}`}>{entry.doi}</a>, {entry.year}
        </div>
    </div>
{/if}
