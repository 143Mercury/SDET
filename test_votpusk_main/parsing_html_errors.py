import requests
from bs4 import BeautifulSoup

URL = "https://votpusk.ru/"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

if soup.find():
    print("No HTML errors found.")
else:
    print("HTML errors found.")
