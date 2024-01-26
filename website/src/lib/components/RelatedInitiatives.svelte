<script>
    import { Popover } from "flowbite";

    let initiatives = [
        {
            name: "VolMIP",
            description:
                "CMIP6 endorsed project with the aim to coordinate the activities of different research institutes involved in numerical climate modelling focused on a multi-model assessment of climate model performance under strong volcanic forcing conditions",
            href: "http://www.volmip.org/",
        },
        {
            name: "GeoMIP",
            description:
                "Serves to organize geoengineering simulations by prescribing the experiments which all participating climate models will perform.",
            href: "http://climate.envsci.rutgers.edu/GeoMIP/index.html",
        },
        {
            name: "PAGES VICS",
            description:
                "Supports research focused on reconstructing the history of past explosive volcanism, and research using this knowledge to better understand how the climate system responds to changes in radiative forcing, and how societies have been impacted by and responded to the resulting climatic changes.",
            href: "http://www.pastglobalchanges.org/science/wg/vics/intro",
        },
        {
            name: "OCTAV-UTLS",
            description: "Observed Composition Trends And Variability in the Upper Troposphere and Lower Stratosphere",
            href: "https://www.octav-utls.net/",
        },
        {
            name: "ACAM",
            description: "Atmopsheric Composition and the Asian Monsoon",
            href: "https://www2.acom.ucar.edu/acam",
        },
        {
            name: "CCMI",
            description: "Chemistry-Climate Model Initiative",
            href: "https://igacproject.org/activities/CCMI",
        },
    ];
</script>

<div>
    <div class="flex flex-row justify-between">
        {#each initiatives as activity}
            <div class="w-40 border border-gray-300 text-center text-xl text-gray-700">
                {activity.name}
            </div>
        {/each}
    </div>
</div>
