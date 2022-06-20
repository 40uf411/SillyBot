# test the bot class
from selenium.webdriver.common.by import By
from bot import Bot
from googleBot import GoogleBot
from facebookBot import FacebookBot
import time

def testBot(bot: Bot, driver):
    # maximize the window
    bot.maximizeWindow()
    # wait 2 seconds for the bot to be ready
    bot.wait(2)
    # got to google search
    # GoogleBot.search(bot, "facebook")
    # wait for the results to load
    # bot.wait(2)
    # click on the first result
    # GoogleBot.clickOnFirstResult(bot)
    # go to mobile version of facebook
    FacebookBot.goToMobileHome(bot)
    # load the cookies
    bot.loadCookies("cookies.json", refresh=True)
    # wait for the cookies to load
    bot.wait(2)
    # click on data-sigil="login_profile_form"
    bot.click(by=By.CSS_SELECTOR, value="[data-sigil='login_profile_form']")
    # input into the pass field
    bot.input(by=By.NAME, value="pass", text="Salam0147")
    # submit by clicking on type="submit"
    bot.submit(by=By.CSS_SELECTOR, value="[type='submit']")
    # wait for the page to load
    # bot.waitForElementToBeVisible(by=By.NAME, value="login", timeout=10)
    # got to facebook login
    # FacebookBot.login(bot, "ali25aa@outlook.fr", "Salam0147")
    # save the cookies
    # bot.saveCookies()
    # wait for the page to load
    time.sleep(5)
    # go to the profile page
    FacebookBot.goToMobileProfile(bot)
    time.sleep(5)
    # open the css selector ._4g34._6ber._78cq._7cdk._5i2i._52we
    bot.click(by=By.CSS_SELECTOR, value="._4g34._6ber._78cq._7cdk._5i2i._52we")

    # # wait for the file selector to load
    # bot.wait(1)
    # # fill textarea class = "composerInput mentions-input" with "test"
    # bot.input(by=By.CSS_SELECTOR, value="textarea.composerInput.mentions-input", text="test")
    # # insert file into id = photo_input
    # bot.sendKeys(by=By.ID, value="photo_input", text="/home/zsasz/Downloads/test.jpg")

    # take input from the user
    userInput = input("Enter your message: ")
    # while the user input is not empty
    while userInput != "":
        # check if the user input is present in the page
        if bot.isPresent(by=By.CLASS_NAME, value=userInput):
            print("The element is present")
        else:
            print("The element is not present")
        # wait for the page to load
        bot.wait(1)
        # re-take input from the user
        userInput = input("Enter your message: ")


Bot("chrome", "/usr/bin/chromedriver").run(testBot)


# statuselement=driver.find_element_by_xpath("//[@name='xhpc_message']").click() 
# driver.find_element_by_xpath("//[@class='_3jk']").click() 
# l=driver.find_elements_by_tag_name('input') 
# ipath="/home/zsasz/Downloads/test.jpg" 
# for g in l: 
#     if g==driver.find_element_by_xpath("//input[@type='file'][@class='_n _5f0v']"): 
#         g.send_keys(ipath) 
#         print('image loaded')