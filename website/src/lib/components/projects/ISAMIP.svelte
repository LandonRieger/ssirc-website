<script>
    import Project from "$lib/components/Project.svelte";
</script>

<Project title={"ISA-MIP"} leads={["Graham Mann", "Timofei Sukhodolov", "Margot Clyne"]}>
    {#snippet children()}
        <div>
            The multi-modeling initiative with closest alignment to the Stratospheric Aerosol Activity continues to be
            ISA-MIP (https://isamip.eu/home), which defined in 2018 (Timmreck et al., 2018) four co-ordinated
            multi-model experiments for composition climate models with interactive stratospheric aerosol. The ISA-MIP
            experiments provide a continuing basis to develop and improve the models, with protocols defining benchmark
            integrations across 3 themes:
            <ul class="list-disc list-inside my-2">
                <li>the background/quiescent stratospheric aerosol layer (BG experiment)</li>
                <li>the post-2000 transient stratospheric aerosol record (TAR experiment)</li>
                <li>historical major volcanic aerosol clouds (HErSEA and PoEMS experiments)</li>
            </ul>
            After the CoViD period, ISA-MIP resumed multi-model analysis, and benchmark papers in 2023 and 2024 have analysed
            intercomparisons for BG (Brodowsky et al. 2024) and HErSEA-Pinatubo experiments (Quaglia et al., 2023).
        </div>
        <div>
            A PhD studentship at the BOKU University (Vienna, Austria) analysing the heating of the stratosphere
            predicted from the interactive HErSEA-Pinatubo integrations, presented at the SSiRC-aligned stratospheric
            aerosol & volcanic impacts EGU session (Perny et al., 2025).
        </div>
        <div>
            Aligned to the HTHH-MOC activity, another recent ISA-MIP multi-model activity of the Hunga aerosol is led by
            Margot Clyne (now at Colorado State University, formerly Univ. Colorado). The Tonga-MIP experiment assesses
            how water vapour co-emitted with volcanic SO2 affects an initial descent of volcanic aerosol clouds, and how
            it affects microphysical progression.
        </div>
        <div>
            Whilst ISA-MIP remains the primary multi-model activity for the Stratospheric Aerosol Activity, the activity
            will also continue to align with new experiments in the VolMIP and GeoMIP activities, contributing to CMIP7,
            including with the new emission-based volcanic forcing dataset (Aubry, 2025).
        </div>
        <div>
            The ISA-MIP data archive at the German DKRZ data center continues to provide a basis also for new
            comparative analysis of interactive stratospheric aerosol model data, across the three themes.
        </div>
    {/snippet}
</Project>
