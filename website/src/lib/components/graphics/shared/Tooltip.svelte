<script>
  /** @type {Object} evt - A svelte event created via [`dispatch`](https://svelte.dev/docs#createEventDispatcher) with event information under `evt.detail.e`. */
  export let evt = {};

  /** @type {Number} [offset=-35] - A y-offset from the hover point, in pixels. */
  export let offset = -15;
  export let xoffset = 0;
</script>

<style>
  .tooltip {
    position: absolute;
    width: var(--width, 150px);
    border: 1px solid #ccc;
    background: rgba(255, 255, 255, 0.95);
    transform: translate(-50%, -100%);
    padding: 5px;
    z-index: 15;
  }
</style>

{#if evt.detail}
  <div
    class="tooltip shadow-md"
    style="
      top:{evt.detail.e.layerY + offset}px;
      left:{evt.detail.e.layerX + xoffset}px;
    "
  >
    <slot detail={evt.detail}></slot>
  </div>
{/if}