<script>
    import Question from "$lib/components/questions/Question.svelte";
    let { refs } = $props();
    const title =
        "What are, quantitatively, the impacts on radiative forcing and stratospheric chemistry, of particles transported upward or formed in pyroconvective plumes?";
</script>

<Question {title}>
    <div>
        Natural processes play an important role in the global sulfur cycle. Different sulfur compounds are emitted or
        taken up by vegetation, soils, the oceans and wildfires. Climate change induces significant changes to and in
        many ecosystems and may thus alter natural sulfur fluxes substantially. A quantitative understanding of these
        processes and fluxes is necessary to predict such changes and possible climate feedbacks.
    </div>
</Question>
