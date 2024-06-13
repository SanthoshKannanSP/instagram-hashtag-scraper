from dotenv import load_dotenv
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from seleniumbase import Driver
import time

load_dotenv()

SESSION_URL = os.environ.get("LOCALURL")
SESSION_ID = os.environ.get("SID")
TEXT_FILE = os.getenv("TEXTFILE")
FOLDER = os.getenv("FOLDER")
NUMBER_OF_POSTS = int(os.environ.get("NUM_POSTS"))
HASHTAG = os.environ.get("HASHTAG")



def create_driver_session(session_id, executor_url):

    options = Options()

    options.add_argument("--headless")
    options.add_argument("window-size=1400,1500")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities={},
        options=options
    )
    
    driver.session_id = session_id

    return driver

def collect(driver):

    textfile_name       = TEXT_FILE + ".txt"
    text_path           = os.getcwd()
    textfile_path       = os.path.join(text_path, textfile_name)
    
    if not os.path.exists(textfile_path):
        os.mknod(textfile_path)
        print("Created text file: " + textfile_name)

    images_all      = []
    url         = f"https://www.instagram.com/explore/tags/{HASHTAG}/"
    driver.get(url)
    time.sleep(2)
    images = []
    for post in range(NUMBER_OF_POSTS):
        try:
            images              = driver.find_elements(By.TAG_NAME,'img')
            for image in images:
                images_all.append(image.get_attribute('src'))
        except Exception as error:
            print(error)

        print("Adding to text file")
        with open(textfile_path, "r+") as outfile:
            text                = outfile.read()
            for image in images:
                img             = image.get_attribute('src')
                if isinstance(img, str):
                    if img in text:
                        print("Link already exists")
                    else:
                        outfile.write("\n"+str(img))
                        
        try:
            body                = driver.find_element(By.CSS_SELECTOR,'body')
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(5)
        except Exception as error:
            print(error)

        print("Completed")


def startpy():
    try:
        driver = Driver(browser="chrome",headed=True)
        driver.maximize_window()
        
        collect(driver = driver)

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            driver.quit()
            sys.exit(0)
        except SystemExit:
            driver.quit()
            os._exit(0)


if __name__ == '__main__':
    startpy()
