from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import numpy as np 
import cv2
import pyautogui



DRIVER_PATH = Service("dinosaur-bot\chromedriver.exe")
URL = "https://trex-runner.com/"


def page_open(path, url):
    # browser page opening
    driver = webdriver.Chrome(service=path)
    driver.get(url)

    #setting basic parameters
    driver.set_window_size(1000, 600)
    driver.set_window_position(100, 100)

page_open(DRIVER_PATH, URL)

top, left, width, height = 360, 610, 100, 75

rtop, rleft, rwidth, rheight = 575, 590, 30, 25

while True:

    image = pyautogui.screenshot(region=(top, left, width, height))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    replay_btn = pyautogui.screenshot(region=(rtop, rleft, rwidth, rheight))
    replay_btn = cv2.cvtColor(np.array(replay_btn), cv2.COLOR_RGB2BGR)

    black_pixels_rpl = np.sum(replay_btn < 100)
    white_pixels_rpl = np.sum(replay_btn > 100)

    black_pixels = np.sum(image < 100)
    white_pixels = np.sum(image > 100)

    if black_pixels in range(1000, 20000):
        pyautogui.keyDown("space")

    if white_pixels in range(1000, 20000):
        pyautogui.keyDown("space")

    if black_pixels_rpl > 1650:
        pyautogui.click(x=(rleft+(rwidth/2)), y=(rtop+(rheight/2)))

    cv2.imshow('image', image)
    cv2.imshow('rpl', replay_btn)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break 