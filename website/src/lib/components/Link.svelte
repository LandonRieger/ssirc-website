<script>
    let { href, children } = $props()
</script>

<a href={href} class="text-blue-700 hover:underline">
    {@render children()}
</a>