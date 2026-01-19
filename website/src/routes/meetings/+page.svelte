<script>
    import { Listgroup } from "flowbite-svelte";

    let links = [
        { name: "2022 SSiRC Workshop", href: "#leeds" },
        { name: "2021 Virtual Meeting", href: "#virtual" },
        { name: "2018 Chapman Conference", href: "#chapman" },
        { name: "2018 Measurement Workshop", href: "#measurement" },
        { name: "2016 SSiRC Workshop", href: "#potsdam" },
        { name: "2013 SSiRC Workshop", href: "#atlanta" },
    ];
</script>

<div class="flex w-full">
    <div class="flex-none hidden w-64 xl:text-sm xl:block end-0">
        <div class="flex overflow-y-auto sticky top-20 flex-col justify-between pb-6 mr-6 h-[calc(100vh-5rem)]">
            <div>
                <p class="uppercase font-medium text-gray-700 mb-4">On this page</p>

                <Listgroup active items={links} >
                    {#snippet children({ item })}
                                        {item.name}
                                                        {/snippet}
                                </Listgroup>
            </div>
        </div>
    </div>

    <div class="flex flex-col">
        <h1>Meetings</h1>
        <h2 id="leeds">2022 SSiRC Workshop</h2>
        <p class="text-sm font-light italic">March 2022, Leeds, UK</p>
        <p>
            The 3<sup>rd</sup> International SSiRC Workshop has now been confirmed for 16-18 May 2022 in Leeds, UK.
            Visit the conference website
            <a href="https://eu.eventscloud.com/ehome/200197691/home/" class="text-blue-700">here</a> for updates and details.
        </p>

        <h2 id="virtual">2021 Virtual Meeting</h2>
        <p class="text-sm font-light italic">27-20 September 2021</p>
        <p>
            In September 2021, SSiRC hosted its first virtual conference with more than 100 participants. In three
            sessions, recent and ongoing studies related to sulfur and stratospheric aerosol were presented and
            discussed. A complete list of 39 presentations with titles is found
            <a href="http://www.sparc-ssirc.org/pics/SSiRC_VirtualMeeting2021_Schedule.pdf" class="text-blue-700">here</a>.
        </p>

        <h2 id="tenerife">Stratospheric aerosol in the post-Pinatubo era: Processes, Interactions, and Importance</h2>
        <p class="text-sm font-light italic">18-23, March 2018, Tenerife, Spain</p>
        <p>
            <a href="http://www.sparc-ssirc.org/downloads/Chapman_Talks.7z" class="text-blue-700">Download the presentations</a>
        </p>
        <p>
            <a href="http://www.sparc-ssirc.org/downloads/Chapman_Posters.7z" class="text-blue-700">Download the posters</a>
        </p>

        <p>
            Stratospheric aerosol, a persistent yet highly variable component of the stratosphere, has impacts on
            radiation and stratospheric ozone, and thus climate. Since the 1960s the study of stratospheric aerosol has
            been substantially influenced by the large volcanic eruptions of: Agung, Fuego, El Chichón, and Pinatubo.
            This paradigm of decadal major volcanic eruptions changed after Pinatubo in 1991. Since then, no volcanic
            eruptions have had similar magnitudes and in most cases the stratospheric signature was lost within one
            year. The period following Pinatubo to the present overlaps with a golden age for stratospheric aerosol and
            gas phase sulfur measurements from satellites, aircraft, balloons, and the ground, representing an optimum
            period for testing climate models that use prescribed stratospheric aerosol and gas phase sulfur, and those
            that use surface emissions and calculate stratospheric aerosol and gas phase sulfur. Historically such a
            period of quiescent to mild volcanism is perhaps more common than the active volcanism of the 1960s through
            the 1990s, and is more suited to study troposphere-to-stratosphere transport, background stratospheric
            chemistry, trends in stratospheric sulfate aerosol, and the sources and potential climate impact of
            non-sulfate stratospheric aerosol. This Chapman Conference will be focused on addressing the following
            scientific questions that have grown out of this period of observations.
        </p>
        <ol>
            <li>
                What sources (volcanic, natural non-volcanic, and anthropogenic) and processes have controlled
                stratospheric aerosol levels since the decay of the Mt. Pinatubo aerosol?
            </li>
            <li>
                How do the observed variations in stratospheric aerosol, over the recent quiescent and mild volcanic
                period, impact climate and the composition of the stratosphere?
            </li>
            <li>
                How well do we understand the sulfur budget over the ?golden period? of stratospheric observations, in
                the post-Pinatubo era?
            </li>
            <li>
                What is the role of non-sulfate aerosol in the stratosphere and how much does it change the current
                sulfate-dominated picture of stratospheric aerosol?
            </li>
            <li>
                How well do the global aerosol climatologies, derived primarily from satellite measurements, capture the
                climate relevant quantities during the quiescent to mild volcanic period?
            </li>
            <li>How well do models represent the stratospheric aerosol over quiescent to mild volcanic periods?</li>
        </ol>

        <h2 id="boulder">Workshop on the Measurement of Stratospheric Aerosol</h2>
        <p class="text-sm font-light italic">September 6-8, 2017, Boulder, Colorado</p>
        <p>
            SPARC's Stratospheric Sulfur and its Role in Climate (SSiRC) activity is sponsoring a workshop focused on
            facilitating communications and collaborations among scientists responsible for observations of
            stratospheric aerosol by in situ, ground-based and space-based instruments. Key goals are to develop
            strategies for understanding and closing differences among instruments, and for characterizing the
            continuity of the measurement record as instruments and measurement paradigms change, while keeping in mind
            the end goal of providing data users, particularly the climate modeling community, more robust and
            better-characterized data sets than normally obtained from single instruments. As such, it will consist of a
            few invited talks and substantial time set aside for group discussions. We hope that participants will
            develop ideas for collaborative projects and, perhaps, proposal ideas. We will summarize meeting outcomes in
            the SPARC Newsletter.
        </p>
        <p>
            Given the nature of the workshop, attendance will be limited to about 25, with some allowance for students
            and early career scientists. If you are interested in attending, please contact the conveners. If you wish
            to make a presentation, please include a synopsis in your email. We will distribute the synopses to
            attendees prior to the workshop. The workshop is scheduled for September 6 to 8th at Laboratory for
            Atmospheric and Space Physics (LASP) in Boulder, Colorado. A modest registration fee is expected. More
            details about the meeting location and schedule will be forthcoming.
        </p>

        <h2 id="potsdam">2016 SSiRC Workshop</h2>
        <p class="text-sm font-light italic">25-28 April 2016, Potsdam, Germany</p>
        <p>
            2nd SSiRC Workshop took place 25-28 April 2016 in Potsdam, Germany. The meeting was very well sought with
            over 70 participants. Presentations from the workshop are now downloadable
            <a href="http://www.sparc-ssirc.org/downloads/potsdam2016/present_potsdam_2016.html" class="text-blue-700">here</a>!
        </p>

        <h2 id="atlanta">2013 SSiRC Workshop</h2>
        <p class="text-sm font-light italic">28-30 October 2013, Atlanta, Georgia</p>
        <p>
            Presentations are available for download <a href="http://www.sparc-ssirc.org/data/downloads.html" class="text-blue-700">here</a>.
        </p>
    </div>
</div>
