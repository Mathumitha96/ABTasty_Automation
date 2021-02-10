import unittest
from selenium import webdriver
from time import sleep
class checkingLoginPageInEnglish(unittest.TestCase):
   def setUp(self):
        self.driver = webdriver.Chrome("D:/Python/chromedriver_win32/chromedriver.exe")
        self.driver.maximize_window()   
   def test_login_page(self):
        driver = self.driver 
        driver.get("https://www.abtasty.com/")
        driver.find_element_by_xpath("//li[@id='jet-menu-item-52816']/a/div/div").click()
        driver.find_element_by_xpath("//li[@id='jet-menu-item-54519']/a/div/div").click()
        titleOfPage = driver.find_element_by_css_selector('.FormHeader__title___vWI3B').text
        print(titleOfPage)
        #checks the title matchs
        self.assertEqual("Sign in to your account", titleOfPage, "title text is not matching")
        mailText = driver.find_element_by_css_selector('.Input__labelText___3690B').text
        print(mailText)
        #checks the email text
        self.assertEqual("Email", mailText, "Mail text is not matching")
        nextBtn = driver.find_element_by_css_selector('.Button__button___3_Ozh')
        nextBtnText = nextBtn.text
        print(nextBtnText)
        #checks the next button text
        self.assertEqual("Next", nextBtnText, "Next text is not matching")
        nextBtn.click()
        mailErrorText = driver.find_element_by_css_selector('.Input__errorMessage___371Rm').text
        print(mailErrorText)
        #checks the mail Error Text
        self.assertEqual("Please enter a valid email", mailErrorText, "Mail error text is not matching")
        driver.find_element_by_css_selector('#email').send_keys("azert@123.fr")
        nextBtn.click()
        sleep(3)
        pwdText = driver.find_element_by_css_selector("span.Input__labelText___3690B").text
        print(pwdText)
        #checks the password Text
        self.assertEqual("Password", pwdText, "Password text is not matching")
        signBtn = driver.find_element_by_css_selector('#signIn')
        signBtnText = signBtn.text
        print(signBtnText)
        #checks the Sign in button Text
        self.assertEqual("Sign in", signBtnText, "SignIn button text is not matching")
        signBtn.click()
        pwdErrorText = driver.find_element_by_css_selector('.Input__errorMessage___371Rm').text
        print(pwdErrorText)
        #checks the password error text
        self.assertEqual("Please enter a valid password", pwdErrorText, "Password errorText is not matching")
if __name__ == "__main__":
	unittest.main()