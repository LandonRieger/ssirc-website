<script>
    import { Listgroup } from "flowbite-svelte";
    import BibEntry from "$lib/components/BibEntry.svelte";
    let links = [
        { name: "Knowledge Gaps", href: "#knowledge-gaps" },
        { name: "Stratospheric Aerosol Projects", href: "#ssirc-projects" },
        { name: "Associated Projects", href: "#associated-projects" },
        { name: "New Projects", href: "#new-projects" },
        { name: "Outreach", href: "#outreach" },
    ];
    import {parse} from 'yaml'
    import bibEntries from "./../../lib/bib/references.yaml?raw";
    let bib = parse(bibEntries);
    console.log(bib["kremser2016"], bib["timreck2018"],bib["thomason2018"],bib["zanchettin2016"])
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
        <h1>Implementation Plan</h1>
        <p class="font-light italic text-sm text-gray-700">May 2019 - by the {@render ssirc()} Science Steering Group</p>
        <div class="mb-2">
            {@render ssirc()} addresses critical elements of the World Climate Research Program (WCRP) mission by focusing
            on the most variable component of climate forcing: stratospheric aerosol. At most times, aerosol above the tropopause
            is an optically thin veil with little impact on climate but it can intensify dramatically due to massive, aperiodic
            volcanic eruptions. Following such events, the stratospheric aerosol influences the Earth's climate by cooling
            the planet as a whole and creating potentially devastating changes to regional weather patterns that can persist
            for a number of years. In the modern era, large volcanic events can temporarily slow the pace of human-derived
            global warming. Since 2012, {@render ssirc()} has worked to build and support a community focused on the scientific understanding
            of stratospheric sulfur and aerosol, and their role in climate. The {@render ssirc()} community has been
            built through two general workshops on stratospheric aerosol (Atlanta, 2013; Potsdam, 2016), one workshop focused
            on measurement of stratospheric aerosol (Boulder, 2017), and a Chapman Conference on stratospheric aerosol in
            the post Pinatubo era (Tenerife, 2018). Furthermore, a subgroup that focuses on a rapid response to an ongoing
            volcanic eruption to determine the potential climate impact (VolRes) has been formed. This groups is supported
            by the development of the Model Intercomparison Project on the climatic response to Volcanic forcing (VolMIP
            , Zanchettin et al., 2016); and a new Interactive Stratospheric Aerosol Model Intercomparison Project (ISA-MIP,
            Timmreck et al., 2018). The {@render ssirc()} community also contributed to the development of long-term stratospheric aerosol
            forcing datasets for climate modeling (GloSSAC , Thomason et al., 2018). A key contribution to the stratospheric
            aerosol research was the publication of the first extensive review of the status of stratospheric aerosol (Kremser
            et al., 2016) since the SPARC Assessment of Stratospheric Aerosol Properties (ASAP ) was published in 2006.
        </div>
        <div class="mb-2">
            Through these contributions, the {@render ssirc()} Scientific Steering Group (SSG) believes that {@render ssirc()} has proven to be
            an active and successful SPARC activity. However, it is clear that substantial work remains before we
            adequately understand stratospheric aerosol, their precursors, and feedback between stratospheric sulfur and
            climate resulting from the warming induced by increasing atmospheric carbon dioxide. For {@render ssirc()} to remain
            productive, it must be agile with respect to our changing understanding and to scientific priorities
            regarding our knowledge gaps, and committed to acting as a bridge between the measurement, process
            modelling, and the wider global climate modelling communities. This document summarizes where {@render ssirc()} is and
            where it is aiming to head as an activity
        </div>
        <h2 id="knowledge-gaps">Knowledge Gaps - Stratospheric Sulfur and Aerosol</h2>
        <div class="mb-2">
            While much is understood about the impact of stratospheric aerosol on climate, there are a number of open
            questions relevant to {@render ssirc()}, SPARC and the WCRP. For instance, a key knowledge gap is understanding the
            impact on climate of volcanic eruptions on scales from the modest eruptions observed since 2000 (e.g., Nabro
            in 2011) to eruptions with large stratospheric impact such as the 1991 eruption of Mt Pinatubo and the 1815
            eruption of Tambora. Another poorly understood area is the feedback between the global sulfur cycle and
            climate. For instance, while we generally understand the sources of biogenic sulfur for the stratosphere,
            significant gaps remain with virtually no understanding of how these contributions may change in a changing
            climate. Similarly, the contribution of human-derived SO2 to the stratospheric sulfur budget remains poorly
            quantified. How changes to the stratospheric sulfur burden, due to the changing climate and its impact on
            sulfur sources, feed back into circulation changes (particularly the Brewer-Dobson Circulation) is almost
            completely unknown. Finally, while it has long been known that sulfuric droplets dominate stratospheric
            aerosol composition, it is becoming clearer that other components such as nitrate aerosol,
            meteoritic-sulfuric aerosol, organics, soot, and, episodically, volcanic ash are likely relevant in the
            lower stratosphere and upper troposphere including. How this diverse composition impacts climate and how it
            can be characterized in climate models is not well understood.
        </div>
        <div class="mb-2">
            {@render ssirc()} addresses these knowledge gaps through directly stimulated activities and associations with related
            but independently managed projects. The following projects are presently active areas of work or subject of
            proposals currently underway, and have been at least partly stimulated by {@render ssirc()}.
        </div>

        <h2 id="ssirc-projects">{@render ssirc()} Projects</h2>
        <div class="mb-2">
            Estimating the climate impact of historical eruptions remains an on-going challenge. Work here is currently
            focused on investigating the radiative effects from historical major eruptions, particularly those in the
            post-1950s era, to address the sources of uncertainties in the capacity of current models to simulate the
            impacts of volcanic eruptions of very different scales. Outgrowths of this work include the Interactive
            Stratospheric Aerosol Model Intercomparison Project (ISA-MIP ) led by Valentina Aquila and Graham Mann. A
            closely related activity is focused on the recovery of historical data led by Juan Carlos Antuña. These data
            would contribute to new or updated volcanic forcing datasets and can provide observational constraints for
            interactive stratospheric aerosol models. The work is primarily focused on early lidar and searchlight data,
            but is also highlighting some of the early in situ data which are archived at NDACC. We encourage efforts to
            archive any recovered data at NDAAC or a similar facility, preferably with a DOI.
        </div>
        <div class="mb-2">
            VolRes , led by Jean-Paul Vernier and Claudia Timmreck, is focused on creating a document to describe
            activities recommended to follow a significant volcanic eruption. The idea is to have an easily accessible,
            and annually updated, document available for reference by observationalists and modelers which specifies a
            measurement and modeling strategy to promote the capture of the most important information in the short term
            following a major volcanic eruption. While this document could be generally described in a refereed
            publication, the ultimate goal is a living document since volcanic eruptions are not predictable and
            instrumentation, observational capabilities, and models are always in flux.
        </div>
        <div class="mb-2">
            Measured Sulfur Burden In the Stratosphere : Summarizing and reviewing the measured stratospheric sulfur
            burden is the goal of this effort which is led by Terry Deshler. The goals and commitments are to provide
            this review of both gas and particle phase sulfur.
        </div>
        <div class="mb-2">
            Volcanic Impact on Climate Index: {@render ssirc()} recognizes that VEI cannot adequately relate the impact of volcanic
            eruptions on climate. As a result, a new activity which is led by Landon Rieger and Matthew Toohey, was
            initiated to develop a simple index to convey the likely significance to climate due to the injection of
            sulfur into the stratosphere by a volcanic eruption.
        </div>
        <div class="mb-2">
            Database of data bases: At this point we are abandoning the idea of a wiki page hosting a list of sulfur and
            aerosol measurements. Partly this is due to the lukewarm response to the idea by the community and due to
            new EU regulations on data protection that would make such a wiki difficult to maintain. In lieu of the
            wiki, we will add a page to the {@render ssirc()} web site to promote key data sets available at data centers around the
            world.
        </div>
        <h2 id="associated-projects">Associated Projects</h2>
        <h3>
            Volcanic Model Intercomparison Project
        </h3>
        <div class="mb-2">
            The Model Intercomparison Project on the climatic response to Volcanic forcing (VolMIP) is a climate model
            intercomparison project that seeks to understand the wide discrepancy in various climate model responses to
            large eruptions that were observed in the CMIP5 comparisons. VolMIP is an endorsed MIP as part of CMIP6.
            VolMIP's key goal is to compare the response of the coupled ocean-atmosphere system in coupled climate
            models when the same strong volcanic forcing is applied.
        </div>
        <h3>Geoengineering Model Intercomparison Project</h3>
        <div class="mb-2">
            The Geoengineering Model Intercomparison Project (GeoMIP) addresses the effectiveness and perhaps
            unintended consequences of attempting to modify climate through a variety of radiation management schemes.
            Since a prominent geoengineering proposal is to modify sulfuric aerosol loading in the stratosphere, overlap
            between GeoMIP and {@render ssirc()} science interests is clear. GeoMIP is an endorsed MIP as part of CMIP6.
        </div>
        <h3>Balloon Measurement Campaigns of the Asian Tropopause Aerosol Layer</h3>
        <div class="mb-2">
            The Balloon Measurement Campaigns of the Asian Tropopause Aerosol Layer (BATAL) is a NASA-sponsored field
            campaign that aims to characterize the optical, physical, and chemical properties of the ATAL; assess its
            impacts on water vapor and ozone; and understand the role of convection in its formation. Insight into ATAL
            may lead to an improved understanding of the processes of aerosol and aerosol precursor transport into the
            stratosphere.
        </div>
        <h3>Stratéole 2</h3>
        <div class="mb-2">
            Stratéole 2 is an initiative to study the Tropical Tropopause Layer (TTL) and lower stratosphere using
            long-duration balloon platforms drifting near and within the TTL. The three ballooning campaigns planned
            between 2018 and 2024 present unique opportunities to make measurements of the physics and chemistry of the
            TTL from nearly Lagrangian platforms. In situ measurements of temperature, water vapor and cirrus profiles
            across the TTL and aerosol size distributions, ozone, and three dimensional winds in the lower stratosphere,
            just above the TTL, will advance scientific inquiries into the TTL concerning the role of gravity and
            equatorial wave dynamics, clouds and aerosols, stratospheric hydration, and the validation of satellite
            retrievals and model simulations.
        </div>
        <h3>Stratospheric and upper tropospheric processes for better climate predictions</h3>
        <div class="mb-2">
            Stratospheric and upper tropospheric processes for better climate predictions (StratoClim) seeks to improve
            the understanding of the microphysical, chemical and dynamical processes that determine the composition of
            the UTLS, such as the formation, loss and redistribution of aerosol, ozone and water vapor, and how these
            processes will be affected by climate change. An atmospheric observatory has been established on Palau and
            two successful aircraft campaigns have been carried out within StratoClim; one from Kalamata, Greece and one
            from Katmandu, Nepal.
        </div>
        <h3>Long Term Stratospheric Aerosol Datasets</h3>
        <div class="mb-2">
            The construction of long-term stratospheric aerosol forcing datasets for climate modeling has long been
            associated with SPARC stratospheric aerosol projects beginning with ASAP in 2006 and continuing with {@render ssirc()}.
            It consists of two components, a climatology of stratospheric aerosol optical properties primarily based on
            space missions (GloSSAC) and a climate forcing data set produced by ETH Zurich available at input for MIPS
            .
        </div>
        <h3>AEROCOM</h3>
        <div class="mb-2">
            The AEROCOM -project is focused on improving the understanding of global aerosol and its impact on climate.
            AEROCOM is primarily focused on tropospheric aerosol but a component is related to stratospheric and upper
            tropospheric aerosol observations.
        </div>
        <h2 id="new-projects">New Activities</h2>
        <div class="mb-2">
            The {@render ssirc()} SSG is committed to supporting these activities and others that advance an improved understanding
            of the role of stratospheric sulfur and aerosol. We will continue to consider the broad overall goal of
            understanding the sulfur cycle and its impact on stratospheric aerosol and to be self-critical as areas
            appear where knowledge is particularly deficient. Along these lines we encourage scientists to convey ideas
            for {@render ssirc()} activities to the {@render ssirc()} SSG. Promoting these activities through general workshops, topic-specific
            workshops, and other organizational support are all possible. Extending these ideas leads to the following
            areas which have been suggested as in need of future investigation.
        </div>
        <div class="mb-2">
            Strateole2, BATAL, StratoClim, and Asian Monsoon activities, are all focused on the UTLS because of the
            importance of this source region for the majority of material which maintains the non-volcanic stratospheric
            aerosol. The only material not controlled by the UTLS is meteoritic and material from explosive volcanic
            eruptions. {@render ssirc()} is committed to encourage these and other activities related to the role of the UTLS as a
            source region for stratospheric aerosol precursors including processes related to the Asian Monsoon,
            pyroCbs, and other regional processes which provide avenues for aerosol and aerosol precursor gases such as
            OCS, DMS, and organics to enter the stratosphere.
        </div>
        <h2 id="outreach">Extending Outreach</h2>
        <div class="mb-2">
            {@render ssirc()} needs to continue to reach out to the broader scientific community. This includes improving
            connectivity with other APARC activities such as the Atmospheric Composition and the Asian Monsoon (ACAM)
            activity and the emerging Observed Composition Trends and Variability in the Upper Troposphere and Lower
            Stratosphere (OCTAV-UTLS) activity. In addition, we seek improving connectivity to the ice core community
            perhaps through the International Partnership in Ice Core Sciences (IPICS). Also, improved communications
            with organizations like the International Association of Volcanology and Chemistry of the Earth's Interior
            (IAVCEI) and PAGES/VICS - Past Global Changes/Volcanic Impacts on Climate and Society could be beneficial,
            particularly as they relate to atmospheric emissions of SO2 and other sulfur species by volcanoes.
        </div>
        <div class="mb-2">
            We would also like to improve the diversity of the {@render ssirc()} Scientific Steering group and the membership
            as reflected in our email distribution list and in attendance at {@render ssirc()} and {@render ssirc()}-sponsored workshops. In
            particular, we would like to increase the presence of scientists from Asia, developing countries, women, and
            early career scientists. At the same time, we recognize that expanding our diversity may place greater
            demands on financial support in a period when support from APARC is increasingly limited. Part of outreach
            will require us to be more creative in how we acquire support in the future. We plan major updates to our
            web sites at SPARC and at {@render ssirc()} to reflect our commitment to diversity as well as our updated science focus
            and workshop planning.
        </div>
        <div class="mb-2">
            Meetings are a key part of making {@render ssirc()} a unique community. Workshops (both general and topical) allow
            unique gatherings where the state of the art of {@render ssirc()}-related science can be assessed. At the moment,
            another workshop on stratospheric aerosol in 2020 in Leeds, UK is envisioned. Topical workshops, such as the
            stratospheric aerosol measurement workshop in Boulder in 2018, are encouraged. Some possible topics include:
            VolRes, ISA-MIP, Historical data, and developing a new index to define the climate impact of volcanic
            eruptions. EGU and AGU sessions for topical {@render ssirc()} related activities are also encouraged.
        </div>
        <h2 id="references">References</h2>

        <div class="space-y-4">
            <BibEntry
                entry={bib["kremser2016"]} />
            <BibEntry
                entry={bib["timreck2018"]} />
            <BibEntry
                entry={bib["thomason2018"]} />
            <BibEntry
                entry={bib["zanchettin2016"]} />
        </div>
    </div>
</div>
