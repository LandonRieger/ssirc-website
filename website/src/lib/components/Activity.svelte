<script>
    export let image;
    export let title;
    export let link;
    export let content;
</script>

<div class="shadow-md hover:shadow-lg hover:scale-105 border-1 border-gray-300 p-0 rounded-sm transition-all">
    <a href={link}>
        <div class="relative">
            <div class="font-bold text-gray-500 uppercase p-2">{title}</div>
<!--                    <div class="font-bold text-gray-50 uppercase p-2 absolute">{title}</div>-->
            <img src={image} alt={title} />
            <div
                class="opacity-0 hover:opacity-90 bg-gray-700 duration-300 absolute inset-0 z-10 flex justify-center items-center text-sm text-white font-semibold p-4">
                {content}
            </div>
        </div>
    </a>
</div>
