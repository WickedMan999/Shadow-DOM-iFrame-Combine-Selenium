from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Variables
base_url = "https://selectorshub.com"
endpoint = "shadow-dom-in-iframe/"

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

# Locate iframe
iframe = driver.find_element(By.CSS_SELECTOR, "#pact")

# Switch to frame
driver.switch_to.frame(iframe)

if iframe is None:
    print(f"iframe with selector {iframe} cannot be located")
else:
    # Locating nearby element of DOM 1
    shadow_dom1 = driver.find_element(
        By.CSS_SELECTOR, "#snacktime").shadow_root

    if shadow_dom1 is None:
        print(f"Shadow Dom 1 with selector {shadow_dom1} is not found")

    else:
        # Locating 'tea' text field element inside of Dom 1
        tea = shadow_dom1.find_element(By.CSS_SELECTOR, "#tea")
        tea.send_keys("YES")

        # Get the value of the input field
        tea_message = tea.get_attribute('value')
        print('Do you love tea:', tea_message)

        # Locating nearby element of DOM 2 i.e. inside of DOM 1
        shadow_dom2 = shadow_dom1.find_element(
            By.CSS_SELECTOR, "#app2").shadow_root

        if shadow_dom2 is None:
            print(f"Shadow Dom 2 with selector {shadow_dom2} is not found")

        else:
            # Enter text in launch time
            launch_time = shadow_dom2.find_element(By.CSS_SELECTOR, "#pizza")
            launch_time.send_keys("9 P.M.")

            # Get the value of the input field
            launch_time_message = launch_time.get_attribute('value')
            print('Lunch Time is:', launch_time_message)


time.sleep(5)
