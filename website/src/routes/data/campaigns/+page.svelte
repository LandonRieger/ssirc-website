<script>
    import BalloonCampaigns from "$lib/components/BalloonCampaigns.svelte";
    import data from "$lib/data/campaign_data.json";
    import { Card } from "flowbite-svelte";
    import ISSIAcknowledgement from "$lib/components/ISSIAcknowledgement.svelte";
</script>

<Card size="xl">
    <div class="pb-4">
        Click on a row to see more detailed information about a campaign. If you would like to add additional
        information to this table please contact
        <a class="text-blue-500" href="mailto:jeanpaul.vernier@nasa.gov">Jean-Paul Vernier</a>.
    </div>
    <BalloonCampaigns {data} />
</Card>
<ISSIAcknowledgement/>