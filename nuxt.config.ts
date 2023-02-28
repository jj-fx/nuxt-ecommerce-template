// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    runtimeConfig: {
        public: {
            STORE_API: process.env.STORE_API || 'http://localhost:5000'
        }
    },
    css: [
        '@/styles/bulma.scss'
    ]
})
