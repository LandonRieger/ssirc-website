<script>
    let { name, title, children } = $props();
</script>

<div>
    <h3 class="text-gray-800">{title}</h3>
    <div class=" hyphens-auto text-justify">
        {@render children()}
    </div>
</div>
