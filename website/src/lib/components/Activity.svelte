<script>
    let {
        image,
        title,
        link,
        content
    } = $props();
</script>

<div class="shadow-md hover:shadow-lg hover:scale-105 border-1 border-gray-300 p-0 rounded-sm transition-all">
    <a href={link}>
        <div class="relative">
            <!--            <div class="font-bold text-sky-600 uppercase p-2">{title}</div>-->
            <div
                class="w-full h-16 font-bold text-gray-50 leading-none uppercase p-2 absolute bg-gradient-to-b from-gray-900/70 via-gray-900/20 via-50% via-gray-900/10 via-70% absolute">
                {title}
            </div>
            <!--            <div class="bg-gradient-to-r from-blue-500 absolute">-->
            <!-- ... -->
            <!--</div>-->
            <img src={image} alt={title} />
            <div
                class="opacity-0 hover:opacity-90 bg-gray-700 duration-300 absolute inset-0 z-10 flex justify-center items-center text-sm text-white font-semibold p-4">
                {content}
            </div>
        </div>
    </a>
</div>
