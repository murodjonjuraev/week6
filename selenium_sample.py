import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://google.com")
print("opened the browser and google website")
time.sleep(3)

search_text_box = driver.find_element_by_name("q")
print("identified google search box")

search_text_box.clear()
search_text_box.send_keys("python selenium")
print("cleared the search box then typed 'python selenium' words in it")

search_text_box.send_keys(Keys.ENTER)
print("hit the enter button")

time.sleep(3)
print("now closing the browser...")
driver.close()
