import argparse
import requests

URLS = ["https://www.dhl.com/us-en/home.html", "https://www.fedex.com/en-us/home.html", "https://www.ups.com/us/en/Home.page"]


def check_delivery_service(url):
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Проверить статус служб доставки')
    parser.add_argument('-u', '--url', type=str, required=True, help='URL службы доставки для проверки')
    args = parser.parse_args()

    url = args.url
    status = check_delivery_service(url)

    if status:
        print(f"Служба доставки по адресу {url} активна")
    else:
        print(f"Служба доставки по адресу {url} неактивна")
else:
    for service in URLS:
        status = check_delivery_service(service)
        if status:
            print(f"Служба доставки по адресу {service} активна")
        else:
            print(f"Служба доставки по адресу {service} неактивна")