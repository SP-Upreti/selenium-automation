import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Browser:
    browser =  None

    def __init__(self) :
        self.browser = webdriver.Chrome()

    def Open(self, url:str):
        self.browser.get(url)
    
    def Close(self):
        self.browser.close()

    def Input(self, by:By, value:str, text:str):
        field = self.browser.find_element(by=by,value=value)
        field.send_keys(text)
        time.sleep(1)

    def Click(self, by:By, value):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)
    
    def Login(self, username:str, password:str):
        self.Input(by=By.NAME, value="email", text=username)
        self.Input(by=By.NAME, value="pass", text=password)
        self.Click(by=By.NAME, value="login")


browser = Browser()
browser.Open("https://www.facebook.com/")
time.sleep(3)
browser.Login("demo@gmail.com", "#demo123")
time.sleep(20)
browser.Close()