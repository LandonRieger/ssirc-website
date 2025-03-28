/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'],
  plugins: [require('flowbite/plugin')],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter']
      },
      borderRadius: {sm: '0.125rem', md: '0.18rem', lg: '0.25rem'}
    },
  },
}

