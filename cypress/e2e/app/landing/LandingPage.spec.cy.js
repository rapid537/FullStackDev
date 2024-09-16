describe('landing page', () => {
    it('requires a jwt for the protected route', () => {
        cy.task('flask:cy_create_user')

        cy.visit('/')
        cy.contains('JWT Protected Route').click()

        cy.wait('@allApiRequests')
        .its('response.statusCode').should('eq', 202)

        cy.url().should('include', '/auth/sign-in')

        cy.authenticate_user('test_user')

        cy.visit('/')
        cy.contains('JWT Protected Route').click()

        cy.wait('@allApiRequests')
        .its('response.statusCode').should('eq', 200)
        cy.url().should('include', '/auth/protected-route')
        cy.contains('I am a protected route!').should('exist')
    })
})
