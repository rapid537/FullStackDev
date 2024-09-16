describe('/auth/sign-up', () => {
    it('submits the sign-up form', () => {
        cy.visit('/auth/sign-up')
        cy.get('input[name=name]').type('test_user')
        cy.get('input[name=email]').type('test_user@mail.com')

        cy.get('button[type=submit]').click()
        cy.wait('@allPostRequests')
        .its('response.statusCode').should('eq', 201)

        cy.get('.swal-modal').contains('OK').click()
        cy.url().should('include', '/auth/confirm-code')
    })
})
