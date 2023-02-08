import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize("lower_number", [
    "pl-005121-S11640",
    "ASO2501GB02775299501",
    "lC566539063CN",
    "uT096870916nL",
    "ls574189320Ch",
    "uk005021339NO",
    "jshua0000044601Yq",
    "dpk364084244303",
    "eb541831315tH",
    "9274899990995431341306",
    "twn00430636",
])
def test_tracking_number(driver, lower_number):
    # Navigate to the tracking site
    driver.get("https://track.global/ru")

    # Wait for the input form and the "Find" button to become visible
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/main/section/section[1]/div/div['
                                                    '1]/div/div/form/div/div[1]/label/input'))
    )
    input_field.send_keys(lower_number)

    submit_click = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "top__search-btn"))
    )
    submit_click.click()

    try:
        tracking_info = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="widgetContentMain"]/section/div/div/div[2]'))
        )
        assert tracking_info, "does not match the result"
        assert True

    except:
        not_found_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="widgetContentMain"]/section/div/h3'))
        )
        assert not_found_message, "Did not get any matches"
        assert False
