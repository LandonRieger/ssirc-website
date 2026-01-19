<script>
    import Project from "$lib/components/Project.svelte";
    import Link from "$lib/components/Link.svelte";
    let { refs } = $props();
</script>

<Project title={"SABRE"} leads={["Troy Thornberry", "Eric Jensen"]} newproject>
    {#snippet children()}
        <div>
            The NOAA <Link href={"https://csl.noaa.gov/projects/sabre/"}>SABRE</Link> (Stratospheric Aerosol processes, Budget
            and Radiative Effects) project is using the NASA WB-57 high-altitude research aircraft equipped with comprehensive
            aerosol and chemistry instruments to better understand stratospheric aerosol sources, evolution, and chemical
            impacts. In 2023 SABRE had a major field intensive out of Fairbanks, AK, USA, acquiring measurements in the arctic
            winter. Future flight campaigns are tentatively planned for sampling of the tropical UT/LS (2026) and the antarctic
            stratosphere.
        </div>
    {/snippet}
</Project>
