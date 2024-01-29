<script>
    import { Card } from "flowbite-svelte";
    export let title;
    export let content;
    export let image;
    export let link;
</script>

<!--<div class="w-full">-->
<!--    <Card img={image} href={link} horizontal size="md" padding="none">-->
<!--        <div class="m-3">-->
<!--            <div class="mb-2 text-lg font-medium tracking-tight leading-tight text-gray-900 dark:text-white">{title}</div>-->
<!--            <div class="mb-3 font-normal text-sm text-gray-700 dark:text-gray-400 leading-tight">{content}</div>-->
<!--        </div>-->
<!--    </Card>-->
<!--</div>-->

<div class="shadow-md hover:shadow-lg border-1 border-gray-300 p-2 rounded-sm transition-all">
    <a href={link}>
        <div class="flex flex-row">
            <div class="flex-none">
                <img src={image} alt={title} class="object-cover object-left-bottom w-24 h-24"/>
            </div>
            <div class="grow pl-4">
                <div class="font-bold text-gray-500 uppercase pb-2">{title}</div>
                <div class="text-xs">
                        {content}
                </div>
            </div>
        </div>
    </a>
</div>
