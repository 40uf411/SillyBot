# TODO: Add the option to ignore if the element does not exist
import wget
import threading
import time
import json
import sys
import random
import string
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
import undetected_chromedriver as uc


class Bot:
    # Initialize the bot with the browser and the cookies
    def __init__(self, browser, webdriver_locations, cookies=None, user_agent=None):
        self.browser = browser
        self.webdriver_locations = webdriver_locations
        self.cookies = cookies
        self.user_agent = user_agent
        self.__createBot()
        if cookies:
            self.loadCookies()
        print("Bot ready !")

    # Create a browser Bot in an private mode, disable the notification and disable the extension
    def __createBot(self):
        if self.browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--profile-directory=Default')
            chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_experimental_option(
                "prefs", {"profile.default_content_setting_values.notifications": 2})
            if self.user_agent:
                chrome_options.add_argument('user-agent='+self.user_agent)
            self.driver = uc.Chrome(
                executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
        elif self.browser == "firefox":
            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference(
                "dom.webnotifications.enabled", False)
            firefox_profile.set_preference("dom.push.enabled", False)
            firefox_profile.set_preference(
                "browser.privatebrowsing.autostart", True)
            firefox_profile.set_preference("browser.window.maximize", True)
            if self.user_agent:
                firefox_profile.set_preference(
                    "general.useragent.override", self.user_agent)
            self.driver = webdriver.Firefox(
                executable_path='/usr/bin/geckodriver', firefox_profile=firefox_profile)
        elif self.browser == "edge":
            edge_options = webdriver.EdgeOptions()
            edge_options.add_argument("--incognito")
            edge_options.add_argument('--disable-extensions')
            edge_options.add_argument('--profile-directory=Default')
            edge_options.add_argument("--disable-plugins-discovery")
            edge_options.add_argument("--start-maximized")
            edge_options.add_argument("--disable-notifications")
            edge_options.add_argument("--disable-infobars")
            edge_options.add_experimental_option(
                "prefs", {"profile.default_content_setting_values.notifications": 2})
            if self.user_agent:
                edge_options.add_argument('user-agent='+self.user_agent)
            self.driver = webdriver.Edge(
                executable_path='/usr/bin/msedgedriver', edge_options=edge_options)
        elif self.browser == "safari":
            self.driver = webdriver.Safari(
                executable_path='/usr/bin/safaridriver')
        else:
            print("Invalid browser")
            sys.exit(1)
        print("Bot created !")

    # switch to the next window
    def switchToNextWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print("Switched to next window !")

    # switch to the previous window
    def switchToPreviousWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[-2])
        print("Switched to previous window !")

    # open a new tab by sending the key combination
    def newTab(self, url):
        # check the platform and send the key combination
        if sys.platform.startswith('win'):
            self.driver.find_element_by_tag_name(
                'body').send_keys(Keys.CONTROL + 't')
        elif sys.platform.startswith('linux'):
            self.driver.find_element_by_tag_name(
                'body').send_keys(Keys.CONTROL + 't')
        elif sys.platform.startswith('darwin'):
            self.driver.find_element_by_tag_name(
                'body').send_keys(Keys.COMMAND + 't')
        else:
            self.driver.find_element_by_tag_name(
                'body').send_keys(Keys.CONTROL + 't')
        self.driver.get(url)
        print("New tab opened !")

    # open a new window
    def newWindow(self, url):
        self.driver.execute_script("window.open('"+url+"', 'new_window');")
        print("New window opened !")

    # close the current window
    def closeWindow(self):
        self.driver.close()
        print("Window closed !")

    # maximize the window
    def maximizeWindow(self):
        self.driver.maximize_window()
        print("Window maximized !")

    # minimize the window
    def minimizeWindow(self):
        self.driver.minimize_window()
        print("Window minimized !")

    # un-minimize the window
    def unMinimizeWindow(self):
        self.driver.maximize_window()
        print("Window un-minimized !")

    # save the browser cookies to a file
    def saveCookies(self, file_name="cookies.json"):
        with open(file_name, 'w') as f:
            json.dump(self.driver.get_cookies(), f)
        print("Cookies saved !")

    # load the browser cookies from a file
    def loadCookies(self, file_name=None, refresh=False):
        # if the file name is not specified, use the default one
        if not file_name:
            file_name = self.cookies
        with open(file_name, 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            print(cookie)
            self.driver.add_cookie(cookie)
        if refresh:
            self.driver.refresh()
        print("Cookies loaded !")

    # get the browser cookies
    def getCookies(self):
        return self.driver.get_cookies()

    # scroll the page
    def scroll(self, direction="down", distance=1000):
        if direction == "down":
            self.driver.execute_script(
                "window.scrollBy(0, "+str(distance)+");")
        elif direction == "up":
            self.driver.execute_script(
                "window.scrollBy(0, -"+str(distance)+");")
        else:
            print("Invalid direction")
            sys.exit(1)
        print("Scrolled !")

    # scroll to the top of the page
    def scrollToTop(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        print("Scrolled to top !")

    # scroll to the bottom of the page
    def scrollToBottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        print("Scrolled to bottom !")

    # scroll to the selected element
    def scrollToElement(self, by, value):
        if by == "id":
            self.driver.execute_script(
                "document.getElementById('"+value+"').scrollIntoView();")
        elif by == "class":
            self.driver.execute_script(
                "document.getElementsByClassName('"+value+"')[0].scrollIntoView();")
        elif by == "name":
            self.driver.execute_script(
                "document.getElementsByName('"+value+"')[0].scrollIntoView();")
        elif by == "xpath":
            self.driver.execute_script(
                "document.evaluate('"+value+"', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView();")
        elif by == "css":
            self.driver.execute_script(
                "document.querySelector('"+value+"').scrollIntoView();")
        else:
            print("Invalid element")
            sys.exit(1)
        print("Scrolled to element !")

    # download the page source
    def downloadPageSource(self, filename="page_source.html"):
        with open(filename, 'w') as f:
            f.write(self.driver.page_source)
        print("Page source downloaded !")

    # download the page screenshot
    def downloadScreenshot(self, filename="screenshot.png"):
        self.driver.save_screenshot(filename)
        print("Screenshot downloaded !")

    # download Screenshot from the element
    def downloadElementScreenshot(self, by, value, filename="image.png"):
        self.driver.find_element(by, value).screenshot(filename)
        print("Element screenshot downloaded !")

    # download a video in video tag by getting the video src
    def downloadVideo(self, by, value, filename="video.mp4"):
        video_src = self.driver.find_element(by, value).get_attribute("src")
        wget.download(video_src, filename)
        print("Video downloaded !")

    # download a audio in audio tag by getting the audio src
    def downloadAudio(self, by, value, filename="audio.mp3"):
        audio_src = self.driver.find_element(by, value).get_attribute("src")
        wget.download(audio_src, filename)
        print("Audio downloaded !")

    # download a image in image tag by getting the image src
    def downloadImage(self, by, value, filename="image.png"):
        image_src = self.driver.find_element(by, value).get_attribute("src")
        wget.download(image_src, filename)
        print("Image downloaded !")

    # download a file in file tag by getting the file src
    def downloadFile(self, by, value, filename="file.pdf"):
        file_src = self.driver.find_element(by, value).get_attribute("src")
        wget.download(file_src, filename)
        print("File downloaded !")

    # check if the element is present
    def isPresent(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    # check if the element is visible
    def isVisible(self, by, value):
        try:
            self.driver.find_element(by, value).is_displayed()
            return True
        except NoSuchElementException:
            return False

    # check if the element is enabled
    def isEnabled(self, by, value):
        try:
            self.driver.find_element(by, value).is_enabled()
            return True
        except NoSuchElementException:
            return False

    # check if the element is selected
    def isSelected(self, by, value):
        try:
            self.driver.find_element(by, value).is_selected()
            return True
        except NoSuchElementException:
            return False

    # check if the element is checked
    def isChecked(self, by, value):
        try:
            self.driver.find_element(by, value).is_selected()
            return True
        except NoSuchElementException:
            return False

    # By selector
    def By(self, selector):
        selector = selector.lower()
        selector = selector.replace(" ", "")
        if selector == "id":
            return By.ID
        elif selector == "name":
            return By.NAME
        elif selector == "class":
            return By.CLASS_NAME
        elif selector == "xpath":
            return By.XPATH
        elif selector == "css":
            return By.CSS_SELECTOR
        elif selector == "link":
            return By.LINK_TEXT
        elif selector == "partial":
            return By.PARTIAL_LINK_TEXT
        else:
            print("Invalid selector")
            sys.exit(1)

    # get element
    def getElement(self, by, value):
        try:
            return self.driver.find_element(by, value)
        except NoSuchElementException:
            return None

    # get the text of the element
    def getText(self, by, value):
        try:
            return self.driver.find_element(by, value).text
        except NoSuchElementException:
            return None

    # get the attribute of the element
    def getAttribute(self, by, value, attribute):
        try:
            return self.driver.find_element(by, value).get_attribute(attribute)
        except NoSuchElementException:
            return None

    # implicit wait
    def wait(self, time):
        self.driver.implicitly_wait(time)
        print("Implicit wait set !")

    # wait for the element to be present
    def waitForElement(self, by, value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value)))
        except TimeoutException:
            print("Element not found")
            sys.exit(1)

    # wait for the element to be visible
    def waitForElementToBeVisible(self, by, value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value)))
        except TimeoutException:
            print("Element not found")
            sys.exit(1)

    # wait for the element to be enabled
    def waitForElementToBeEnabled(self, by, value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value)))
        except TimeoutException:
            print("Element not found")
            sys.exit(1)

    # wait for loading the page to be completed
    def waitForLoad(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete")
        except TimeoutException:
            print("Page load timeout")
            sys.exit(1)

    # forced wait
    def forcedWait(self, time):
        time.sleep(time)
        print("Forced wait completed !")

    # conditional wait using lambda function
    def conditionalWait(self, time, condition):
        WebDriverWait(self.driver, time).until(condition)

    # click on the element
    def click(self, by, value):
        try:
            self.driver.find_element(by, value).click()
        except NoSuchElementException:
            print("Element not found")
            sys.exit(1)

    # type in the element character by character
    def input(self, by, value, text):
        try:
            text = list(str(text))
            for i in range(len(text)):
                self.driver.find_element(by, value).send_keys(text[i])
                time.sleep(0.1)
        except NoSuchElementException:
            print("Element not found")
            sys.exit(1)

    # send keys to the element
    def sendKeys(self, by, value, text):
        try:
            self.driver.find_element(by, value).send_keys(text)
        except NoSuchElementException:
            print("Element not found")
            sys.exit(1)

    # select an element from a dropdown
    def select(self, by, value, text):
        try:
            self.driver.find_element(by, value).send_keys(text)
            self.driver.find_element(by, value).send_keys(Keys.ENTER)
        except NoSuchElementException:
            print("Element not found")
            sys.exit(1)

    # submit the form
    def submit(self, by, value):
        try:
            self.driver.find_element(by, value).submit()
        except NoSuchElementException:
            print("Element not found")
            sys.exit(1)

    # refresh the page
    def refresh(self):
        self.driver.refresh()
        print("Page refreshed !")

    # go to the URL
    def goTo(self, url):
        self.driver.get(url)
        print("Page loaded !")

    # go to the back
    def goBack(self):
        self.driver.back()
        print("Page back loaded !")

    # go to the forward
    def goForward(self):
        self.driver.forward()
        print("Page forward loaded !")

    # close the browser
    def close(self):
        self.driver.close()
        print("Browser closed !")

    # switch to frame
    def switchToFrame(self, by, value):
        try:
            # wait for the frame to load
            self.waitForElement(by, value, 60)
            self.driver.switch_to.frame(self.driver.find_element(by, value))
        except NoSuchElementException:
            print("Element not found")
            sys.exit(1)

    # inject JavaScript
    def injectJS(self, js):
        self.driver.execute_script(js)
        print("JavaScript injected !")

    # inject style
    def injectStyle(self, css):
        self.driver.execute_script("document.body.style.cssText = '"+css+"'")
        print("Style injected !")

    # get the current URL
    def getCurrentURL(self):
        return self.driver.current_url

    # breakpoint
    def breakpoint(self):
        input("Press Enter to continue...")

    # get the alert text
    def getAlertText(self):
        try:
            return self.driver.switch_to.alert.text
        except NoAlertPresentException:
            print("No alert found")
            sys.exit(1)

    # accept alert
    def acceptAlert(self):
        try:
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            print("No alert found")
            sys.exit(1)

    # dismiss alert
    def dismissAlert(self):
        try:
            self.driver.switch_to.alert.dismiss()
        except NoAlertPresentException:
            print("No alert found")
            sys.exit(1)

    # wait for the alert to be present
    def waitForAlert(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.alert_is_present())
        except TimeoutException:
            print("Alert not found")
            sys.exit(1)

    # get the title
    def getTitle(self):
        return self.driver.title

    # get the head items in a dictionary of meta, style, script etc.
    def getHead(self):
        head = self.driver.find_element_by_tag_name("head")
        head_items = head.find_elements_by_tag_name("*")
        head_dict = {}
        for item in head_items:
            head_dict[item.tag_name] = item.get_attribute("outerHTML")
        return head_dict

    # get the body
    def getBody(self):
        return self.driver.find_element_by_tag_name("body").get_attribute("outerHTML")

    # run callback function
    def run(self, callback, *args, **kwargs):
        val = callback(self, self.driver, *args, **kwargs)
        print("Callback function executed !")
        return val
