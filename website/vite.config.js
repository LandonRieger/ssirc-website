import { env } from "node:process";
import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vite";

// const apiProxyTarget = "http://127.0.0.1:8000";
const apiProxyTarget = "https://ssirc-website.onrender.com";

export default defineConfig({
    define: {
        "process.env": process.env,
        _WORKLET: false,
        __DEV__: env.DEV,
        global: {},
    },
    plugins: [sveltekit()],
    server: {
        strictPort: true,
        proxy: {
            "/api": {
                target: apiProxyTarget,
                changeOrigin: true,
                secure: false,
                rewrite: (path) => path.replace(/^\/api/, "/api/"),
            },
        },
    },
});
