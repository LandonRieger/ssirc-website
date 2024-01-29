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
            {entry.journal}, {#if entry.doi}<a class="text-blue-700" href={`https://doi.org/${entry.doi}`}
                    >{entry.doi}</a
                >,{/if}
            {entry.year}
        </div>
    </div>
{/if}
