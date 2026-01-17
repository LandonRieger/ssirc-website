<script>
    import { Listgroup } from "flowbite-svelte";
    import BibEntry from "$lib/components/BibEntry.svelte";
    import HistoricalData from "$lib/components/projects/HistoricalData.svelte";
    import VolRes from "$lib/components/projects/VolREs.svelte";
    import HTHHMOC from "$lib/components/projects/VolREs.svelte";
    import SAIRisks from "$lib/components/projects/SAIRisks.svelte";
    import GloSSAC from "$lib/components/projects/GloSSAC.svelte";
    import Cosanova from "$lib/components/projects/Cosanova.svelte";
    import BATAL from "$lib/components/projects/BATAL.svelte";
    import REAS from "$lib/components/projects/REAS.svelte";
    import SABRE from "$lib/components/projects/SABRE.svelte";
    import Strateole2 from "$lib/components/projects/Strateole2.svelte";
    import ISAMIP from "$lib/components/projects/ISAMIP.svelte";
    import Outreach from "./Outreach.svelte";
    import { Bibliography } from "$lib/bib/state.svelte.ts"

    let links = [
        { name: "Knowledge Gaps", href: "#knowledge-gaps" },
        { name: "Stratospheric Aerosol Projects", href: "#ssirc-projects" },
        { name: "Associated Projects", href: "#associated-projects" },
        { name: "New Projects", href: "#new-projects" },
        { name: "Outreach", href: "#outreach" },
    ];

    import { parse } from "yaml";
    import bibEntries from "./../../lib/bib/references.yaml?raw";
    let bib = parse(bibEntries);
    let refs = new Bibliography(bib)
    // console.log(bib["kremser2016"], bib["timreck2018"], bib["thomason2018"], bib["zanchettin2016"]);

    let questions = [
        {
            name: "Continuity",
            title: "Ensure continuity in the ~50 year observational record of stratospheric aerosol to detect future changes and to attribute them to natural and anthropogenic processes, and extreme events",
            content:
                "The importance of satellite observations with good spatial and temporal coverage can’t be stressed enough. Such observations are needed for climate models to simulate and predict regional climate impacts on seasonal to sub-seasonal time scales following episodic events like volcanic eruptions and wildfires, and they will be crucial to detect and monitor any deliberate SAI endeavors by governments or private stakeholders. Long-term measurements are critical to understanding a changing climate, but this area remains challenging as instruments are retired, updated and hopefully replaced. Ensuring continuity from an ever-changing collection of advancing instruments that span different techniques, sampling characteristics and quantities remains a primary challenge of the community that will be addressed by the Stratospheric Aerosol Activity with high priority. While discrepancies between instruments (e.g. reconciling solar occultation and limb sounding measurements under enhanced conditions) remains an ongoing source of consternation when merging records, the variety of current and planned missions, both in situ and remote, provide a unique opportunity for measurement synergy and aerosol understanding that was not possible in the past. The ability to improve detection, attribution and understanding of aerosol changes will rely both on the continuation of measurements and the community to maximize the science return from these records. Details on specific challenges and necessary tasks to be addressed in the context of stratospheric aerosol observations over the coming years are given in a white paper by an ISSI team on Perspectives of Stratospheric Aerosol Observations that was initiated by the Stratospheric Aerosol Activity (Kloss et al., 2025).",
        },
        {
            name: "Climate Model Representation",
            title: "How well are upper tropospheric and stratospheric aerosols represented in global climate models, which are critical for our confidence in climate projections?",
            content:
                "With more types of upper tropospheric and stratospheric aerosols being detected and measured remotely and in-situ, there is a need to consider their various roles in the climate system. Currently, most climate models consider only sulfate aerosol in the stratosphere. More evidence now shows the potential importance of meteoric dust, aerosols from satellite reentry and rocket launches, organics, ammonium and nitrate aerosols to be included in aerosol simulations in the climate models. Those non-sulfate particles are important to understand the stratospheric aerosol composition, microphysical properties, and their radiative and chemical impacts.",
        },
        {
            name: "Global Warming",
            title: "What role does global climate warming play in modifying the stratospheric aerosol lifecycle and its associated aerosol radiative forcing?",
            content:
                "Global warming alters the thermal structure and circulation of the upper atmosphere, which in turn alters the stratospheric aerosol lifecycle and the magnitude of aerosol radiative forcing (Aubry et al., 2022). Using climate model simulations, Aubry et al. (2021) showed that a higher future tropopause means moderate-magnitude tropical eruptions inject proportionally less sulfur into the stratosphere, reducing stratospheric aerosol optical depth by about 75 % in a high-end warming scenario. Plume-rise height from less-frequent large-magnitude eruptions on the contrary increases under global warming, which together with an acceleration of the Brewer–Dobson circulation has been suggested to produce smaller-sized sulfate particles and thus a larger global-mean radiative forcing compared to present-day. Overall, our understanding of the role of climate change in altering volcanic aerosol–climate interactions is still limited and requires further research also in the context of SAI.",
        },
        {
            name: "Pyroconvective Events",
            title: "What are, quantitatively, the impacts on radiative forcing and stratospheric chemistry, of particles transported upward or formed in pyroconvective plumes?",
            content:
                "Natural processes play an important role in the global sulfur cycle. Different sulfur compounds are emitted or taken up by vegetation, soils, the oceans and wildfires. Climate change induces significant changes to and in many ecosystems and may thus alter natural sulfur fluxes substantially. A quantitative understanding of these processes and fluxes is necessary to predict such changes and possible climate feedbacks.",
        },
        {
            name: "SAI Impacts",
            title: "What are the global and regional impacts of deliberate SAI on climate and stratospheric chemistry? To what degree do volcanic eruptions serve as analogues for SAI using sulfate aerosol particles?",
            content:
                "Calls to consider climate engineering (CI) as a means to mitigate climate change are growing louder, and SAI is nowadays openly discussed as one CI method. Much research has already been conducted over the past two decades, looking at potential benefits in terms of global radiative forcing but also at unwanted regional climate impacts as well as other risks such as chemical ozone destruction. As the community with comprehensive expertise on stratospheric aerosol, we naturally engage in this research striving to fill relevant knowledge gaps. We support ongoing and anticipated reviews and evaluations to provide a sound scientific foundation for scenario simulations in climate models and a comprehensive risk assessment of SAI. This will be done in close collaboration with the WCRP Lighthouse Activity on Climate Intervention Research (see below under Projects and Activities).",
        },
    ];
    let content = $state(questions[0].content);
    let title = $state(questions[0].title);
</script>

{#snippet ssirc()}
    <span class="italic">Stratospheric Aerosol</span>
{/snippet}

<div class="flex w-full">
    <div class="flex flex-col"></div>

    <div class="flex-none col hidden w-64 xl:text-sm xl:block end-0">
        <div class="flex overflow-y-auto sticky top-20 flex-col justify-between pb-6 mr-6 h-[calc(100vh-5rem)]">
            <div>
                <p class="uppercase font-medium text-gray-700 mb-4">On this page</p>
                <Listgroup active items={links}>
                    {#snippet children({ item })}
                        {item.name}
                    {/snippet}
                </Listgroup>
            </div>
        </div>
    </div>

    <div class="flex flex-col">
        <h1>Stratospheric Aerosol Activity Implementation Plan 2025-2030</h1>
        <p class="font-light italic text-sm text-gray-700">by the Scientific Steering Group</p>
        <div class="mb-2">
            Within the World Climate Research Program’s (WCRP) core project Atmospheric Processes And their Role in
            Climate (APARC), the Stratospheric Aerosol Activity (that evolves from the activity on Stratospheric Sulfur
            and its Role in climate, SSiRC) addresses critical elements of the WCRP mission by focusing on a
            ‘persistently variable’ {@html refs.cite("solomon2011")} component of climate forcing: aerosol in the stratosphere and
            upper troposphere.
        </div>
        <div class="mb-2">
            Above the atmospheric boundary layer, global climate forcing by aerosol under background conditions is small
            and relatively stable, although regional impacts related to anthropogenic emissions of aerosol precursors
            are more prevalent than with greenhouse gases due to the variable nature of emissions and shorter lifetimes.
            Following aperiodic events such as volcanic eruptions or pyro-convection, aerosol loading in the upper
            atmosphere intensifies dramatically and influences the Earth's climate by warming the stratosphere and
            cooling the surface. These temperature changes can potentially induce changes to large scale circulation and
            regional weather patterns that can persist for several years. Particularly large volcanic eruptions like the
            1991 Mt. Pinatubo eruption temporarily slowed the pace of human-induced global warming. This has led to the
            idea of offsetting global warming by artificially supplying particles to the stratosphere, a form of climate
            engineering termed stratospheric aerosol injection (SAI).
        </div>
        <div class="mb-2">
            Since 2012, SSiRC has worked to build and support a community focused on the scientific understanding of
            stratospheric sulfur and its role in stratospheric aerosol and the concomitant impacts on climate. The SSiRC
            community has been built through four general workshops on stratospheric aerosol (Atlanta, 2013; Potsdam,
            2016: Leeds, 2022; virtual event in 2021), one workshop focused on measurement of stratospheric aerosol
            (Boulder, 2017), and a Chapman Conference on stratospheric aerosol in the post Pinatubo era (Tenerife,
            2018). Together with the APARC activity on Atmospheric Composition and the Asian Monsoon (ACAM), SSiRC has
            promoted and supported research activities on UTLS aerosols in Asia and co-organized the STIPMEX workshop in
            June 2024 in Pune {@html refs.cite("fadnavis2024")}. Recently, a workshop on the volcanic impact on atmosphere and
            climate (Greifswald, Germany, 2025) was organized jointly with the German research initiative VolImpact.
            Additionally, SSiRC has made key contributions to the literature including the first extensive review of the
            status of stratospheric aerosol {@html refs.cite("kremser2016")} since the SPARC (2006) Assessment of Stratospheric
            Aerosol Properties (ASAP).
        </div>
        <div class="mb-2">
            A subgroup focusing on a rapid response to volcanic eruptions to determine their potential climate impact
            (VolRes, cf. below in the projects section) was formed in 2015. VolRes responded to the 2019 Raikoke
            eruption within a week {@html refs.cite("vernier2024")}, and provided a communication platform to initiate the global
            community response after the Hunga eruption (Vernier et al., 2022). VolRes is also linked to the Model
            Intercomparison Project on the climatic response to Volcanic forcing (VolMIP, Zanchettin et al., 2016); and
            the Interactive Stratospheric Aerosol Model Intercomparison Project (ISA-MIP, Timmreck et al., 2018). The
            SSiRC community also helped guide the development of long-term stratospheric aerosol forcing datasets for
            climate modeling (GloSSAC), {@html refs.cite("thomason2018", "kovilakam2020")} and enhanced discussions to
            incorporate new satellite observations to the database {@html refs.cite("kovilakam2025")}. In 2022,
            SSiRC also played a key role in initiating the APARC Hunga Tonga-Hunga Ha’pai stratospheric Impacts
            activity, which is currently writing up a community assessment as an APARC report that will directly feed
            into the 2026 UNEP/WMO Scientific Assessment of Ozone Depletion.
        </div>
        <div class="mb-2">
            Through these contributions, the activity’s Scientific Steering Group (SSG) believes that SSiRC has proven
            to be an active and successful APARC activity. However, it is clear that substantial work remains to
            adequately understand stratospheric aerosol, its precursors, and the feedback with climate. This
            understanding is complicated by the increasing atmospheric greenhouse gases and the subsequent warming.
            Moreover, the rapidly growing interest in research into SAI, which could involve active experimentation in
            the coming years, has added a new urgency to understanding the details controlling stratospheric aerosol
            properties and their impacts on climate.
        </div>
        <div class="mb-2">
            This warrants a continuation of the activity with its active community. The activity will be renamed from
            SSiRC to Stratospheric Aerosol Activity, accounting for the understanding that stratospheric aerosol is not
            as dominated by sulfur compounds as previously thought and for emerging non-sulfur topics and challenges,
            e.g. the role of Ammonium Nitrate particles of anthropogenic origin over Asia {@html refs.cite("hopfner2019")}, the
            discovery of substantial contributions of spacecraft debris to the global stratosphere (Murphy et al., 2023)
            or the growing frequency and intensity of aerosol injections from wildfires {@html refs.cite("katich2023")}. For the
            activity to remain productive, it must be agile with respect to our changing understanding and to scientific
            priorities regarding our knowledge gaps, and committed to acting as a bridge between the measurement and
            modelling communities. This document summarizes where the Stratospheric Aerosol Activity is aiming to head,
            describing the most important knowledge gaps and challenges and ongoing and planned specific projects and
            collaborations.
        </div>

        <h2 id="knowledge-gaps">Knowledge gaps, new challenges and science questions</h2>

        <div class="flex flex-row">
            <div class="w-64 flex-none">
                <Listgroup
                    active
                    items={questions}
                    class="w-48"
                    on:click={(e) => {
                        content = e.detail.content;
                        title = e.detail.title;
                    }}>
                    {#snippet children({ item })}
                        {item.name}
                    {/snippet}
                </Listgroup>
            </div>
            <div class="grow">
                <h3>{title}</h3>
                <div class="text-gray-800">{content}</div>
            </div>
        </div>

        <h2 id="ssirc-projects">Projects and Activities</h2>
        <h3>Projects organized or led by the Stratospheric Aerosol Activity</h3>

        <HistoricalData />
        <VolRes />
        <h3>Associated Projects to which the Stratospheric Aerosol Activity contributes</h3>
        <HTHHMOC />
        <SAIRisks />
        <GloSSAC />
        <Cosanova />
        <BATAL />
        <Strateole2 />
        <REAS />
        <SABRE />
        <ISAMIP />

        <h2 id="outreach">Extending Outreach</h2>
        <Outreach />

        <h2 id="references">References</h2>

        {#each refs.print() as item}
            <BibEntry entry={item.entry} id={item.id} />
        {/each}
    </div>
</div>
