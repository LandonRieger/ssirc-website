import { env } from "node:process";
import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vite";
import tailwindcss from '@tailwindcss/vite'

// const apiProxyTarget = "http://127.0.0.1:8000";
// const apiProxyTarget = "https://ssirc-website.onrender.com";

export default defineConfig({
    define: {
        "process.env": process.env,
        _WORKLET: false,
        __DEV__: env.DEV,
        global: {},
    },
    plugins: [sveltekit(), tailwindcss()]
});
