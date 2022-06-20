# google plugin for the bot class
from selenium.webdriver.common.by import By
from bot import Bot

class GoogleBot():
    # search for text
    def search(bot: Bot, text, load_url=True):
        if load_url:
            bot.goTo("https://www.google.com/")
        bot.input(by=By.NAME, value="q", text=text)
        bot.submit(by=By.NAME, value="btnK")

    # click on the first result
    def clickOnFirstResult(bot: Bot):
        bot.click(by=By.CLASS_NAME, value="DKV0Md")
