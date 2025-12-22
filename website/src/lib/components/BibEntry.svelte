<script>
    let { entry } = $props();
</script>

{#if entry.title}
    <div>
        <div class="text-sm font-semibold">
            {@html entry.title}
        </div>
        <div class="font-normal text-sm">
            {#each entry.author as author, idx}
                {#if author.name}
                    {author.prefix} {author.name}, {author["given-name"]}
                {:else}
                    {@html author}
                {/if}
                {#if idx != entry.author.length - 1}&nbsp{/if}
            {/each}
        </div>
        <div class="text-sm text-gray-600">
            {entry.parent.title},
            {#if entry["serial-number"] && entry["serial-number"].doi}
                <a class="text-blue-700" href={`https://doi.org/${entry["serial-number"].doi}`}
                    >{entry["serial-number"].doi}</a
                >,
            {/if}
            {entry.date}
        </div>
    </div>
{/if}
