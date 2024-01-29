<script>
    import climate from "$lib/images/activities/gcm-cgi-primitive.svg";
    import pinatubo from "$lib/images/activities/puskurme-primitive.svg";
    import rescue from "$lib/images/activities/data-rescue-primitive.svg";
    import balloon from "$lib/images/activities/balloon-gondola-primitive.svg";
    import analysis from "$lib/images/activities/analysis-primitive.svg";
    import logo from "$lib/images/activities/implementation-plan-primitive.svg";
    import Activity from "$lib/components/Activity.svelte";
</script>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-8">
    <div>
        <Activity
            image={climate}
            title="Modelling"
            link="/activities/modelling"
            content="Stratospheric aerosol modeling activities" />
    </div>
    <div>
        <Activity
            image={pinatubo}
            title="VolRes"
            link="/activities/volres"
            content="Monitoring discussion for the next big eruption" />
    </div>
    <div>
        <Activity
            image={rescue}
            title="Data Rescue"
            link="/activities/data_rescue"
            content="Rediscovery and updates of past measurements" />
    </div>
    <div>
        <Activity
            image={balloon}
            title="Campaigns"
            link="/activities/campaigns"
            content="Past and upcoming balloon and aircraft campaigns" />
    </div>
    <div>
        <Activity
            image={analysis}
            title="Analysis"
            link="/activities/analysis"
            content="Analysis efforts to quantify stratospheric aerosols" />
    </div>
    <div>
        <Activity
            image={logo}
            title="Implementation"
            link="/implementation"
            content="Read about the SSiRC implementation plan" />
    </div>
</div>
