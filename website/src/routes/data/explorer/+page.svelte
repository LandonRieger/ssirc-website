<script>
    import ParticleSize from "$lib/components/graphics/balloon/ParticleSize.svelte";
    import { Alert, Card } from "flowbite-svelte";
    import ISSIAcknowledgement from "$lib/components/ISSIAcknowledgement.svelte";
</script>

<ParticleSize />
<ISSIAcknowledgement />

<Alert class="bg-gray-50 mt-4">
    <div>
    If you would like to add additional flight data to this explorer please contact <a
        class="text-blue-500"
        href="mailto:landon.rieger@ec.gc.ca">Landon Rieger</a
    >.
</div>
</Alert>