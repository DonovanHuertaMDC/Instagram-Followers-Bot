import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common import ElementClickInterceptedException
import os

account = os.environ.get("SIMILAR_ACCOUNT")
my_email = os.environ.get("USERNAME")
my_password = os.environ.get("PASSWORD")


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        email.send_keys(my_email)
        password.send_keys(my_password)
        log_in.click()

        time.sleep(8)
        save_login_prompt = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Ahora no')]")
        save_login_prompt.click()
        time.sleep(8)
        notifications_prompt = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Ahora no')]")
        notifications_prompt.click()
        time.sleep(5)
        '''search = self.driver.find_element(By.XPATH, value="// span[contains(text(), 'Búsqueda')]")
        search.click()
        time.sleep(3)
        searcher = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_xm"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        searcher.send_keys(account, Keys.ENTER)'''

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{account}/followers/")
        time.sleep(5)
        for i in range(10):
            bar = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', bar)
            time.sleep(3)

    def follow(self):
        followers_button = self.driver.find_elements(By.CSS_SELECTOR, '._aano button')
        for f in followers_button:
            try:
                f.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Cancelar')]")
                cancel.click()


        #followers_button.click()
        #time.sleep(5)
        #while True:
        #follow = self.driver.find_elements(By.XPATH, value="//div[contains(text(), 'Seguir')]")
        #follow_button = [f.text for f in follow]
        #print(follow_button)
        #follow = self.driver.find_elements(By.XPATH, '//*[@id="mount_0_0_lX"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div[3]/div[1]/div/div[3]/div/div/div/div[3]/div/button/div/div')
        #follow = self.driver.find_elements(By.XPATH, '//*[@id="mount_0_0_lX"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div[3]/div[1]/div/div[5]/div/div/div/div[3]/div/button/div/div')

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()