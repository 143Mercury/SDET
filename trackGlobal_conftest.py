import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()
driver.get(link)
WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
driver.find_element(By.ID, "book").click()
driver.execute_script("window.scrollBy(0, 150);")
driver.implicity_wait(5)
x_element = driver.find_element(By.CSS_SELECTOR, "[id ='input_value']")
x = x_element.text
y = calc(x)
driver.find_element(By.CSS_SELECTOR, "[id ='answer']").send_keys(y)
formButton = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[type ='submit']"))
)
formButton.click()
# time.sleep(10) - если хотите самолично увидеть код
print(driver.switch_to.alert.text.split(': ')[-1])

