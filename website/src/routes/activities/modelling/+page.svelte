<script>
    import ISAMIP from "$lib/components/projects/ISAMIP.svelte";
    import VolMIP from "$lib/components/projects/VolMIP.svelte";
    // import HTHHMOC from "$lib/components/projects/HTHHMOC.svelte";
    import HTHH from "./HTHH.svelte";
    import { Bibliography } from "$lib/bib/state.svelte.ts";
    import { parse } from "yaml";
    import bibEntries from "$lib/bib/references.yaml?raw";
    import BibEntry from "$lib/components/BibEntry.svelte";
    let bib = parse(bibEntries);
    let refs = new Bibliography(bib);
</script>

<h1>Modeling Activities</h1>

<div class="space-y-4">
<VolMIP></VolMIP>
<ISAMIP {refs}></ISAMIP>
<HTHH {refs}></HTHH>
</div>

<h2>References</h2>
<div class="space-y-2">
    {#each refs.print() as item}
        <BibEntry entry={item.entry} id={item.id} format={"short"} />
    {/each}
</div>
