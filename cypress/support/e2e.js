import './commands'
import '@cypress/code-coverage/support'


before(() => {})


after(() => {})


beforeEach(() => {
    cy.db_setup()

    cy.intercept(
        {path: '/api/**/?**'},
        request => request.headers['Accept-Encoding'] = 'gzip, deflate',
    ).as('allApiRequests')

    cy.intercept({method: 'POST', path: '/api/**'}).as('allPostRequests')
})


afterEach(() => {})
