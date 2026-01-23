<script>
    import Project from "$lib/components/projects/Project.svelte";
    let { refs } = $props()
</script>

<Project title={"Hunga Model Observations Comparison (HTHH-MOC)"} leads={["Yunqian Zhu", "Graham Mann"]} ongoing>
    {#snippet children()}
        <div>
            The 2022 Hunga eruption was the most explosive volcanic eruption in the satellite era, and the water-rich
            plume presents an opportunity to understand the impacts on the stratosphere of a large magnitude explosive
            phreatomagmatic eruption. The APARC Hunga Impact Activity that was co-initiated by SSiRC has coordinated
            research activities and is currently finalizing a special report on Hunga-Tonga impacts that will be
            published in late 2025 and will directly feed into the upcoming 2026 UNEP/WMO Scientific Assessment of Ozone
            Depletion report, providing a benchmark synthesis of the impacts from the eruption.
        </div>
        <div>
            The Hunga Model Observations Comparison (HTHH-MOC) project has been established to assist the success of the
            report and will continue after 2025 with more analysis and publications and release data to the public.The
            project investigates the evolution of volcanic water and aerosols, and their impacts on atmospheric
            dynamics, chemistry, and climate, using several state-of-the-art chemistry climate models.
        </div>
    {/snippet}
</Project>
