//Login page objects
class loginPage {


    getEmailTextbox() {
        return  cy.get('#email')
    }

    nextBtn() {
        return cy.get('.Button__button___3_Ozh')
    }

    getPassword() {
        return cy.get('#password')
    }

    getEyeIcon() {
        return cy.get('.icons__pulsar-eye-open___eB5fT')
    }

    signInBtn() {
        return cy.get('#signIn')
    }

    getErrorText() {
        return  cy.get('.Input__errorMessage___371Rm')
    }

    getCaptchaErrorText() {
        return cy.get('.ReCaptcha__errorMessage___gBQEe')
    }

    previousBtn() {
        return  cy.get('.icons__pulsar-arrow-left___RcqB9')
    }
}

export default loginPage;