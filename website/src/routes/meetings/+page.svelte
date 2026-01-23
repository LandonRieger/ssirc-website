<script>
    // import { Listgroup } from "flowbite-svelte";
    import ListGroup from "$lib/components/ListGroup.svelte";
    import Link from "$lib/components/Link.svelte";
    import Meeting from "./Meeting.svelte";
    let links = [
        { label: "2025 SAI Workshop", id: "sai" },
        { label: "2024 STIPMEX Workshop", id: "stipmex" },
        { label: "2022 SSiRC Workshop", id: "leeds" },
        { label: "2021 Virtual Meeting", id: "virtual" },
        { label: "2018 Chapman Conference", id: "chapman" },
        { label: "2018 Measurement Workshop", id: "measurement" },
        { label: "2016 SSiRC Workshop", id: "potsdam" },
        { label: "2013 SSiRC Workshop", id: "atlanta" },
    ];
</script>

<div class="flex w-full">
    <div class="w-64 flex-none">
        <ListGroup {links}></ListGroup>
    </div>
    <div class="flex flex-col">
        <h1>Meetings</h1>
        <Meeting
            title="Virtual Workshop Series on Stratospheric Aerosol Injection (SAI)"
            subtitle="6-9 October 2025"
            id="sai">
            <p>
                Over four intensive days, more than 200 participants from around the globe came together for the <Link
                    href="https://www.wcrp-climate.org/ci-workshop-series-sai"
                    >Virtual Workshop Series on Stratospheric Aerosol Injection (SAI)
                </Link>, hosted by the WCRP Lighthouse Activity- Research on Climate Intervention and the Core Activity
                “Atmospheric Processes and their Role in Climate”. Featuring 52speakers, the event provided a lively
                forum for in-depth discussions on SAI, a proposed climate intervention that would aim to reduce the
                impacts of global warming through the injection of reflective particles in the stratosphere. As this
                topic becomes more widely discussed, it is important that robust scientific discussions are had to
                better identify potential risks and impacts of SAI across different scenarios, to understand and reduce
                uncertainties in future projections using Earth System Models, and to address SAI science questions
                using small scale deployment that may not be answered by studying natural analogues only
            </p>
            <p>
                The workshops explored a wide range of topics, from observational strategies and modeling of
                stratospheric aerosols to climatic, societal, and ecological impacts, as well as the ethical
                considerations of studying and testing SAI. Participants shared the latest research, debated potential
                risks and uncertainties, and considered strategies for robust monitoring and simulation of future
                scenarios.
            </p>
            <p>
                By fostering an inclusive, international dialogue, the series emphasized collaboration across
                observational and modeling communities, aiming to advance our understanding of Earth system responses to
                climate interventions and inform evidence-based policy and governance.
            </p>
        </Meeting>

        <Meeting title="2024 STIPMEX Workshop" subtitle="June 2-7 2024, Pune, India" id="stipmex">
            <p>
                An International workshop on <Link href="https://sparc-extreme.tropmet.res.in/">
                    Stratosphere-Troposphere Interactions and Prediction of Monsoon weather EXtremes (STIPMEX)</Link> will
                foster all observational/modelling aspects of the stratosphere-troposphere coupling processes and extreme
                weather events associated with Asian summer monsoon. The workshop will provide a platform for discussions
                on dynamical, chemical, radiative and convective processes of the atmosphere during the Asian summer monsoon.
                It will particularly emphasize on the recent changes/trends in stratosphere-troposphere coupling process,
                linkages of stratospheric process/volcanic eruptions with the Asian summer monsoon. The challenges of forecasting
                extreme weather events during Asian summer monsoon will also be deliberated upon. The workshop will also
                showcase the new initiatives and insights for future pathways of forecasting extremes along with stakeholder
                discussions. There will be a one-day pre-workshop training session for students and early career scientists/professionals
                on latest data analysis techniques.
            </p>
        </Meeting>
        <Meeting title="2022 SSiRC Workshop" subtitle="March 2022, Leeds, UK" id="leeds">
            <p>
                The 3<sup>rd</sup> International SSiRC Workshop has now been confirmed for 16-18 May 2022 in Leeds, UK.
                Visit the conference website
                <a href="https://eu.eventscloud.com/ehome/200197691/home/" class="text-blue-700">here</a> for updates and
                details.
            </p>
        </Meeting>

        <Meeting title="2021 Virtual Meeting" subtitle="17-20 September 2021" id="virtual">
            <p>
                In September 2021, SSiRC hosted its first virtual conference with more than 100 participants. In three
                sessions, recent and ongoing studies related to sulfur and stratospheric aerosol were presented and
                discussed. A complete list of 39 presentations with titles is found
                <a href="http://www.sparc-ssirc.org/pics/SSiRC_VirtualMeeting2021_Schedule.pdf" class="text-blue-700"
                    >here</a
                >.
            </p>
        </Meeting>

        <Meeting
            title="Stratospheric aerosol in the post-Pinatubo era: Processes, Interactions, and Importance"
            subtitle="18-23, March 2018, Tenerife, Spain"
            id="tenerife">
            <p>
                <a href="http://www.sparc-ssirc.org/downloads/Chapman_Talks.7z" class="text-blue-700"
                    >Download the presentations</a>
            </p>
            <p>
                <a href="http://www.sparc-ssirc.org/downloads/Chapman_Posters.7z" class="text-blue-700"
                    >Download the posters</a>
            </p>

            <p>
                Stratospheric aerosol, a persistent yet highly variable component of the stratosphere, has impacts on
                radiation and stratospheric ozone, and thus climate. Since the 1960s the study of stratospheric aerosol
                has been substantially influenced by the large volcanic eruptions of: Agung, Fuego, El Chichón, and
                Pinatubo. This paradigm of decadal major volcanic eruptions changed after Pinatubo in 1991. Since then,
                no volcanic eruptions have had similar magnitudes and in most cases the stratospheric signature was lost
                within one year. The period following Pinatubo to the present overlaps with a golden age for
                stratospheric aerosol and gas phase sulfur measurements from satellites, aircraft, balloons, and the
                ground, representing an optimum period for testing climate models that use prescribed stratospheric
                aerosol and gas phase sulfur, and those that use surface emissions and calculate stratospheric aerosol
                and gas phase sulfur. Historically such a period of quiescent to mild volcanism is perhaps more common
                than the active volcanism of the 1960s through the 1990s, and is more suited to study
                troposphere-to-stratosphere transport, background stratospheric chemistry, trends in stratospheric
                sulfate aerosol, and the sources and potential climate impact of non-sulfate stratospheric aerosol. This
                Chapman Conference will be focused on addressing the following scientific questions that have grown out
                of this period of observations.
            </p>
            <ul>
                <li>
                    What sources (volcanic, natural non-volcanic, and anthropogenic) and processes have controlled
                    stratospheric aerosol levels since the decay of the Mt. Pinatubo aerosol?
                </li>
                <li>
                    How do the observed variations in stratospheric aerosol, over the recent quiescent and mild volcanic
                    period, impact climate and the composition of the stratosphere?
                </li>
                <li>
                    How well do we understand the sulfur budget over the ?golden period? of stratospheric observations,
                    in the post-Pinatubo era?
                </li>
                <li>
                    What is the role of non-sulfate aerosol in the stratosphere and how much does it change the current
                    sulfate-dominated picture of stratospheric aerosol?
                </li>
                <li>
                    How well do the global aerosol climatologies, derived primarily from satellite measurements, capture
                    the climate relevant quantities during the quiescent to mild volcanic period?
                </li>
                <li>How well do models represent the stratospheric aerosol over quiescent to mild volcanic periods?</li>
            </ul>
        </Meeting>

        <Meeting
            title="Workshop on the Measurement of Stratospheric Aerosol"
            subtitle="September 6-8, 2017, Boulder, Colorado"
            id="boulder">
            <p>
                SPARC's Stratospheric Sulfur and its Role in Climate (SSiRC) activity is sponsoring a workshop focused
                on facilitating communications and collaborations among scientists responsible for observations of
                stratospheric aerosol by in situ, ground-based and space-based instruments. Key goals are to develop
                strategies for understanding and closing differences among instruments, and for characterizing the
                continuity of the measurement record as instruments and measurement paradigms change, while keeping in
                mind the end goal of providing data users, particularly the climate modeling community, more robust and
                better-characterized data sets than normally obtained from single instruments. As such, it will consist
                of a few invited talks and substantial time set aside for group discussions. We hope that participants
                will develop ideas for collaborative projects and, perhaps, proposal ideas. We will summarize meeting
                outcomes in the SPARC Newsletter.
            </p>
            <p>
                Given the nature of the workshop, attendance will be limited to about 25, with some allowance for
                students and early career scientists. If you are interested in attending, please contact the conveners.
                If you wish to make a presentation, please include a synopsis in your email. We will distribute the
                synopses to attendees prior to the workshop. The workshop is scheduled for September 6 to 8th at
                Laboratory for Atmospheric and Space Physics (LASP) in Boulder, Colorado. A modest registration fee is
                expected. More details about the meeting location and schedule will be forthcoming.
            </p>
        </Meeting>

        <Meeting title="2016 SSiRC Workshop" subtitle="25-28 April 2016, Potsdam, Germany" id="potsdam">
            <p>
                2nd SSiRC Workshop took place 25-28 April 2016 in Potsdam, Germany. The meeting was very well sought
                with over 70 participants. Presentations from the workshop are now downloadable
                <a
                    href="http://www.sparc-ssirc.org/downloads/potsdam2016/present_potsdam_2016.html"
                    class="text-blue-700">here</a
                >!
            </p>
        </Meeting>

        <Meeting title="2013 SSiRC Workshop" subtitle="28-30 October 2013, Atlanta, Georgia" id="atlanta">
            <p>
                Presentations are available for download <a
                    href="http://www.sparc-ssirc.org/data/downloads.html"
                    class="text-blue-700">here</a
                >.
            </p>
        </Meeting>
    </div>
</div>
