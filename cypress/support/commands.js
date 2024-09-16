Cypress.Commands.add('authenticate_user', user => {
    cy.request(
        'POST',
        'http://code.dev.com:5001/api/cy_authenticate_user',
        {username: `${user}`, email: `${user}@mail.com`},
    )
})


Cypress.Commands.add('db_setup', () => {
    cy.task('flask:cy_db_teardown')
    sessionStorage.removeItem('context')
    cy.task('flask:cy_db_setup')
})


Cypress.Commands.add('sync_session', session_user => {
    sessionStorage.setItem(
        'context',
        JSON.stringify(
            {user: {
                userName: session_user,
                userMail: `${session_user}@mail.com`,
            }}
        )
    )
})
