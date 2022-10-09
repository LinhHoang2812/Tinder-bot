import selenium
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

EMAIL = os.environ["EMAIL"]
PASS_WORD = os.environ["PASS"]

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get("https://tinder.com")
driver.maximize_window()

driver.implicitly_wait(10)

cookies = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()

time.sleep(3)



main_window = driver.current_window_handle

# click whatever button it is to open popup
log_in = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()



#after opening popup, change window handle
handles = driver.window_handles
for handle in driver.window_handles:
    if handle != main_window:
        popup = handle
        driver.switch_to.window(popup)
time.sleep(2)
facebook = driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook.click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
facebook_cookies = driver.find_elements(By.CSS_SELECTOR,"._9xo5 button")[0]
facebook_cookies.click()

email = driver.find_element(By.NAME,"email")
email.send_keys(EMAIL)

password = driver.find_element(By.NAME,"pass")
password.send_keys(PASS_WORD)

facebook_log_in= driver.find_element(By.NAME,"login")
facebook_log_in.click()



driver.switch_to.window(main_window)

location_allow = driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[3]/button[1]')
location_allow.click()

no_notif = driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[3]/button[2]')
no_notif.click()

time.sleep(10)
for _ in range(0,100):
    try:

        like_button = driver.find_element(By.CSS_SELECTOR,'.Bdc\(\$c-ds-border-gamepad-like-default\) button')
        like_button.click()
        time.sleep(5)
    except ElementClickInterceptedException:
        print("Tinder popup")
        try:
            not_interested = driver.find_elements(By.CSS_SELECTOR,'.Pb\(8px\) button')[1]
            not_interested.click()
            print("click not interested")


            like_button = driver.find_element(By.CSS_SELECTOR, '.Bdc\(\$c-ds-border-gamepad-like-default\) button')
            like_button.click()
        except NoSuchElementException:
            time.sleep(5)



