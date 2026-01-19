<script>
    import Question from "$lib/components/questions/Question.svelte";
    let { refs } = $props();
    const title = "How well are upper tropospheric and stratospheric aerosols represented in global climate models, which are critical for our confidence in climate projections?"

</script>

<Question {title}>
    <div>
        With more types of upper tropospheric and stratospheric aerosols being detected and measured remotely and
        in-situ, there is a need to consider their various roles in the climate system. Currently, most climate models
        consider only sulfate aerosol in the stratosphere. More evidence now shows the potential importance of meteoric
        dust, aerosols from satellite reentry and rocket launches, organics, ammonium and nitrate aerosols to be
        included in aerosol simulations in the climate models. Those non-sulfate particles are important to understand
        the stratospheric aerosol composition, microphysical properties, and their radiative and chemical impacts.
    </div>
</Question>
