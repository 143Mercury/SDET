import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.switch_to.window(driver.window_handles[0])
    yield driver
    driver.quit()


