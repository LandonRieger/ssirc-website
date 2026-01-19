<script>
    import Project from "$lib/components/Project.svelte";
    import Link from "$lib/components/Link.svelte";
    let { refs } = $props();
</script>

<Project title={"VolRes"} leads={["Jean-Paul Vernier", "Claudia Timmreck", "Thomas Aubry"]} ongoing>
    {#snippet children()}
        <div id="volres">
            Since its creation in 2015, VolRes consists of more than 250 scientists worldwide, from a diverse range of
            both model and observational expertise, aiming to contribute to the sharing and discussion of information
            related to the atmospheric impacts of volcanoes. Discussion and sharing via the mailing list is maintained
            through an archive and <Link href={"https://wiki.earthdata.nasa.gov/display/volres"}>Wiki page</Link> proposal.
            The 2019 Raikoke eruption was used as a test bed to demonstrate how the VolRes group responded to this event
            by providing a total SO2 mass vertical distribution derived from satellite observations within one week after
            the eruption. This allowed simple climate calculations to assess the impact of Raikoke {@html refs.cite(
                "vernier2024",
            )}. Further work has been done by the climate modelling community to simulate what could be the impact of a
            Mt Pinatubo-size eruption on current climate under the APARC Decadal Climate Prediction Project (DCPP)
            through Volcanic Response Readiness Exercise {@html refs.cite("alfonso2024")}.
        </div>
        <div>
            VolRes will continue to foster immediate communication of available information and strategies and plans for
            observational and modeling activities after large and medium-size volcanic eruptions and significant
            wildfire events. This includes, on the technical side, maintenance of the VolRes web forum and mailing list.
            Specific tasks and improvements for the 2025 - 2030 period include:
            <ul class="list-disc list-inside my-2">
                <li>Rapid production of SO2 mass estimates and vertical distributions after eruptions.</li>
                <li>Organization of VolRes sessions at large conferences (AGU, EGU).</li>
                <li>
                    Formalization of products that can be developed by VolRes and made available for climate modellers
                    of APARC-DCPP and co-organization of a meeting with APARC-DCPP in the 2025/26 time frame.
                </li>
                <li>
                    Exploring whether new products can be made available, e.g. volcanic ash concentration and profiles,
                    water vapor, relevant parameters in the context of wildfires.
                </li>
            </ul>
        </div>
    {/snippet}
</Project>
