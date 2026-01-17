<script>
    import Project from "$lib/components/Project.svelte";
</script>

<Project title={"REAS"} leads={["Nicolas Dumelie", "Jean-Paul Vernier", "Gwenael Berthet"]}>
    {#snippet children()}
        <div>
            The REAS (Rapid Balloon Experiments for Sudden Aerosol Injection in the Stratosphere, Dumelié et al., 2024)
            project is a collaboration between NASA, CNRS-Orleans and the University of Reims to launch instrumented
            balloons with aerosol measurements to respond to volcanic eruptions and PyroCbs impacting stratospheric
            aerosol. There are obvious links to the Stratospheric Aerosol Activity and in particular the VolRes project,
            and close links are currently being established. A dedicated project page on the Stratospheric Aerosol
            Activity’s website will provide relevant information including data links and promote this activity.
        </div>
    {/snippet}
</Project>
