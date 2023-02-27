// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    runtimeConfig: {
        public: {
            MEDUSA_API: process.env.MEDUSA_API || 'http://127.0.0.1:9000'
        }
    },
    css: [
        '@/styles/bulma.scss'
    ]
})
