<script>
    import { Tooltip } from "flowbite";

    let initiatives = [
        {
            name: "VolMIP",
            description:
                "CMIP6 endorsed project with the aim to coordinate the activities of different research institutes involved in numerical climate modelling focused on a multi-model assessment of climate model performance under strong volcanic forcing conditions",
            short: "Volcanic Modelling Intercomparison Project",
            href: "http://www.volmip.org/",
        },
        {
            name: "GeoMIP",
            description:
                "Serves to organize geoengineering simulations by prescribing the experiments which all participating climate models will perform.",
            short: "Geoengineering Modelling Intercomparison Project",
            href: "http://climate.envsci.rutgers.edu/GeoMIP/index.html",
        },
        {
            name: "PAGES VICS",
            description:
                "Supports research focused on reconstructing the history of past explosive volcanism, and research using this knowledge to better understand how the climate system responds to changes in radiative forcing, and how societies have been impacted by and responded to the resulting climatic changes.",
            short: "Volcanic Impacts on Climate and Society",
            href: "http://www.pastglobalchanges.org/science/wg/vics/intro",
        },
        {
            name: "OCTAV-UTLS",
            short: "Observed Composition Trends And Variability in the Upper Troposphere and Lower Stratosphere",
            href: "https://www.octav-utls.net/",
        },
        {
            name: "ACAM",
            short: "Atmopsheric Composition and the Asian Monsoon",
            href: "https://www2.acom.ucar.edu/acam",
        },
        {
            name: "CCMI",
            description:
                "The Chemistry Climate Model Initiative (CCMI) seeks to improve our understanding of the role of chemistry-climate interactions within the Earth system in the past, the present, and in future projections.",
            short: "Chemistry Climate Model Initiative",
            href: "https://igacproject.org/activities/CCMI",
        },
        {
            name: "HTHH Impacts",
            description: "The Hunga Tonga-Hunga Ha’apai Impacts activity was established by SPARC (Stratosphere-troposphere Processes And their Role in Climate) to examine impacts of the Hunga Tonga-Hunga Ha’apai (HTHH) eruption of January 2022.",
            short: "Hunga Tonga-Hunga Ha’apai Impacts Report",
            href: "https://csl.noaa.gov/assessments/hthh/"
        }
    ];
</script>

<div class="shadow-md p-4">
<!--<div class="grid grid-cols-2 gap-x-4 gap-y-1">-->
<div class="">
    {#each initiatives as activity}
        <a id={activity.name} class="font-bold text-sm text-gray-700" href={activity.href}>
            {activity.name}
        </a>
        <div class="text-xs pb-2">
            {activity.short}
        </div>
    {/each}
</div>
</div>