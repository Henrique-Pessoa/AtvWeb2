export default defineNuxtConfig({
  devtools: { enabled: true },
  css: [
    "primevue/resources/themes/aura-light-green/theme.css",
    "~/assets/css/main.css",
  ],
  modules: ["nuxt-primevue", "nuxt-icon"],
  primevue: {},
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
});
