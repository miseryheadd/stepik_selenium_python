import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)


try:
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)
    btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn.click()
    alert_text = browser.switch_to.alert.text
    print(alert_text.split()[-1])

finally:
    time.sleep(5)
    browser.quit()
