from selenium import webdriver


class BaseTest:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
