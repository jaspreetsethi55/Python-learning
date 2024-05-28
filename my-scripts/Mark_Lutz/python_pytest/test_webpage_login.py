from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

CHROMEDRIVER_PATH = "/usr/lib/chromium-browser/chromedriver"

##Using headless oprions for Linux
options = Options() 
options.add_argument('--headless=new')

def test_google():

    driver = webdriver.Chrome(CHROMEDRIVER_PATH , options=options) ##For Linux
    #driver = webdriver.Chrome(ChromeDriverManager().install())  ## For windows

    driver.implicitly_wait(10)
    driver.get('http:/www.Google.com/')
    assert driver.title == "Google"
    driver.quit()

def test_google():

    driver = webdriver.Chrome(CHROMEDRIVER_PATH , options=options) ##For Linux
    #driver = webdriver.Chrome(ChromeDriverManager().install())  ## For windows

    driver.implicitly_wait(10)
    driver.get('http:/www.facebook.com/')
    assert driver.title == "Google"
    driver.quit()

def test_google():

    driver = webdriver.Chrome(CHROMEDRIVER_PATH , options=options) ##For Linux
    #driver = webdriver.Chrome(ChromeDriverManager().install())  ## For windows

    driver.implicitly_wait(10)
    driver.get('http:/www.instagram.com/')
    assert driver.title == "Google"
    driver.quit()

def test_google():

    driver = webdriver.Chrome(CHROMEDRIVER_PATH , options=options) ##For Linux
    #driver = webdriver.Chrome(ChromeDriverManager().install())  ## For windows

    driver.implicitly_wait(10)
    driver.get('http:/www.gmail.com/')
    assert driver.title == "Google"
    driver.quit()

def test_google():

    driver = webdriver.Chrome(CHROMEDRIVER_PATH , options=options) ##For Linux
    #driver = webdriver.Chrome(ChromeDriverManager().install())  ## For windows

    driver.implicitly_wait(10)
    driver.get('http:/www.reddif.com/')
    assert driver.title == "Google"
    driver.quit()


