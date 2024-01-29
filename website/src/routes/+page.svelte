<script>
    import NotificationList from "$lib/components/NotificationList.svelte";
    import ActivityPage from "$lib/components/ActivityPage.svelte";
    import RelatedInitiatives from "$lib/components/RelatedInitiatives.svelte";
    import UpdatesList from "$lib/components/UpdatesList.svelte";
</script>

<div class="w-full">
    <div class="sm:flex sm:flex-row">
        <div class="grow mr-4">
            <div class="text-lg font-light">
                <span class="font-semibold">SSiRC</span> is an established APARC (Atmospheric Processes And their Role in
                Climate) activity, with APARC being a core project within the World Climate Research Program (WCRP). SSiRC
                aims to foster collaboration across observational and modelling groups to better understand the stratospheric
                aerosol layer and the drivers for its observed variations.
            </div>
            <ActivityPage />
        </div>

        <div class="sm:w-96 sm:flex-none mx-4">
            <div class="font-bold text-gray-500 uppercase mb-4">Upcoming Meetings</div>
            <NotificationList />
            <div class="font-bold text-gray-500 uppercase my-4">Research Highlights</div>
            <UpdatesList/>
            <div class="font-bold text-gray-500 uppercase my-4">Related Initiatives</div>
        <RelatedInitiatives />

        </div>
    </div>

<!--    <div>-->
<!--        <div class="row mt-4">-->
<!--            <div class="font-bold text-gray-500 uppercase mb-2">Related Initiatives</div>-->
<!--        </div>-->
<!--        <RelatedInitiatives />-->
<!--    </div>-->
</div>
