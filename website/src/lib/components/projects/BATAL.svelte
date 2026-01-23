<script>
    import Project from "$lib/components/projects/Project.svelte";
    let { refs } = $props()
</script>

<Project title={"BATAL"} leads={["Jean-Paul Vernier"]} ongoing>
    {#snippet children()}
        <div>
            The Stratospheric Aerosol Activity will continue to collaborate with the Balloon Measurement Campaigns of
            the Asian Tropopause Aerosol Layer, BATAL, {@html refs.cite("vernier2018")}. The project will be funded by NASA until
            2029, but campaigns may not take place every year. A regularly updated page about BATAL with links to latest
            results and data will soon be included on the Stratospheric Aerosol Activity’s website.
        </div>
    {/snippet}
</Project>
