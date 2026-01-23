<script>
    let { links } = $props()
</script>
    <div class="flex overflow-y-auto sticky top-20 flex-col justify-between pb-6 mr-6 h-[calc(100vh-5rem)] invisible lg:visible">
        <div class="border-1 text-gray-200 rounded-sm divide-gray-200">
            <div class="px-4 py-2 text-gray-400 uppercase">On this page</div>
            <nav class="w-48" id="my-custom-scroll">
                <ul class="nav">
                    {#each links as link}
                        <li class="text-sm font-medium text-gray-600 hover:font-bold"><a href={`#${link.id}`} class="px-4 py-2 flex flex-grow">{link.label}</a></li>
                    {/each}
                </ul>
            </nav>
        </div>
    </div>