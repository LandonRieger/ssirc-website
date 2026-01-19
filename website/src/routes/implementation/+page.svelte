<script>
    import { Listgroup } from "flowbite-svelte";
    import Link from "$lib/components/Link.svelte";
    import BibEntry from "$lib/components/BibEntry.svelte";
    import HistoricalData from "$lib/components/projects/HistoricalData.svelte";
    import VolRes from "$lib/components/projects/VolRes.svelte";
    import HTHHMOC from "$lib/components/projects/HTHHMOC.svelte";
    import SAIRisks from "$lib/components/projects/SAIRisks.svelte";
    import GloSSAC from "$lib/components/projects/GloSSAC.svelte";
    import Cosanova from "$lib/components/projects/Cosanova.svelte";
    import BATAL from "$lib/components/projects/BATAL.svelte";
    import REAS from "$lib/components/projects/REAS.svelte";
    import SABRE from "$lib/components/projects/SABRE.svelte";
    import Strateole2 from "$lib/components/projects/Strateole2.svelte";
    import ISAMIP from "$lib/components/projects/ISAMIP.svelte";

    import Continuity from "$lib/components/questions/Continuity.svelte";
    import GlobalWarming from "$lib/components/questions/GlobalWarming.svelte";
    import ModelRepresentation from "$lib/components/questions/ModelRepresentation.svelte";
    import PyroCBs from "$lib/components/questions/PyroCBs.svelte";
    import SAI from "$lib/components/questions/SAI.svelte";

    import Outreach from "./Outreach.svelte";
    import { Bibliography } from "$lib/bib/state.svelte.ts";
    import { parse } from "yaml";
    import bibEntries from "./../../lib/bib/references.yaml?raw";

    let links = [
        { name: "Overview", href: "#implementation" },
        { name: "Knowledge Gaps", href: "#knowledge-gaps" },
        { name: "Projects and Activities", href: "#ssirc-projects" },
        { name: "Outreach", href: "#outreach" },
        { name: "References", href: "#references" },
    ];
    let bib = parse(bibEntries);
    let refs = new Bibliography(bib);
</script>

{#snippet ssirc()}
    <span class="italic">Stratospheric Aerosol</span>
{/snippet}

<div class="flex">
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

    <div class="flex flex-col max-w-3xl hyphens-auto text-justify">
        <h1 class="text-3xl font-bold text-gray-900 text-left">
            Stratospheric Aerosol Activity Implementation Plan 2025-2030
        </h1>
        <p class="font-light italic text-sm text-gray-700">by the Scientific Steering Group</p>
        <h2>Activity Overview</h2>
        <div class="space-y-2" id="implementation">
            <div>
                Within the World Climate Research Program’s (WCRP) core project Atmospheric Processes And their Role in
                Climate (APARC), the Stratospheric Aerosol Activity (that evolves from the activity on Stratospheric
                Sulfur and its Role in climate, SSiRC) addresses critical elements of the WCRP mission by focusing on a
                ‘persistently variable’ {@html refs.cite("solomon2011")} component of climate forcing: aerosol in the stratosphere
                and upper troposphere.
            </div>
            <div>
                Above the atmospheric boundary layer, global climate forcing by aerosol under background conditions is
                small and relatively stable, although regional impacts related to anthropogenic emissions of aerosol
                precursors are more prevalent than with greenhouse gases due to the variable nature of emissions and
                shorter lifetimes. Following aperiodic events such as volcanic eruptions or pyro-convection, aerosol
                loading in the upper atmosphere intensifies dramatically and influences the Earth's climate by warming
                the stratosphere and cooling the surface. These temperature changes can potentially induce changes to
                large scale circulation and regional weather patterns that can persist for several years. Particularly
                large volcanic eruptions like the 1991 Mt. Pinatubo eruption temporarily slowed the pace of
                human-induced global warming. This has led to the idea of offsetting global warming by artificially
                supplying particles to the stratosphere, a form of climate engineering termed stratospheric aerosol
                injection (SAI).
            </div>
            <div>
                Since 2012, SSiRC has worked to build and support a community focused on the scientific understanding of
                stratospheric sulfur and its role in stratospheric aerosol and the concomitant impacts on climate. The
                SSiRC community has been built through four general workshops on stratospheric aerosol (Atlanta, 2013;
                Potsdam, 2016: Leeds, 2022; virtual event in 2021), one workshop focused on measurement of stratospheric
                aerosol (Boulder, 2017), and a Chapman Conference on stratospheric aerosol in the post Pinatubo era
                (Tenerife, 2018). Together with the APARC activity on Atmospheric Composition and the Asian Monsoon
                (ACAM), SSiRC has promoted and supported research activities on UTLS aerosols in Asia and co-organized
                the STIPMEX workshop in June 2024 in Pune {@html refs.cite("fadnavis2024")}. Recently, a workshop on the
                volcanic impact on atmosphere and climate (Greifswald, Germany, 2025) was organized jointly with the
                German research initiative VolImpact. Additionally, SSiRC has made key contributions to the literature
                including the first extensive review of the status of stratospheric aerosol {@html refs.cite(
                    "kremser2016",
                )} since the SPARC (2006) Assessment of Stratospheric Aerosol Properties (ASAP).
            </div>
            <div>
                A subgroup focusing on a rapid response to volcanic eruptions to determine their potential climate
                impact (<Link href="#volres">VolRes</Link>) was formed in 2015. VolRes responded to the 2019
                Raikoke eruption within a week {@html refs.cite("vernier2024")}, and provided a communication platform
                to initiate the global community response after the Hunga eruption (Vernier et al., 2022). VolRes is
                also linked to the Model Intercomparison Project on the climatic response to Volcanic forcing (VolMIP,
                Zanchettin et al., 2016); and the Interactive Stratospheric Aerosol Model Intercomparison Project
                (ISA-MIP, Timmreck et al., 2018). The SSiRC community also helped guide the development of long-term
                stratospheric aerosol forcing datasets for climate modeling (GloSSAC), {@html refs.cite(
                    "thomason2018",
                    "kovilakam2020",
                )} and enhanced discussions to incorporate new satellite observations to the database {@html refs.cite(
                    "kovilakam2025",
                )}. In 2022, SSiRC also played a key role in initiating the APARC Hunga Tonga-Hunga Ha’pai stratospheric
                Impacts activity, which is currently writing up a community assessment as an APARC report that will
                directly feed into the 2026 UNEP/WMO Scientific Assessment of Ozone Depletion.
            </div>
            <div>
                Through these contributions, the activity’s Scientific Steering Group (SSG) believes that SSiRC has
                proven to be an active and successful APARC activity. However, it is clear that substantial work remains
                to adequately understand stratospheric aerosol, its precursors, and the feedback with climate. This
                understanding is complicated by the increasing atmospheric greenhouse gases and the subsequent warming.
                Moreover, the rapidly growing interest in research into SAI, which could involve active experimentation
                in the coming years, has added a new urgency to understanding the details controlling stratospheric
                aerosol properties and their impacts on climate.
            </div>
            <div>
                This warrants a continuation of the activity with its active community. The activity will be renamed
                from SSiRC to Stratospheric Aerosol Activity, accounting for the understanding that stratospheric
                aerosol is not as dominated by sulfur compounds as previously thought and for emerging non-sulfur topics
                and challenges, e.g. the role of Ammonium Nitrate particles of anthropogenic origin over Asia {@html refs.cite(
                    "hopfner2019",
                )}, the discovery of substantial contributions of spacecraft debris to the global stratosphere {@html refs.cite(
                    "murphy2023",
                )} or the growing frequency and intensity of aerosol injections from wildfires {@html refs.cite(
                    "katich2023",
                )}. For the activity to remain productive, it must be agile with respect to our changing understanding
                and to scientific priorities regarding our knowledge gaps, and committed to acting as a bridge between
                the measurement and modelling communities. This document summarizes where the Stratospheric Aerosol
                Activity is aiming to head, describing the most important knowledge gaps and challenges and ongoing and
                planned specific projects and collaborations.
            </div>
        </div>
        <h2 id="knowledge-gaps">Knowledge gaps, new challenges and science questions</h2>

        <div class="space-y-4">
            <Continuity {refs} />
            <GlobalWarming {refs} />
            <ModelRepresentation {refs} />
            <PyroCBs {refs} />
            <SAI {refs} />
        </div>

        <h2 id="ssirc-projects">Projects and Activities</h2>
        <h3>Projects organized or led by the Stratospheric Aerosol Activity</h3>

        <HistoricalData {refs} />
        <VolRes {refs} />
        <h3>Associated Projects to which the Stratospheric Aerosol Activity contributes</h3>
        <HTHHMOC {refs} />
        <SAIRisks {refs} />
        <GloSSAC {refs} />
        <Cosanova {refs} />
        <BATAL {refs} />
        <Strateole2 {refs} />
        <REAS {refs} />
        <SABRE {refs} />
        <ISAMIP {refs} />

        <h2 id="outreach">Extending Outreach</h2>
        <Outreach />

        <h2 id="references">References</h2>

        <div class="space-y-2">
            {#each refs.print() as item}
                <BibEntry entry={item.entry} id={item.id} format={"short"} />
            {/each}
        </div>
    </div>
</div>
