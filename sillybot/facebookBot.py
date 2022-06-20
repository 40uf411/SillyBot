# facebook plugin for the bot class
from selenium.webdriver.common.by import By
from bot import Bot

class FacebookBot():
    # login to the facebook mobile page
    def login(bot: Bot, email, pwd, load_url=True):
        if load_url:
            bot.goTo("https://m.facebook.com/")
        bot.input(by=Bot.By('name'), value="email", text=email)
        bot.input(by=By.NAME, value="pass", text=pwd)
        bot.wait(1)
        bot.submit(by=By.NAME, value="login")
    
    # navigate to mobile home page
    def goToMobileHome(bot: Bot):
        bot.goTo("https://m.facebook.com/home.php")
        bot.wait(1)
    
    # go to the profile page
    def goToMobileProfile(bot: Bot):
        # redirect to the profile page
        bot.goTo("https://m.facebook.com/profile.php")
        bot.wait(1)
    
    # upload a photo to the profile page on m.facebook.com
    def uploadPhotoToMobileProfile(bot: Bot, description, file_path):
        bot.click(by=By.ID, value="u_0_10_71")
        bot.wait(1)