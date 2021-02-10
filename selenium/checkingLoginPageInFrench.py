import unittest
from selenium import webdriver
from time import sleep
class checkingLoginPageInFrench(unittest.TestCase):
   def setUp(self):
        self.driver = webdriver.Chrome("D:/Python/chromedriver_win32/chromedriver.exe")
        self.driver.maximize_window()
        # options = webdriver.ChromeOptions()
        # options.add_argument('--lang=fr')
        # self.driver = webdriver.Chrome(executable_path="D:/Python/chromedriver_win32/chromedriver.exe", chrome_options=options)
   def test_login_page(self):
        driver = self.driver      
        print("Checks the login page is in French")
        driver.get("https://www.abtasty.com/")
        driver.find_element_by_xpath("//li[@id='jet-menu-item-52820']/a/div/div").click()
        driver.find_element_by_xpath("//li[@id='jet-menu-item-52820-fr']/a/div/div").click()
        #checks the home url is in french
        print(driver.current_url)
        URL = driver.current_url
        self.assertEqual(URL, "https://www.abtasty.com/fr/" )
        driver.find_element_by_xpath("//li[@id='jet-menu-item-54373']/a/div/div").click()
        driver.find_element_by_xpath("//li[@id='jet-menu-item-54514']/a/div/div").click()
        titleOfPage = driver.find_element_by_css_selector(".FormHeader__title___vWI3B").text
        #checks the title matchs
        print(titleOfPage)
        self.assertEqual("Connexion", titleOfPage, "title text is not matching")
        mailPwd = driver.find_element_by_css_selector('.Input__labelText___3690B').text
        print(mailPwd)
        #checks the email text
        self.assertEqual("Email", mailPwd, "Mail text is not matching")
        nextBtn = driver.find_element_by_css_selector('.Button__button___3_Ozh')
        nextBtnText = nextBtn.text
        print(nextBtnText)
        #checks the next button text
        self.assertEqual("Suivant", nextBtnText, "Text is not matching")
        nextBtn.click()
        mailErrorText = driver.find_element_by_css_selector('.Input__errorMessage___371Rm').text
        print(mailErrorText)
        #checks the mail Error Text
        self.assertEqual("Veuillez entrer un email valide", mailErrorText, "Text is not matching")
        driver.find_element_by_css_selector('#email').send_keys("azert@123.fr")
        nextBtn.click()
        sleep(3)
        pwdText = driver.find_element_by_css_selector("span.Input__labelText___3690B").text
        print(pwdText)
        #checks the password Text
        self.assertEqual("Mot de passe", pwdText, "Password text is not matching")
        signBtn = driver.find_element_by_css_selector('#signIn')
        signBtnText = signBtn.text
        print(signBtnText)
        #checks the Sign in button Text
        self.assertEqual("Se connecter", signBtnText, "SignIn button text is not matching")
        signBtn.click()
        pwdErrorText = driver.find_element_by_css_selector('.Input__errorMessage___371Rm').text
        print(pwdErrorText)
        #checks the password error text
        self.assertEqual("Veuiller entrer un mot de passe valide", pwdErrorText, "Password errorText is not matching")
if __name__ == "__main__":
	unittest.main()