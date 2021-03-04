from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")
time.sleep(2)

login_button = driver.find_element_by_css_selector("header .focus-button-style")
login_button.click()
time.sleep(2)

login = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login.click()
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

fb_email = driver.find_element_by_xpath('//*[@id="email"]')
fb_email.send_keys(YOUR EMAIL)
fb_pass = driver.find_element_by_xpath('//*[@id="pass"]')
fb_pass.send_keys(YOUR PASS)
fb_pass.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)

allow_location = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(2)

notifications = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[2]')
notifications.click()
time.sleep(1)

cookies = driver.find_element_by_xpath('//*[@id="t--1032254752"]/div/div[2]/div/div/div[1]/button')
cookies.click()
time.sleep(3)

for n in range(100):
    time.sleep(1)
    try:
        like_button = driver.find_element_by_xpath("//*[@id='t--1032254752']/div/div[1]/div/main/div[1]/div/div/div["
                                                   "1]/div[1]/div[2]/div[4]/button")
        like_button.click()
        time.sleep(2)
    except ElementClickInterceptedException:
        try:
            no_thanks_button = driver.find_element_by_xpath("//*[@id='t-1222506740']/div/div/button[2]")
            no_thanks_button.click()
        except NoSuchElementException:
            time.sleep(2)
    except NoSuchElementException:
        not_interested = driver.find_element_by_xpath("//*[@id='t-1222506740']/div/div/div[2]/button[2]")
        not_interested.click()
        
driver.quit()
