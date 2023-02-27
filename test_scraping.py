import requests
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize("tracking_number", [
    "ECMOF00000571550",
    "ECAMZ01000104203",
    "APECHUS203005191",
    "1LSCXLZ000V0PNK",
    "1LSCZ5A000UYESC",
    "1LSCYG5000VG0QW",
    "1LSCYG5000Z08QT",
    "RH969059067AT",
    "CA000060551LY",
    "EZ903260796",
    "LX242920433CN",
    "ML5610933",
    "0000000000000000",
    "6163774380",
    "7000600225694009",
    "HKG0972225",
    "LZ044500518DK",
    "128185344",
    "128185344",
    "44538407-1",
    "712103909775",
    "006481328195",
    "056450540554",
    "712103703290",
    "006581108337",
    "710292739376",
    "CPAK2HC0248947",
    "0123028215783336",
    "9017011200096436",
    "051144752805",
    "211144948334",
    "RO300586663EE",
    "RR236929464EE",
    "RO300586663EE",
    "EM082980995DK",
    "TWAL564811",
    "RR913088725BA",
    "RY957371958CN",
    "RO131881872RU",
    "RR055897653BA",
    "RF930041215HR",
    "LT662934070NL",
    "RY538580590CN",
    "LT679205407NL",
    "EM118683360HR",
    "CE281407557HR",
    "RG233269855HR",
    "000233725",
    "27731395",
    "505393321426",
    "pl-005121-S11640",
    "pl-080735-7125",
    "pl-000193-1584-vtm929",
    "pl-005167-000Т-031622",
    "AT0000948980",
    "WS764182",
    "RC045714925MK",
    "TYZRB0001548168YQ",
    "TYZRB0003823178YQ",
    "TYZPH0015011363YQ",
    "21-01321018731",
    "23704392",
    "23791614",
    "2103681089962",
    "5403-3310010",
    "969-415923",
    "RB120328416MD",
    "RB120328416MD",
    "RI067577064UA",
    "RI065536844UA",
    "JSHUA0000044601YQ",
    "JSHRS0000000346YQ",
    "JSHRS0000000002YQ",
    "40624493",
    "LS060502225NL",
    "LS163846863NL",
    "LS391727933NL",
    "RU744760675NL",
    "RU744760675NL",
    "RU744760675NL",
    "RU747466029NL",
    "RU894515273NL",
    "UD675148182NL",
    "RI310935289BG",
    "RI325086796BG",
    "CH126899650AU",
    "RO300586663EE",
    "LX664911125NL",
    "BLGKH0109594105YQ",
    "BLGSL1117929007YQ",
    "H1018660452486101043",
    "LP521102701CN",
    "4PX3000198230101CN",
    "ZVT35873080",
    "210290090485",
    "SHP1499738",
    "44436922-0",
    "alp2584930",
    "0000158793364",
    "0000262178509",
    "AGE124292997",
    "SLPU00032513RU",
    "RP1287257",
    "EG714124256KR",
    "LK073103726KR",
    "RW20734069",
    "QFLQQ3000054686YQ",
    "TSE2827713",
    "aepu0007127431ru2",
    "370722151259330246",
    "1900445",
    "СП-п284923",
    "КРК-013031",
    "RA179204425LV",
    "ДЖЗКРД0101694603",
    "МСККГД0062667526",
    "4643422",
    "6459575",
    "ETSSD1027127932YQ",
    "HJYTE2123586067YQ",
    "HJYTE7758381311YQ",
    "HJYTE2124840389YQ",
    "546579717207170014",
    "11410047604570",
    "760064823",
    "WEBN4006506",
    "D392928",
    "J285343",
    "EB542513662TH",
    "EE333516665NG",
    "5557565114",
    "1200164116",
    "3206725118",
    "3063603114",
    "3234735115",
    "179303175117",
    "LS574189320CH",
    "RX130359700JP",
    "RX131715314JP",
    "RX136369444JP",
    "99990026978669",
    "SPON655159",
    "SPON263820",
    "SPON263821",
    "RA137997539LV",
    "CU001283966AM",
    "RF103420101AM",
    "RG890001352BE",
    "LD270562604BE",
    "RR952193178CZ",
    "RR276202785CZ",
    "RR402883636CZ",
    "90356309333",
    "QR21309472",
    "QR13278702",
    "QR17241473",
    "QR13376544",
    "RE000776995RU",
    "QR17576555",
    "CGSBY0100000204YQ",
    "CGSRU0500007905YQ",
    "CGSRU0500030290YQ",
    "CGSRU0500070323YQ",
    "CGSRU0500079408YQ",
    "1098500603",
    "2188356773",
    "EFS1002740138",
    "EFS1003510959",
    "EFS1003516354",
    "ANTPK1423310425YQ",
    "ANTPK3905097279YQ",
    "ANTLK1431459056YQ",

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
        slack_webhook_url1 = "https://hooks.slack.com/services/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"
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
        slack_webhook_url2 = "https://hooks.slack.com/services/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"
        requests.post(slack_webhook_url2,
                      json={"text": f"Tracking number: {tracking_number}\nInformation :"
                                    f"Не найдено в Track-Global- Но обнаружено тут {alternate_site_url}\nAlert:"
                                    f"{not_found_message_text}"})
