<script>
    import Notification from "$lib/components/Notification.svelte";
    import glossac from "$lib/images/notifications/glossac-v221.png";

    let notifications = [
        {
            title: "GloSSAC v2.21",
            content:
                "The Global Space-based Stratospheric Aerosol Climatology has been updated through the end of 2022.",
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
