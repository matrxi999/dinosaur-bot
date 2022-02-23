from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path_to_extension = r"C:\Users\rainb\Desktop\FlaskMarket\dinosaur-bot\4.43.0_0"

chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)


driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
driver.get("https://www.trex-game.skipser.com/")