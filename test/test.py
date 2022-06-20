import wget
import threading
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

# Create a class for a bot that will be used to upload a video to a Facebook page
class Bot:
    # Initialize the bot with the email and password of the account
    def __init__(self, browser, email, pwd):
        self.browser = browser
        self.email = email
        self.pwd = pwd
        self.createAgent(browser)
        # wait for the login page to load
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id("email"))
        self.login(email,pwd)
        # wait for the home page to load
        # WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id("u_0_b"))
        # # click randomly in the home page to avoid the popup
        # self.driver.find_element_by_id("u_0_b").click()
        # move the mouse to the top of the page
        self.driver.execute_script("window.scrollTo(0,0);")

    # Create a browser agent in an private mode, disable the notification and disable the extension
    def createAgent(self, browser):
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--profile-directory=Default')
            chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("--start-maximized")
            # block the notification
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
            self.driver = uc.Chrome(executable_path = '/usr/bin/chromedriver', chrome_options=chrome_options)
        elif browser == "firefox":
            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference("dom.webnotifications.enabled", False)
            firefox_profile.set_preference("dom.push.enabled", False)
            firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
            firefox_profile.set_preference("browser.window.maximize", True)
            self.driver = webdriver.Firefox(executable_path = '/usr/bin/geckodriver', firefox_profile=firefox_profile)
        elif browser == "edge":
            edge_options = webdriver.EdgeOptions()
            edge_options.add_argument("--incognito")
            edge_options.add_argument('--disable-extensions')
            edge_options.add_argument('--profile-directory=Default')
            edge_options.add_argument("--disable-plugins-discovery")
            edge_options.add_argument("--start-maximized")
            self.driver = webdriver.Edge(executable_path = '/usr/bin/msedgedriver', options=edge_options)
        else:
            print("Browser not supported !")
            exit()
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        print("Agent created !")

    def closeBrowser(self):
        self.driver.close()
        print("Browser closed !")

    # Login to the account
    def login(self, email, pwd):
        # send the email character by character
        for i in email:
            self.driver.find_element_by_id("email").send_keys(i)
            time.sleep(0.1)
        # send the password character by character with random delay
        for i in pwd:
            self.driver.find_element_by_id("pass").send_keys(i)
            time.sleep(0.1)
        # wait for the login button to be clickable
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_name("login"))
        self.driver.find_element_by_name("login").click()
        print("Logged in !")
        self.driver.implicitly_wait(10)

    # go the watch tab of the account
    def goToWatch(self):
        # get the element with aria-label="Watch"
        watch = self.driver.find_element_by_xpath("//*[@aria-label='Watch']")
        # click on it
        watch.click()
        print("Go to watch tab !")
        self.driver.implicitly_wait(10)

# create a bot
bot = Bot("chrome", "ali25ab@outlook.fr", "Salam0147")
# go to the watch tab
bot.goToWatch()
#bot.login("
# bot.closeBrowser()

