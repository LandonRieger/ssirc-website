<script>
    let { entry, max_authors = 5, id = undefined, format = "long" } = $props();

    if (!id) {
        id = entry.title;
    }

    function abbreviate(sentence) {
        return sentence
            .trim()
            .split(/\s+/u) // split on whitespace (Unicode-safe)
            .map((word) =>
                word
                    .split("-")
                    .map((part) => {
                        const match = part.match(/\p{L}/u); // first Unicode letter
                        return match ? match[0].toUpperCase() + "." : "";
                    })
                    .join("-"),
            )
            .join(" ");
    }

    function format_name(author) {
        try {
            if (author.name) {
                return `${author.prefix} ${author.name}, ${author["given-name"]}`;
            } else {
                let names = author.split(",");
                let last = names[0];
                let first = names[1].split(" ");
                if (first.length === 1) {
                    first = `${first[0][0]}.`;
                } else {
                    try {
                        first = abbreviate(names[1]);
                    } catch {
                        first = ``;
                    }
                }
                return `${last}, ${first}`;
            }
        } catch {
            console.log("could not format author ", author);
        }
    }
    const title_class = "text-sm font-semibold text-gray-800";
    let inline = $derived(format === "long" ? "block" : "inline");
</script>

{#if entry.title}
    <div {id} class={format !== "long" ? "leading-none " : ""}>
        <div class={["font-normal text-sm text-gray-800", inline]}>
            {#each entry.author as author, idx}
                {#if idx == max_authors}
                    {"et. al."}
                {:else if idx > max_authors}{:else}
                    {format_name(author)}
                    {#if idx != entry.author.length - 1}{/if}
                {/if}
            {/each}
        </div>
        <div class={[title_class, inline]}>
            {@html entry.title}
        </div>
        <div class={["text-sm text-gray-600", inline]}>
            {#if entry.parent}
                {entry.parent.title},
            {/if}
            {#if entry["serial-number"] && entry["serial-number"].doi}
                <a class="text-blue-700" href={`https://doi.org/${entry["serial-number"].doi}`}
                    >{entry["serial-number"].doi.replace("https://doi.org/", "")}</a
                >,
            {/if}
            {entry.date}
        </div>
    </div>
{/if}
