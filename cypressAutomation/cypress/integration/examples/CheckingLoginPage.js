/// <reference types="Cypress" />
import loginPage from '../../support/pageObjects/loginPage'
describe('Login Test suite', function () {

    beforeEach(() => {
        // runs once before all tests in the block
        cy.fixture('loginData').then(function (data) {
            this.data = data
        })
    })

    it('1. Verify mail with plaint text and mail error text', function () {

        //creating object for the class
        const login = new loginPage()
        //navigates to url
        cy.visit('https://app2.abtasty.com/login')
        //types text in email textbox
        login.getEmailTextbox().type(this.data.plaintext)
        //clicks the next button
        login.nextBtn().click()
        //checks the mail error text
        login.getErrorText().should('exist').contains(this.data.mailError);
    })

    it('2. Verify password eye icon and password error text', function () {

        const login = new loginPage()
        //clears the text in textbox
        login.getEmailTextbox().clear()
        //enters mail in textbox
        login.getEmailTextbox().type(this.data.mail)
        login.nextBtn().click()
        //enters the password and checks the password is hidden
        login.getPassword().type(this.data.password1).should('have.attr', 'type', 'password')
        //clicks the eye icon
        login.getEyeIcon().click()
        //checks the password is visible
        login.getPassword().should('have.attr', 'type', 'text')
        //clicks the signIn button
        login.signInBtn().click()
        //checks the password error text
        login.getErrorText().should('have.text', this.data.pwdError)
    })

    it('3. Verifying catcha is displayed', function () {

        const login = new loginPage()
        login.getPassword().type(this.data.password2)
        login.signInBtn().click()

        login.getPassword().type(this.data.password3)
        login.signInBtn().click()
        login.signInBtn().click()

        login.getCaptchaErrorText().should('have.text', this.data.captchaError)

    })

    it('4. Verify mail should be restored and password should not be restored', function () {

        const login = new loginPage()
        //clicks the previous button
        login.previousBtn().click()
        //checks the entered mail is restored
        login.getEmailTextbox().should('have.value', this.data.mail);
        login.nextBtn().click()
        //checks the password is not restored
        login.getPassword().should('have.value', '');

    })
})
