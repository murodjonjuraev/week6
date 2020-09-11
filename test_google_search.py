import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# scenario Google Search:
# 1. open browser. launch website google.com
# 2. type "selenium python in the search and hit enter
# 3. verify result is more than 20 mln
# 4. verify that it takes less the a second
# 5. close browser
# keywords: HTML, locator: xpath, id, cssSelector, name, link_name, partial_link_name, class_name


driver = webdriver.Chrome()

driver.get("https://google.com")
print("opened the browser and google website")
time.sleep(1)

search_text_box = driver.find_element_by_name("q")
print("identified google search box")

search_text_box.clear()
search_text_box.send_keys("python selenium")
print("cleared the search box then typed 'python selenium' words in it")

search_text_box.send_keys(Keys.ENTER)
print("hit the enter button")

result = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(result)
# "About 31,100,000 results (0.37 seconds)"
result_list = result.split()
result_num_str = result_list[1].replace(',', '')
result_num = int(result_num_str)
assert result_num > 20000000
print("Verifying result num passed")

result_time = float(result_list[3].replace('(', ''))
assert result_time < 1, "search took more then 1 sec"
print("verifying time less then 1sec passed")

time.sleep(1)
print("now closing the browser...")
driver.close()


