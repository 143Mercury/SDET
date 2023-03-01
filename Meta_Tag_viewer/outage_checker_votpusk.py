import pytest
import requests
from bs4 import BeautifulSoup


def test_meta_tags():
    url = "https://www.votpusk.ru/article"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    expected_title = "Статьи о туризме и путешествиях - В ОТПУСК.РУ"
    expected_description = "Статьи о туризме и путешествиях, обзоры туристических журналов, газет, публикации, обзоры."
    expected_charset = "UTF-8"
    expected_keywords = ["статьи о туризме, статьи о путешествиях"]
    expected_csrf_param = "_csrf-frontend"

    meta_tags = soup.find_all("meta")

    # Verify the title tag
    title_tag = soup.find("title")
    assert title_tag.string == expected_title

    # Verify the description meta tag
    description_tag = soup.find("meta", {"name": "description"})
    assert description_tag.get("content") == expected_description

    # Verify the author meta tag
    csrf_param_tag = soup.find("meta", {"name": "csrf-param"})
    assert csrf_param_tag.get("content") == expected_csrf_param

    # Verify the keywords meta tag
    keywords_tag = soup.find("meta", {"name": "keywords"})
    assert set(keywords_tag.get("content").split(", ")) == set(expected_keywords)
