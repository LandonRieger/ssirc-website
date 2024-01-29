<script>
    import "../app.css";
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Dropdown, DropdownItem } from "flowbite-svelte";
    import { ChevronDownOutline } from "flowbite-svelte-icons";
    import sunset from "$lib/images/sunset-iss-cropped.jpg";
    import favicon from "$lib/images/favicon.svg";
    import Person from "$lib/components/Person.svelte";
</script>

<svelte:head>
  <link rel="icon" type="image/svg" href={favicon} />
</svelte:head>

<div class="relative height-[200px]">
    <img src={sunset} style="height:200px; width:100%; object-fit:cover; object-position: 100% 100%;" />
    <div class="absolute bottom-0 px-12 py-12">
        <div class="text-white font-medium text-8xl">SSiRC</div>
        <div class="text-white font-normal text-lg">Stratospheric Sulfur and its Role in Climate</div>
    </div>
</div>
<Navbar class="max-w-6xl mx-auto px-0">
    <NavBrand href="/">
        <img src={favicon} class="me-3 h-6 sm:h-9" alt="logo" />
        <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">SSiRC</span>
    </NavBrand>
    <NavHamburger />
    <NavUl>
        <NavLi href="/about">About</NavLi>
        <NavLi href="/meetings">Meetings</NavLi>
        <NavLi class="cursor-pointer">
            Activities
            <ChevronDownOutline class="w-3 h-3 ms-2 text-primary-800 dark:text-white inline" />
        </NavLi>
        <Dropdown class="w-44 z-20">
            <DropdownItem href="/activities/modelling">Modelling</DropdownItem>
            <DropdownItem href="/activities/campaigns">Campaigns</DropdownItem>
            <DropdownItem href="/activities/analysis">Analysis</DropdownItem>
            <DropdownItem href="/activities/volres">VolRes</DropdownItem>
            <DropdownItem href="/activities/data_rescue">Data Rescue</DropdownItem>
        </Dropdown>
        <NavLi href="/publications">Publications</NavLi>
        <NavLi href="/implementation">Implementation Plan</NavLi>
    </NavUl>
</Navbar>

<div class="container max-w-6xl mx-auto px-4 lg:px-0">
    <slot />
</div>

<div class="bg-gray-100 mt-8">
    <div class="container max-w-6xl mx-auto py-6">
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div class="cols-start-1 sm:col-span-1 lg:col-span-3">
                <div class="text-lg font-light text-gray-700">Science Steering Group</div>
                <hr class="my-2 bg-gray-500" />
                <div class="grid sm:grid-cols-1 md:grid-cols-2 gap-2">
                    <div>
                        <Person name={"Landon Rieger"} location="University of Saskatchewan" />
                        <Person name={"Mark von Hobe"} location="Forschungszentrum Jülich"/>
                        <Person name={"Anja Schmidt"} location="Deutsches Zentrum für Luft- und Raumfahrt"/>
                        <Person name={"Juan Carlos Antuña"} location="Departamento de Física Teórica"/>
                        <Person name={"Andrew Rollins"} location="NOAA"/>
                        <Person name={"Corinna Kloss"} location="Forschungszentrum Jülich"/>
                        <Person name={"Terry Deshler"} location="University of Colorado"/>
                    </div>
                    <div>
                        <Person name={"Jean-Paul Vernier"} location="NASA Langley Research Center"/>
                        <Person name={"Mahesh Kovilakam"} location="Science Systems Applications Inc."/>
                        <Person name={"Graham Mann"} location="School of Earth and Environment"/>
                        <Person name={"Yunqian Zhu"} location="University of Colorado Boulder"/>
                        <Person name={"Eduardo Landulfo"} location="Instituto de Pesquisas Energéticas e Nucleares"/>
                        <Person name={"Suvarna Fadnavis"} location="Indian Institute of Tropical Meteorology"/>
                    </div>
                </div>
            </div>
            <div>
                <div class="text-lg font-light text-gray-700">Contact</div>
                <hr class="my-2 bg-gray-500" />
                <div class="text-sm mb-4">
                    If you are interested in joining the email list and to receive updates about the SSiRC activity,
                    please subscribe
                    <a class="text-blue-600" href="https://listserv.gwdg.de/mailman/listinfo/ssirc">here</a>.
                </div>
                <div class="text-sm text-gray-700">
                    <Person name="Landon Rieger" />
                    <div>University of Saskatchewan</div>
                    <div>landon.rieger@usask.ca</div>
                </div>
            </div>
        </div>
    </div>
</div>
