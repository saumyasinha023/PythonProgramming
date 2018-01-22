from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://www.linkedin.com")
elem = driver.find_element_by_id("login-email")
elem_pass=driver.find_element_by_id("login-password")
elem_submit=driver.find_element_by_id("login-submit")
elem.clear()
elem_pass.clear()
elem.send_keys("vardaan.gupta27@gmail.com")
elem_pass.send_keys("Singhania@270808")
elem_submit.click()
driver.get("https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%221481%22%2C%22208643%22%2C%22853612%22%2C%223710655%22%2C%226121%22%2C%2273035%22%2C%2210061%22%2C%22270603%22%2C%22655717%22%2C%2278768%22%2C%22116018%22%2C%221448259%22%2C%222340505%22%2C%22399098%22%2C%22772375%22%5D&page=2")
time.sleep(10)
while True:
    #try:
    connect=driver.find_elements_by_css_selector(".search-result__actions--primary.button-secondary-medium.m5")
    for each in connect:
        if not each.is_enabled():
            continue
        each.click()
        time.sleep(2)
        try:
            popup=driver.find_element_by_css_selector(".button-primary-large.ml1")
        except:
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        popup.click()
        time.sleep(2)
    next_button = driver.find_element_by_css_selector(".next")
    next_button.click()
    time.sleep(5)

    # except e:
    #     print("Wrong")


print(connect)
time.sleep(10)

time.sleep(10)
assert "No results found." not in driver.page_source
driver.close()