<script>
    import Project from "$lib/components/projects/Project.svelte";
    import Link from "$lib/components/Link.svelte";
    let { refs } = $props()
</script>

<Project title={"COSANOVA"} leads={[""]} ongoing>
    {#snippet children()}
        <div>
            The <Link href={"https://www.cosanova.org/"}>COSANOVA</Link> project seeks to fully and quantitatively understand the
            atmospheric budget and cycling of carbonyl sulfide (OCS), their main driver being the use of OCS as a carbon
            cycle proxy. A key COSANOVA objective is still the quantification of anthropogenic and marine OCS sources
            particularly in the tropics (i.e. the region of most likely vertical transport to the stratosphere), which
            is also relevant for our activity (OCS being the most important non-volcanic natural source of stratospheric
            aerosol).
        </div>
    {/snippet}
</Project>
