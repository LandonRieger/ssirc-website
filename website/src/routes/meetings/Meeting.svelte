<script>
    let { title, subtitle, id, children } = $props();
</script>

<div>
    <h2 {id} class="mb-1">{title}</h2>
    <p class="text-sm font-light italic mb-1">{subtitle}</p>
    {@render children()}
</div>
