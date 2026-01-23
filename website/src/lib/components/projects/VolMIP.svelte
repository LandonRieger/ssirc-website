<script>
    import Project from "$lib/components/projects/Project.svelte";
    import Link from "$lib/components/Link.svelte";
    let { refs } = $props();
</script>

<Project title={"Model Intercomparison Project on the climatic response to Volcanic forcing (VolMIP)"} leads={[]}>
    {#snippet children()}
        <div id="volres">
            <Link href="www.volmip.org">VolMIP</Link> is a protocol-driven international project aiming at coordinating the
            activities of different Research Institutes involved in numerical climate modelling focused on a multi-model
            assessment of climate models' performance under strong volcanic forcing conditions.
        </div>
    {/snippet}
</Project>
