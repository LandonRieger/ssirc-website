<script>
    import Project from "$lib/components/projects/Project.svelte";
    import Link from "$lib/components/Link.svelte"
    let { refs } = $props()
</script>

<Project title={"Stratéole 2"} leads={[]} ongoing>
    {#snippet children()}
        <div>
            <Link href={"https://strateole2.cnes.fr/en/strateole-2-0"}>Stratéole 2</Link> is a project to improve our understanding of the
            tropical tropopause layer (TTL). The TTL is the primary pathway for material transport from the troposphere
            to the stratosphere aside from major volcanic eruptions and meteoric material. Thus understanding the
            stratospheric aerosol budget during volcanically quiescent periods requires understanding the material
            contributions from, and the dynamics of, the TTL.
        </div>
        <div>
            Stratéole 2 will extend the unprecedented small scale observations of temperature, wind, water vapor, ozone,
            and aerosol in and across the TTL using semi-Lagrangian drifting balloons, which can remain aloft for
            months. The second Stratéole 2 scientific field campaign is planned for October-December 2026.
        </div>
    {/snippet}
</Project>
