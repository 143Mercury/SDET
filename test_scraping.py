import requests
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


@pytest.mark.parametrize("tracking_number", [
    "EE064523226RU",
    "ASO2501GB02775299501",
    "LC566539063CN",
    "UT096870916NL",
    "LS574189320CH",
    "UK005021339NO",
    "JSHUA0000044601YQ",
    "DPK364084244303",
    "EB541831315TH",
    "9274899990995431341306",
    "TWN00430636",
])
def test_tracking_number(driver, tracking_number):
    # Navigate to the tracking site
    driver.get("https://track.global/ru")

    # Wait for the input form and the "Find" button to become visible
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/main/section/section[1]/div/div['
                                                    '1]/div/div/form/div/div[1]/label/input'))
    )
    input_field.send_keys(tracking_number)

    submit_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "top__search-btn"))
    )
    submit_button.click()

    # Wait for the tracking information or "not found" message to become visible
    try:
        tracking_info = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="widgetContentMain"]/section/div/div/div[2]'))
        )
        tracking_info_text = tracking_info.text
        slack_webhook_url1 = "Тут WebHook от Slack"
        requests.post(slack_webhook_url1,
                      json={
                          "text": f"Tracking number: {tracking_number}\nTracking information: {tracking_info_text}"})

    except:
        not_found_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="widgetContentMain"]/section/div/h3'))
        )
        not_found_message_text = not_found_message.text
        alternate_site_url = f"https://1trackapp.com/en/track/{tracking_number}"
        requests.get(alternate_site_url)
        slack_webhook_url2 = "Тут WebHook от Slack"
        requests.post(slack_webhook_url2,
                      json={"text": f"Tracking number: {tracking_number}\nInformation :"
                                    f"Not found on research site {alternate_site_url}\nNot found :"
                                    f"{not_found_message_text}"})
