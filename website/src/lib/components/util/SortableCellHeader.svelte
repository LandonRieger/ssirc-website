<script>
    export let name;
    export let sortName;
    export let sortBy;

    import { CaretDownSolid, CaretUpSolid } from "flowbite-svelte-icons";
    const baseClass = "text-gray-400 leading-none text-xs"
    const activeClass = "text-gray-900 leading-none text-xs"
</script>

<div>
    <div class="flex flex-row">
        <div>{name}</div>
        <div class="col pl-2 content-center">
            <div class={sortBy.col === sortName  && sortBy.ascending ? activeClass : baseClass}><CaretUpSolid class="w-2 h-2"/></div>
            <div class={sortBy.col === sortName  && !sortBy.ascending ? activeClass : baseClass}><CaretDownSolid class="w-2 h-2"/></div>
        </div>
    </div>
</div>
