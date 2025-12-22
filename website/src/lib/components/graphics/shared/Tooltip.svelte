<script>
  

  
  /**
   * @typedef {Object} Props
   * @property {Object} [evt] - A svelte event created via [`dispatch`](https://svelte.dev/docs#createEventDispatcher) with event information under `evt.detail.e`.
   * @property {Number} [offset] - A y-offset from the hover point, in pixels.
   * @property {number} [xoffset]
   * @property {import('svelte').Snippet<[any]>} [children]
   */

  /** @type {Props} */
  let {
    evt = {},
    offset = -15,
    xoffset = 0,
    children
  } = $props();
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
    {@render children?.({ detail: evt.detail, })}
  </div>
{/if}