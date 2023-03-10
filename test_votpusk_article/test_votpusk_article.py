import random
import time
import pytest
from SDET.test_votpusk_article.Config import configurations
from SDET.test_votpusk_article import methods, article_sl
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


@pytest.mark.sanity()
def test_form_random(driver):
    driver.get(configurations.URL)
    # Ищем фоновый макет сайта
    title = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(article_sl.title)
    )
    # Проверяем его на активность
    assert title.is_enabled(), "Форма выбора страны задисейблена"
    # Поиск формы выбора страны
    country = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(article_sl.dropdown_country)
    )
    # Проверка активности фитчи
    assert country.is_enabled(), "Форма задисейблена"
    # Поиск и проверка на наличие выпадающего списка в контейнере
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(article_sl.dropdown_country)
    )
    assert len(driver.find_elements(*article_sl.dropdown_country)) > 0, "Выпадающий список не найден"
    methods.do_click(driver, article_sl.dropdown_country)
    try:
        action = ActionChains(driver)
        enter_pressed = False
        while True:
            action.send_keys(Keys.DOWN).perform()
            time.sleep(0.5)
            if not country.is_displayed():
                break
            if random.randint(1, 10) == 4:
                time.sleep(random.uniform(0.5, 2.0))
                action.send_keys(Keys.ENTER).perform()
                enter_pressed = True
                break
            if enter_pressed:
                country.send_keys(Keys.ESCAPE)
    finally:
        city = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(article_sl.dropdown_city)
        )
        assert city.is_enabled(), "Форма выбора города не активна"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(article_sl.dropdown_city)
        )
        assert len(driver.find_elements(*article_sl.dropdown_city)) > 0, "Выпадающий список форма городов отсутствует"
        methods.do_click(driver, article_sl.dropdown_city)
        try:
            action = ActionChains(driver)
            enter_pressed = False
            while True:
                action.send_keys(Keys.DOWN).perform()
                time.sleep(0.5)
                if not city.is_displayed():
                    break
                if random.randint(1, 10) == 4:
                    time.sleep(random.uniform(0.5, 2.0))
                    action.send_keys(Keys.ENTER)
                    enter_pressed = True
                    break
                if enter_pressed:
                    city.send_keys(Keys.ESCAPE)
        finally:
            themes = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(article_sl.dropdown_themes)
            )
            assert themes.is_enabled(), "Форма тематик недоступна"
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(article_sl.dropdown_themes)
            )
            assert len(driver.find_elements(*article_sl.dropdown_themes)) > 0, "Выпадающий список тематик недоступен"
            methods.do_click(driver, article_sl.dropdown_themes)

            action = ActionChains(driver)
            enter_pressed = False
            while True:
                action.send_keys(Keys.DOWN).perform()
                time.sleep(0.5)
                if not themes.is_displayed():
                    break
                if random.randint(1, 10) == 4:
                    time.sleep(random.uniform(0.5, 2.0))
                    action.send_keys(Keys.ENTER).perform()
                    enter_pressed = True
                    break
                if enter_pressed:
                    driver.execute_script("window.stop()")
                else:
                    submit_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable(article_sl.submit_button)
                    )
                    assert submit_button.is_displayed() \
                           and submit_button.is_enabled(), "Кнопка не активна либо не кликабельна"


@pytest.mark.sanity()
def test_assert_themes(driver):
    driver.get(configurations.URL)
    driver.execute_script("window.scrollBy(0, 200)")
    try:
        for x in range(1, 8):
            slid_topics = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(getattr(article_sl, f"slid_topics{x}"))
            )
            assert slid_topics.is_enabled(),f"Слайдер с {x} недоступен"
    finally:
        slid_arrow = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(article_sl.slid_arrow_next)
        )
        assert slid_arrow.is_displayed(), "Стрелка слайдера отсутствует"
        for i in range(5):
            time.sleep(0.5)
            slid_arrow.click()


@pytest.mark.sanity()
def test_assert_news(driver):
    driver.get(configurations.URL)
    driver.execute_script("window.scrollBy(0, 550)")
    prev_arrow = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(article_sl.news_slider_prev)
    )
    assert prev_arrow.is_displayed(), "Навигационная стрелка не доступна"
    for i in range(2):
        time.sleep(0.3)
        prev_arrow.click()
    try:
        for i in range(1, 4):
            news_paper = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(getattr(article_sl, f"news_paper{i}"))
            )
            assert news_paper.is_enabled(), f"Блок {i} в статьях отсутствует"

            read_more = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(getattr(article_sl, f"read_more{i}"))
            )
            assert read_more.is_enabled(), f"Ссылка 'Читать дальше' не доступна для блока {i}"
    finally:
        next_arrow = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(article_sl.news_slider_next)
        )
        assert next_arrow.is_displayed(), "Навиг стрелка не доступна"
        for i in range(3):
            time.sleep(0.3)
            next_arrow.click()

        prev_arrow = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(article_sl.news_slider_prev)
        )
        assert next_arrow.is_displayed(), "Навиг стрелка не доступна"
        for i in range(3):
            time.sleep(0.3)
            prev_arrow.click()

        for i in range(1, 4):
            category_locators = getattr(article_sl, f"category{i}")
            category = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(category_locators)
            )
            assert category.is_enabled(), f"Блок {i}не действителен"


@pytest.mark.sanity()
def test_assert_news(driver):
    driver.get(configurations.URL)
    driver.execute_script("window.scrollBy(0, 1150)")
    try:
        container_num = 1
        while container_num <= 5:
            container = None
            while not container:
                try:
                    container = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located(getattr(article_sl, f"article_container{container_num}"))
                    )
                except TimeoutException:
                    # если контейнер не найден, кликаем на кнопку "Дальше" и пытаемся снова найти контейнер
                    articles_next = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable(article_sl.articles_arrow_next)
                    )
                    articles_next.click()
            assert container.is_enabled(), f"Блок{container_num} контейнеров не действителен"
            container_num += 1
    finally:
        time.sleep(2)

