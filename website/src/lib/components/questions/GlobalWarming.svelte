<script>
    import Question from "$lib/components/questions/Question.svelte";
    let { refs } = $props();
    const title =
        "What role does global climate warming play in modifying the stratospheric aerosol lifecycle and its associated aerosol radiative forcing?";
</script>

<Question {title}>
    <div>
        Global warming alters the thermal structure and circulation of the upper atmosphere, which in turn alters the
        stratospheric aerosol lifecycle and the magnitude of aerosol radiative forcing {@html refs.cite("aubry2022")}.
        Using climate model simulations, {@html refs.citet("aubry2021")} showed that a higher future tropopause means
        moderate-magnitude tropical eruptions inject proportionally less sulfur into the stratosphere, reducing
        stratospheric aerosol optical depth by about 75% in a high-end warming scenario. Plume-rise height from
        less-frequent large-magnitude eruptions on the contrary increases under global warming, which together with an
        acceleration of the Brewer–Dobson circulation has been suggested to produce smaller-sized sulfate particles and
        thus a larger global-mean radiative forcing compared to present-day. Overall, our understanding of the role of
        climate change in altering volcanic aerosol–climate interactions is still limited and requires further research
        also in the context of SAI.
    </div>
</Question>
