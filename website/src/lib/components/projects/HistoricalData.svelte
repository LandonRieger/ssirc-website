<script>
    import Project from "$lib/components/projects/Project.svelte";

    let { refs } = $props();
</script>

<Project title={"Recovery of historical data"} leads={["Juan Carlos Antuña-Marrero", "Eduardo Landulfo"]} ongoing
    >{#snippet children()}
        <div>
            The rescue of stratospheric aerosol (SA) lidar datasets began in 2019, although preliminary SSiRC
            discussions on it date back to 2013. The results achieved so far are two rescued shipborne tropical lidar
            datasets from the 1991 Mt. Pinatubo eruption {@html refs.cite("antuna2020")} and three rescued and recalibrated
            datasets from the 1963 Mt. Agung eruption {@html refs.cite("antuna2021", "antuna2024")}. All five rescued
            datasets are publicly available at PANGAEA data repository. The activity will continue to pursue data
            recovery from sites around the globe with some emphasis on the global south. Projects with local funding are
            being proposed to fund part of this effort for the next 5 years, starting in the first semester of 2026. For
            the 2025 - 2030 period, the data recovery project will cover the following specific tasks:
            <ul class="list-disc list-inside my-2">
                <li>
                    Continue the rescue and recalibration of lidar datasets with completion of the 1963 Mt. Agung
                    eruption, continuing with lidar observations from the 1982 El Chichón eruption.
                </li>
                <li>
                    Recalibration of São José dos Campos (1972 -2016) lidar dataset (already rescued) as part of the
                    proposed Brazilian FAPESP project Brazil (led by Dr. Landulfo).
                </li>
                <li>
                    Recalibration of all available tropical SA lidar datasets after the 1991 Pinatubo eruption to fill
                    the first year tropical data gap in GloSSAC (proposal submitted to the Ministry of Science, Spain,
                    led Dr. Juan Antonio Añel, University of Vigo).
                </li>
                <li>
                    Development of a Standardized Lidar Processing Algorithm for SA (SLPS-SA), including a joint
                    proposal together with NDACC, EARLINET, LALINET and GALION to be submitted to the 2026 Call from
                    ISSI.
                </li>
                <li>
                    Expansion of the data rescue to particle size distributions (PSD) in the UTLS that will allow
                    determining the lidar backscatter to extinction, mass and area conversions for SA between the 60’s
                    and 70’s, currently not available.
                </li>
            </ul>
        </div>
    {/snippet}
</Project>
