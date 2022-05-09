import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    text = WebDriverWait(browser, '12').until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    button = browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text
    res = calc(x)

    input1 = browser.find_element(By.ID, 'answer').send_keys(res)
    button = browser.find_element(By.ID, 'solve').click()


    time.sleep(8)
