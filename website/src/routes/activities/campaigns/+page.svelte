<script>
    import Person from "$lib/components/Person.svelte";
    import { Listgroup } from "flowbite-svelte";

    let links = [
        { name: "KLAsh", href: "#klash" },
        { name: "BATAL", href: "#batal" },
        { name: "SWOP", href: "#swop" },
        { name: "StratoClim", href: "#stratoclim" },
        { name: "Stratéole-2", href: "#strateole2" },
    ];
</script>

<div class="flex w-full">
    <div class="flex-none hidden w-64 xl:text-sm xl:block end-0">
        <div class="flex overflow-y-auto sticky top-20 flex-col justify-between pb-6 mr-6 h-[calc(100vh-5rem)]">
            <div>
                <p class="uppercase font-medium text-gray-700 mb-4">On this page</p>

                <Listgroup active items={links} let:item>
                    {item.name}
                </Listgroup>
            </div>
        </div>
    </div>
    <div class="flex flex-col">
        <h1>Field Campaigns</h1>

        <h2 id="klash">KLAsh: Rapid Response to Volcanic Eruption</h2>
        <Person name="Jean Paul Vernier" />
        <Person name="T. D. Fairlie" />
        <Person name="Terry Deshler" />
        <p>
            Increased volcanic activity over the past decade is thought to have contributed significantly to the recent
            global warming 'hiatus'. Thus, it is important to improve our understanding of the microphysical and optical
            properties of even small volcanic plumes as well as their associated climate impacts. On February 13th,
            2014, the Mt. Kelud volcano, located near 4°S on the island of Java (Indonesia), injected volcanic gases and
            ash into the tropical stratosphere. An overpass of the CALIPSO lidar during the active phase of the eruption
            showed volcanic materials reaching 26 km with the main volcanic cloud near 18-19 km. CALIPSO tracked the
            dispersion of the Kelud plume throughout the tropical lower stratosphere (~20°N-20°) and showed the
            persistence of small ash particles a month after the eruption. This is significant because the climate
            impact of ash is neglected in most climate models.
        </p>
        <p>
            In May 2014, a team of NASA and University of Wyoming scientists mounted a 2-week balloon field campaign to
            Darwin (Australia) to characterize the optical properties, sulfate fraction and particle sizes of the
            stratospheric plume from Mt. Kelud, while it remained relatively fresh. They conducted 4 launches of
            backscatter sondes with red and blue channels under small balloons, and a single launch of two optical
            particle counters, one with an inlet heated to 200°C, under a large balloon, to characterize aerosol size
            and volatility. Preliminary results from the campaign indicated 2 layers between 18 and 21 km and suggested
            the persistence of ash particles in the lower layer of the Kelud plume 3 months after the eruption.
        </p>

        <h2 id="batal">BATAL-2014: Balloon characterization of the Asian Tropopause Aerosol Layer</h2>
        <Person name="Jean Paul Vernier" />
        <Person name="Jaya Rayaman" />

        <p>
            Satellite observations have recently shown that the Summer Asian Monsoon leads to the formation of an
            aerosol layer in the upper troposphere extending from the Eastern Mediterranean Sea to Western China.
            Firstly discovered by analyzing data from the CALIPSO space-borne lidar and recently confirmed by past
            SAGE-II limb observations, this Asian Tropopause Aerosol Layer (ATAL) seems to be the main source of
            aerosols in the tropical upper troposphere during volcanic quiescent periods. Analysis of long-term
            satellite observations suggests the emergence of this feature since the beginning 2000's, representing a new
            source of radiative forcing for the Asian Region which could potentially alters the earth energy balance.
        </p>
        <p>
            A balloon field campaign was mounted to characterize the aerosol optical properties and size distribution of
            the Asian Tropopause Aerosol Layer (ATAL). The objective of this mission was to better understand the role
            of convection over the Indian sub-continent in the formation of the ATAL. A 10-day field experiment between
            15-27 August 2014, based in Gadanki (13.4°N,71.2°E, India) at the National Atmospheric Research Laboratory
            (NARL), has deployed 7 flights of a two-wavelength aerosol backscatter sonde and one Optical Particle
            Counter configured for light weather balloons.
        </p>
        <p>
            The balloon campaign was supported by intensive ground-based lidar and radar measurements. In addition, a
            similar balloon field campaign took place from Kunming (China). Altogether, those deployments represent the
            most significant effort to date in order to better understand the nature, origin and formation of the ATAL
            throughout Asia.
        </p>

        <h2 id="swop">SWOP - A Sounding water vapor, ozone and particle campaign</h2>
        <Person name="Jianchun Bian" />
        <Person name="Frank Weinhold" />
        <p>
            A sounding water vapor, ozone and particle (SWOP) campaign has been conducted every year at Kunming (25°N,
            102.6°E, China) or Lhasa (30°N, 91°E, China) during the Asian summer monsoon (ASM) since 2009, with an aim
            to investigate the tropopause transition layer within the ASM anticyclone. A combined measurement of water
            vapor by frost-point hygromemeter (CFH or FPH) and particle by two-wavelength aerosol backscatter sonde
            (COBALD) can provide the detailed information about cirrus and aerosol layer. Totally, there are 21 combined
            soundings (3 cases in August 2010, 18 cases in August 2013) from Lhasa, and 22 soundings (12 cases in August
            2012, 10 cases in August 2014). These balloon-borne soundings will provide in-situ observation of aerosol
            and related measurements in order to better understand the nature, origin and formation of the ATAL
            throughout Asia.
        </p>

        <h2 id="stratoclim">StratoClim</h2>
        <Person name="PD Dr. Markus Rex" />

        <p>Stratospheric and upper tropospheric processes for better climate predictions</p>
        <div>
            StratoClim will produce more reliable projections of climate change and stratospheric ozone by a better
            understanding and improved representation of key processes in the Upper Troposphere and Stratosphere (UTS).
            This will be achieved by an integrated approach bridging observations from dedicated field activities,
            process modelling on all scales, and global modelling with a suite of chemistry climate models (CCMs) and
            Earth system models (ESMs). At present, complex interactions and feedbacks are inadequately represented in
            global models with respect to natural and anthropogenic emissions of greenhouse gases, aerosol precursors
            and other important trace gases, the atmospheric dynamics affecting transport into and through the UTS, and
            chemical and microphysical processes governing the chemistry and the radiative properties of the UTS.
            StratoClim will
        </div>
        <ul class="list-disc list-inside pb-2">
            <li>
                improve the understanding of the microphysical, chemical and dynamical processes that determine the
                composition of the UTS, such as the formation, loss and redistribution of aerosol, ozone and water
                vapour, and how these processes will be affected by climate change;
            </li>
            <li>
                implement these processes and fully include the interactive feedback from UTS ozone and aerosol on
                surface climate in CCMs and ESMs
            </li>
        </ul>
        <p>Through StratoClim new measurements will be obtained in key regions:</p>
        <ul class="list-disc list-inside pb-2">
            <li>
                in a tropical campaign with a high altitude research aircraft carrying an innovative and comprehensive
                payload,
            </li>
            <li>by a new tropical station for unprecedented ground and sonde measurements, and</li>
            <li>through newly developed satellite data products.</li>
        </ul>
        <p>
            The improved climate models will be used to make more robust and accurate predictions of surface climate and
            stratospheric ozone, both with a view to the protection of life on Earth. Socioeconomic implications will be
            assessed and policy relevant information will be communicated to policy makers and the public through a
            dedicated office for communication, stakeholder contact and international co-operation.
        </p>

        <h2 id="strateole2">Stratéole-2</h2>
        <Person name="Albert Hertzog" />
        <Person name="Stephanie Venel" />
        <Person name="Ed Weave" />

        <p>Strat (stratospheric) éole (winds) in the tropics</p>
        <div>
            Strateole-2 is a French-US project to study climate processes in the tropical tropopause layer (TTL) and in
            the lower stratosphere. The project originality arises from the use of CNES superpressure balloons capable
            of drifting for several months between 18 and 20 km altitude. These platforms will be used to make highly
            resolved in situ measurements of winds, temperature, pressure, water vapor, ozone, carbon dioxide, and
            aerosol/clouds; and remote measurements of cirrus, upwelling radiation, and temperature. Strateole-2 will
            release a total of nearly 50 long-duration balloons in three separate campaigns between 2019 and 2024.
            Balloons are released from Mahé international airport, Seychelles, with the local support of Seychelles
            Meteorological Authority. The scientific goals are to improve the understanding of:
        </div>
        <ul class="list-disc list-inside pb-2">
            <li>
                Dynamics in the TTL through better representation of temperature across the TTL and thus gravity,
                Rossby, and Kelvin wave structure.
            </li>
            <li>Transport of water vapor and other trace gases across the TTL.</li>
            <li>
                The prevalence of sub visible cirrus and large aerosol above the TTL, and frequency of overshooting
                convection or other episodic stratospheric aerosol perturbations.
            </li>
        </ul>
        <p>
            The Engineering Flight campaign was completed from November 2019 - February 2020 with the goal to flight
            test all instruments, gondolas, and balloon configurations. Eight balloons were released between
            mid-November and mid-December 2019, five for remote measurements, drifting at 20 km, and three for in situ
            measurements, drifting at 18 km. The balloon flight lifetimes ranged from 57 to 108 days, with most
            completing 1.5 circumnavigations of the Earth between 10°S and 10°N. The campaign was successful in flight
            certifying the instruments, with suitable improvements, and the flight operations.
        </p>
        <p>
            The first Science Campaign is planned for November 2021 - February 2022 and will release up to 20 balloons.
            A second Science Campaign, with a similar number of balloons, is planned for 2024-2025 to capture the
            opposite phase of the quasi-biennial oscillation.
        </p>
    </div>
</div>
