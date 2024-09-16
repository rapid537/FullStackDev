const {default: axios} = require("axios")
const {defineConfig} = require("cypress")
const flaskAPI = 'http://code.dev.com:5001/api/'


module.exports = defineConfig({
    e2e: {
        baseUrl: 'http://code.dev.com:3000',
        trashAssetsBeforeRuns: true,
        watchForFileChanges: false,
        blockHosts: "www.google-analytics.com",
        video: false,
        screenshotOnRunFailure: false,
        fixturesFolder: '. cypress/fixtures',
        defaultCommandTimeout: 7500,
        excludeSpecPattern: process.env.REACT_APP_USE_TEST_API ? ['cypress/e2e/_RunAllSpecs.spec.cy.js'] : [],

        setupNodeEvents(on, config) {
            on('task', {
                async 'flask:cy_db_setup'() {
                    await axios.post(`${flaskAPI}cy_db_setup`)
                    return null
                },

                async 'flask:cy_db_teardown'() {
                    await axios.post(`${flaskAPI}cy_db_teardown`)
                    return null
                },

                async 'flask:cy_create_user'(user='test') {
                    await axios.post(`${flaskAPI}cy_create_${user}_user`)
                    return null
                },
            })

            require('@cypress/code-coverage/task')(on, config)
            return config
        },
    },
})
