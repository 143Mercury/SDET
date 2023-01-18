import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class testButton(unittest.TestCase):
    def setUp(self):
        self.link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()

    def test_button(self):
        self.browser.get(self.link)

        required_fields = self.browser.find_elements(By.CSS_SELECTOR, 'input[required]')
        for field in required_fields:
            field.send_keys('Прошла вечность')

        button = self.browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        time.sleep(1)

        welcome_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Congratulations', welcome_text)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def tearDown(self):
        time.sleep(10)
        self.browser.quit()
