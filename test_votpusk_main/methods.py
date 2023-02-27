from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def do_click(driver, by_locator):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(by_locator)
        )
        element.click()
    except Exception as e:
        print("Test should to be able to pass")
        print(e)


def do_send_keys(driver, by_locator, keys):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        element.clear()
        element.send_keys(keys)
    except Exception as e:
        print("Can't find an element")
        print(e)


def do_wait_until_element_clickable(driver, element):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(element))


def do_wait_visibility_of_element_located(driver, element):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(element))


def do_double_click(driver, by_locator, double_click=True):
    element = driver.find_element(*by_locator)
    if double_click:
        action = ActionChains(driver)
        action.double_click(element).perform()
    else:
        element.click()


def do_click_nw(driver, by_locator):
    element = driver.find_element(by_locator)
    element.click()


def assert_visibility(driver, by_locator, timeout=15):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )
        assert element.is_displayed()
        assert element.location_once_scrolled_into_view == element.location
        print(f"Тест пройден успешно: элемент {by_locator} виден на странице")
    except Exception as e:
        print(f"Тест пройден не успешно: элемент {by_locator} или элемент вне зоны видимости ")
        print(f"Причина: {str(e)}")


def assert_text_visible(driver, text):
    try:
        element_present = EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]"))
        element_visible = EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]"))
        WebDriverWait(driver, 10).until(element_present)
        assert WebDriverWait(driver, 10).until(element_visible).is_displayed()
        print(f"Text '{text}' is visible on the page")
    except Exception as e:
        print(f"Error: {e}")
        raise AssertionError(f"Text '{text}' is not visible on the page")
