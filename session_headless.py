from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import string
import random
import wget
import re

# Import Driver
from webdriver_manager.chrome import ChromeDriverManager


load_dotenv()

IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")
NUM_POSTS = int(os.getenv("NUM_POSTS"))
TEXTFILE = os.getenv("TEXTFILE")
FOLDER = os.getenv("FOLDER")

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")




driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome(chrome_options=options,
#                           executable_path=chromedriver_path)


def login():
    username = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username.clear()
    username.send_keys(IG_USERNAME)
    time.sleep(2)
    password.clear()
    password.send_keys(IG_PASSWORD)
    time.sleep(2)

    button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']"))).click()

    # Not now and Cancel buttons
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="_a9-- _a9_1"]'))).click()
    time.sleep(2)
    # not_now2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    #     (By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]'))).click()

    sid = driver.session_id
    localurl = driver.command_executor._url

    print("Session ID: " + sid)
    print("\nLocal URL: " + localurl)


def startpy():
    driver.get("http://www.instagram.com")
    driver.maximize_window()

    login()


if __name__ == '__main__':
    startpy()
