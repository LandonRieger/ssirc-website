<script>
    import Notification from "$lib/components/Notification.svelte";
    import sparc from "$lib/images/notifications/SPARC_logo.jpg";
    import stipmex from "$lib/images/notifications/STIPMEX_logo.png";

    let notifications = [
        {
            title: "Hunga-Tonga Workshop",
            content:
                "The 2nd open science workshop of the SPARC Hunga-Tonga impacts activity will be held in Paris April 22-24, 2024.",
            image: sparc,
            link: "https://sparc-ht24.sciencesconf.org/",
        },
        {
            title: "STIMPEX Workshop",
            content:
                "Stratosphere-Troposphere Interactions and Prediction of Monsoon weather EXtremes (STIPMEX) will be held in Pune on June 2-4, 2024",
            image: stipmex,
            link: "https://sparc-extreme.tropmet.res.in/",
        },
    ];
</script>
<!--<div class="shadow-md hover:shadow-lg border-1 border-gray-300 p-2 rounded-sm transition-all">-->

<div class="divide-y">
    {#each notifications as notification}
        <Notification
            title={notification.title}
            content={notification.content}
            image={notification.image}
            link={notification.link} />
    {/each}
</div>
