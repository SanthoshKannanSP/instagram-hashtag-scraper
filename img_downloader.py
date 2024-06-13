from dotenv import load_dotenv
import os
import sys
from selenium.webdriver.support import expected_conditions as EC
import time
import string
import random
import wget
import re

load_dotenv()

TEXT_FILE   = os.getenv("TEXTFILE")
FOLDER      = os.getenv("FOLDER")

def download():
    
    all_content         = []
    path_folder         = os.getcwd()
    path_folder         = os.path.join(path_folder, FOLDER)
    
    if not os.path.exists(path_folder):
        os.mkdir(path_folder)

    file_path           = TEXT_FILE + ".txt"
    if(os.path.exists(file_path)):
        my_file         = open(file_path, "r")
        content         = my_file.read()
        content_list    = content.split("\n")
        content_list    = list(set(content_list))
        all_content.append(content_list)
        my_file.close()

    from itertools import chain
    flatten_list        = list(chain.from_iterable(all_content))
    flatten_list        = list(set(flatten_list))

    for image in flatten_list:
        res             = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=15))
        save_as         = os.path.join(path_folder, res + '.jpg')
        try:
            wget.download(image, save_as)
            if(os.path.getsize(save_as) < 10000):
                os.remove(save_as)
        except Exception as e2:
            print(image)
            print(e2)
    print("\nCompleted")

def startpy():
    download()


if __name__ == '__main__':
    startpy()
