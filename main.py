import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = Service("chromedriver.exe")
URL = "https://trex-runner.com/"

def page_open(path, url):
    # browser page opening
    driver = webdriver.Chrome(service=path)
    driver.get(url)

    #setting basic parameters
    driver.set_window_size(1000, 600)
    driver.set_window_position(100, 100)


page_open(DRIVER_PATH, URL)