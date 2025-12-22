<script>
    import Notification from "$lib/components/Notification.svelte";
    import glossac from "$lib/images/notifications/glossac-v221.png";
    import hunga from "$lib/images/notifications/hunga-report.jpg";

    let notifications = [
        {
            title: "Hunga Report Published",
            content: "The WCRP report on the climatic impacts of the Hunga volcanic eruption has been published.",
            image: hunga,
            link: "https://www.wcrp-climate.org/news/wcrp-news/2381-hunga-tunga-report"
        },
        // {
        //     title: "OMPS-LP Aerosol version 2.5",
        //     content:
        //         "The NASA OMPS-LP stratospheric aerosol product version 2.5 has been released.",
        //     image: glossac,
        //     link: "https://www.earthdata.nasa.gov/data/catalog/ges-disc-omps-npp-lp-l2-aer-daily-2.5"
        // },
        {
            title: "GloSSAC v2.23",
            content:
                "The Global Space-based Stratospheric Aerosol Climatology has been updated through the end of 2024.",
            image: glossac,
            link: "https://asdc.larc.nasa.gov/project/GloSSAC",
        },
    ];
</script>

<div class="space-y-4">
    {#each notifications as notification}
        <Notification
            title={notification.title}
            content={notification.content}
            image={notification.image}
            link={notification.link} />
    {/each}
</div>
