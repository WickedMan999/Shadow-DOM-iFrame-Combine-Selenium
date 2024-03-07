from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Variables
base_url = "https://selectorshub.com"
endpoint = "iframe-in-shadow-dom/"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# Actionchains Instance
action = ActionChains(driver)

# Open URL
driver.get(f"{base_url}/{endpoint}")
time.sleep(5)

# Locating nearby element of DOM
shadow_dom = driver.find_element(
    By.CSS_SELECTOR, "#userName").shadow_root

# Locate 'username' text field element inside of Dom
username = shadow_dom.find_element(By.CSS_SELECTOR, "#kils")

# Locating the iframe that is inside of shadow dom. NOTE when iframe is inside of shadow dom we cannot locate element using XPATH
iframe = shadow_dom.find_element(By.CSS_SELECTOR, "#pact1")

# Switch to iframe
driver.switch_to.frame(iframe)

time.sleep(1)

# Locate text element named 'Destiny' inside iframe which is inside of shadow dom.
# NOTE Xpath can be use on element that is inside of iframe despite iframe being inside of shadow dom
destiny = driver.find_element(By.XPATH, "//input[@id='glaf']")

# Enter value
destiny.send_keys("Age of Aquarius")

# Get the value of the input field
entered_username = destiny.get_attribute('value')
print('Entered username is:', entered_username)

time.sleep(5)
