<script>
    import Project from "$lib/components/Project.svelte";
</script>

<Project
    title={"Collaborative project with the WCRP Lighthouse Activity on Climate Intervention Research to explore measurement capabilities and risks of SAI (new project)"}
    leads={["Marc von Hobe", "Daniele Visioni"]}>
    {#snippet children()}
        <div>
            In close coordination and collaboration with the WCRP LHA, the APARC Stratospheric Aerosol Activity will
            build on the knowledge and resources of its community with respect to both, observations and simulations, to
            evaluate and better understand:
            <ul class="list-disc list-inside my-2">
                <li>the capacities and needs to detect, monitor and attribute any SAI endeavours</li>
                <li>the global and regional climate impacts as well as the associated risks of SAI.</li>
            </ul>
        </div>
        <div>
            The production of an assessment report is envisaged for the scientific community as well as relevant
            stakeholders and policy makers, and to serve as input for the IPCC in the AR7 process. In this respect, a
            virtual workshop will be held in October 2025 It has already been announced at
            https://www.wcrp-climate.org/ci-workshop-series-sai.
        </div>
    {/snippet}
</Project>
