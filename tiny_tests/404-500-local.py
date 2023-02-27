from selenium import webdriver


def check_delivery_service(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        assert "404" not in driver.page_source, f"Error: 404 Not Found"
        assert "500" not in driver.page_source, f"Error: 500 Internal Server Error"
        return True
    except AssertionError as error:
        return False, error
    finally:
        driver.quit()


delivery_services = [
    "https://www.dhl.com/us-en/home.html",
    "https://track-global-2.com",
    "https://track-global-3.com"
]

for url in delivery_services:
    print("Checking", url)
    response = check_delivery_service(url)
    if response == True:
        print("Success")
    else:
        print("Error:", response[1])
