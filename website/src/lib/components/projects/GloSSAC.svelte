<script>
    import Project from "$lib/components/Project.svelte";
    let { refs } = $props()
</script>

<Project title={"GloSSAC"} leads={["Mahesh Kovilakam"]} ongoing>
    {#snippet children()}
        <div>
            The Stratospheric Aerosol Activity will continue to support the continuation and improvement of the NASA
            GloSSAC climatology. The engagement includes the input from data providers and experts on stratospheric
            aerosol observations with respect to usability and quality of already included and potentially valuable new
            data, as well as input from modellers to ensure and maximise GloSSAC usability for global climate models, in
            particular CMIP simulations.
        </div>
    {/snippet}
</Project>
