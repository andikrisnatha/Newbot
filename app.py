from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot      = webdriver.Firefox(executable_path = "./geckodriver.exe")
    
    def login(self):
        bot = self.bot
        bot.get("https://instagram.com/accounts/login")
        time.sleep(4)
        bot.find_element_by_name("username").send_keys(self.username)
        bot.find_element_by_name("password").send_keys(self.password + Keys.RETURN)
        time.sleep(4)

    def searchHashtag(self,hashtag):
        bot = self.bot

        bot.get('https://instagram.com/explore/tags/' + hashtag)

    def likePhoto(self,amount,comment):
        bot = self.bot 
        bot.find_element_by_class_name('v1Nh3').click()
        # bot.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
        bot.find_elements_by_css_selector('._65Bje').click()
        

        i = 1
        while i <= amount:
            time.sleep(2)
            #bot.find_elements_by_class_name('wpO6b').click()
            #bot.find_element_by_xpath("//span[class='fr66n']")
            # bot.find_eslement_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click() #follow
            bot.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click() #like
            time.sleep(2)
            bot.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click() #button comment
            bot.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(comment) #insert comment
            time.sleep(2)
            #bot.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(Keys.RETURN) #post commnet
            bot.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click() #post commnet
            time.sleep(5)
            bot.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click() #click next
            time.sleep(1)            
            i += 1

        bot.get('https://instagram.com/' + self.username)




insta = instagramBot('sideradnyani', 'Brandon23')
insta.login()
insta.searchHashtag('balinesefood')
insta.likePhoto(10,'delicious,  please follow @espenderry')