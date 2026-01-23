<script>
    // import { Listgroup } from "flowbite-svelte";
    import ListGroup from "$lib/components/ListGroup.svelte";
    let questions = [
        {
            name: "Aerosol Properties",
            title: "What is the uncertainty associated with estimates of aerosol properties such as aerosol optical depth over the satellite era, and what are the uncertainties at scales from the 1991 Pinatubo eruption to background levels?",
            content:
                "Space-based measurements provide a record of microphysical and optical properties of stratospheric aerosol with good time resolution and near global coverage. But significant uncertainties as well as discrepancies between observations from different instruments still exist and need to be understood. New satellite missions are urgently needed as the future of space-based measurements beyond 2020 is uncertain.",
        },
        {
            name: "Non-Sulfate",
            title: "What is the contribution from non-sulfate components and how important is the contribution?",
            content:
                "About 50% of all aerosols contain non-sulfate cores of terrestrial or meteoritic origin, and organic and nitrogen compounds contribute to the volatile fraction besides sulfate particularly in the lower stratosphere. The contributions of different compounds from different sources are not well quantified, and their role for the microphysical and chemical aerosol properties is far from being understood and not yet accounted for in most chemistry-climate models to date.",
        },
        {
            name: "Anthropogenic Contributions",
            title: "How do anthropogenic emissions stratospheric aerosol precursors affect stratospheric aerosol variability?",
            content:
                "There is significant uncertainty in the role of human-derived SO2 in changes to stratospheric aerosol levels, and a potential contribution from emissions of other precursors (organics, nitrogen compounds) has only recently been suggested. The impact of regular minor volcanic injections of SO2 and ash into the lower stratosphere makes it difficult to discern human and natural contributions. More measurements of SO2 and other aerosol precursors in the tropical UTLS (Upper Troposphere/Lower Stratosphere) are needed to quantify the role of human activity on stratospheric aerosol levels.",
        },
        {
            name: "Tropospheric Impacts",
            title: "How does the tropospheric sulfur cycle respond to climate change, and how does it affect stratospheric aerosol levels?",
            content:
                "Natural processes play an important role in the global sulfur cycle. Different sulfur compounds are emitted or taken up by vegetation, soils, the oceans and wildfires. Climate change induces significant changes to and in many ecosystems and may thus alter natural sulfur fluxes substantially. A quantitative understanding of these processes and fluxes is necessary to predict such changes and possible climate feedbacks.",
        },
        {
            name: "Temperature and Precipitation",
            title: "How does variability in stratospheric aerosol affect surface temperature and precipitation?",
            content:
                "To investigate the impact of future changes in stratospheric aerosol on surface temperature and precipitation, the temporal development of the stratospheric aerosol layer (including sources and sinks) needs to be included as an interactive module in global climate models. One particular focus is also on the impact of volcanic eruptions.",
        },
        {
            name: "Volcanic Ash",
            title: "How does co-emitted ultra-fine ash influence the volcanic SO2 radiative forcing from major volcanic eruptions?",
            content:
                "Large amounts of ash are emitted by virtually all volcanic eruptions, but this ash is usually removed from the atmosphere much more rapidly than the emitted SO2, and may facilitate rapid removal of the SO2. However, the smallest ash particles may remain for an extended period of time, and they may impact the microphysics and thus the lifetime and radiative forcing of the sulfate particles.",
        },
        {
            name: "Radiative Forcing",
            title: "What are the major uncertainties in calculating stratospheric aerosol radiative forcing?",
            content:
                "For historic eruptions, knowledge of the initial vertical distribution of sulfuric source gases, particularly SO2, is not well known nor is the impact of other condensable and non-volatile material. As a result, the initial aerosol formation process and their resultant radiative impact are difficult to model interactively or estimate from aerosol observations. This data gap might be a potential source of the exaggerated heating found in many models following the eruption of Pinatubo.",
        },
    ];

    let content = $state(questions[0].content);
    let title = $state(questions[0].title);
</script>

<h1 id="about-ssirc">About the Stratospheric Aerosol Activity</h1>
<p>
    <span class="italic">Stratospheric Aerosol</span> is an established APARC (Stratosphere-Troposphere Processes and their
    role in Climate) activity, with APARC being a core project within the World Climate Research Program (WCRP). This activity
    aims to foster collaboration across observational and modelling groups to better understand the stratospheric aerosol
    layer and the drivers for its observed variations. The abrupt volcanic enhancements of the stratospheric aerosol concentrations
    cause strong solar dimming and thereby surface cooling with important changes in circulation and atmospheric composition
    in response. Key science questions link with several foci of the WCRP grand challenges.
</p>
<p>
    The stratospheric aerosol layer was discovered 60 years ago, but it still poses us riddles. Aerosol above 15 km
    forms an optically thin veil with a small well characterized impact on climate, but then, in explosive episodes, it
    can intensify dramatically due to massive, aperiodic volcanic eruptions. Following such events, the stratospheric
    aerosol influences Earth's climate by cooling the planet as a whole and creates potentially devastating changes to
    regional weather patterns, such as winter warming in the Northern Hemisphere and reducing summer monsoon rainfall
    over Africa and Asia. It also increases the probability of an El Niño in the following Northern Hemisphere winter.
    In the modern era, large volcanic events can temporarily slow the pace of anthropogenic global warming.
</p>

<h2 id="open-questions">Open Questions</h2>
<div class="pb-4">
    While much is understood about the impact of stratospheric aerosol on climate, there are a number of open questions
    relevant to the Stratospheric Aerosol activity, SPARC and the WCRP:
</div>

<div class="flex flex-row">
    <div class="w-72 flex-none mx-4">
        {#each questions as question}
            <div class="flex-grow">
                <button
                    class="flex-grow hover:bg-gray-100 hover:font-bold px-4 py-1.5 w-full text-left"
                    onclick={() => {
                        content = question.content;
                        title = question.title;
                    }}>{question.name}</button>
            </div>
        {/each}
        <!--        <ListGroup-->
        <!--            active-->
        <!--            links={questions}-->
        <!--            class="w-48"-->
        <!--            on:click={(e) => {-->
        <!--                content = e.detail.content;-->
        <!--                title = e.detail.title;-->
        <!--            }}>-->
        <!--            &lt;!&ndash;{#snippet children({ item })}&ndash;&gt;-->
        <!--            &lt;!&ndash;    {item.name}&ndash;&gt;-->
        <!--            &lt;!&ndash;{/snippet}&ndash;&gt;-->
        <!--        </ListGroup>-->
    </div>
    <div class="grow">
        <h3>{title}</h3>
        <div class="text-gray-800">{content}</div>
    </div>
</div>

<h2 id="goals">Goals</h2>
<p>
    By addressing these questions, the Stratospheric Aerosol activity aims at better constraining the pathways of
    stratospheric aerosol and its precursors from emission to radiative forcing. By raising these questions and
    highlighting their importance, this activity stimulates research in this area that is relevant to WCRP's mission;
    enabling the assessment of our understanding of the role of stratospheric aerosol in climate including the potential
    for catastrophic climate impacts following a major volcanic event, and decoupling more moderate climate changes in
    the stratospheric aerosol burden from those attributable to human activities. This activity builds a community from
    different fields of study and fosters collaboration, and connecting to other WCRP/SPARC activities including ACAM,
    OCTV-UTLS and CCMI.
</p>
