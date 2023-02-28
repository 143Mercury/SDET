import random
import time
import pytest
from SDET.test_votpusk_main.Config import configuration
from SDET.test_votpusk_main import methods, css_sl
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.mark.sanity()
def test_tour_rus(driver):
    driver.get(configuration.URL)
    # Форма выбора города
    city_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(css_sl.city_dropdown)
    )
    assert city_input.is_enabled(), "Поле ввода не доступно для ввода данных"
    methods.do_send_keys(driver, css_sl.city_dropdown, "Москва")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(css_sl.city_dropdown_item)
    )
    assert len(driver.find_elements(*css_sl.city_dropdown_item)) > 0, "Список городов не появился"
    methods.do_click(driver, css_sl.city_dropdown_item)
    # Форма выбора тура
    attractions_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(css_sl.attractions_checkbox)
    )
    assert attractions_checkbox.is_enabled(), "Поле выбора типа туров не доступно"
    driver.execute_script("window.scrollBy(0, 125)")
    methods.do_click(driver, css_sl.form_attractions)
    methods.do_click(driver, css_sl.type_attractions)
    driver.implicitly_wait(3)
    assert attractions_checkbox.is_enabled(), "Тип туров был не выбран"
    # Форма выбора даты
    calendar_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(css_sl.click_on_calendar)
    )
    methods.do_double_click(driver, css_sl.click_on_calendar)
    assert calendar_icon.is_enabled(), "Календарь не открылся"
    methods.do_click(driver, css_sl.pick_the_data)
    calendar_icon2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(css_sl.click_on_calendar2)
    )
    methods.do_click(driver, css_sl.click_on_calendar2)
    assert calendar_icon2.is_enabled(), "Календарь-2 не открылся "
    methods.do_click(driver, css_sl.pick_the_data2)

    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(css_sl.displayed_button)
    )
    methods.do_click(driver, css_sl.displayed_button)
    assert accept_button.is_displayed() \
           and accept_button.is_enabled(), "Кнопка не обнаружена на странице формы либо не кликабельна"


@pytest.mark.sanity()
def test_tour_world(driver):
    driver.get(configuration.URL)
    # Форма выбора города
    choose_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(css_sl.chose_option)
    )
    methods.do_click(driver, css_sl.chose_option)
    assert choose_option.is_enabled() \
           and choose_option.is_displayed(), "Кнопка смены опции вида тура не доступна и не встроена "
    where = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(css_sl.where)
    )
    methods.do_send_keys(driver, css_sl.where, "Москва")
    assert where.is_enabled(), "Поле ввода не доступна"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.list_destinations)
    )
    assert len(driver.find_elements(*css_sl.list_destinations)) > 0, "Список городов не появился"
    methods.do_click(driver, css_sl.where)
    # Удаление дефолтного выражения
    default_value = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.remove_arguments)

    )
    default_value.clear()
    city = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.city)
    )
    assert city.is_enabled(), "Поле ввода не доступно"
    methods.do_send_keys(driver, css_sl.city, "Воронеж")
    departure_items = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.departure_items)
    )
    assert departure_items.is_enabled(), "Список городов не появился"
    methods.do_click(driver, css_sl.city)
    # Форма выбора календаря
    calendar = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.calendar_checkin)
    )
    assert calendar.is_enabled(), "Календарь не открылся"
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.calendar_checkin)
    )
    methods.do_click(driver, css_sl.calendar_checkin)
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.next_arrow)
    )
    methods.do_click(driver, css_sl.next_arrow)
    driver.execute_script("window.scrollBy(0, 200)")
    choose_date = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.choose_date)
    )
    assert choose_date.is_enabled(), "Дата не выбрана"
    methods.do_click(driver, css_sl.choose_date)

    dropdown = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.dropdown_select)
    )
    assert dropdown.is_enabled(), "Поле выбора количества ночей не доступна"
    methods.do_click(driver, css_sl.dropdown_select)
    add_nights = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.dropdown_select_to)
    )
    assert add_nights.is_enabled(), "form error"
    for i in range(5):
        add_nights.click()

    add_tourist = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.dropdown_select_tourist)
    )
    assert add_tourist.is_enabled(), "Инсерты добавления туристов не активны"
    for i in range(4):
        add_tourist.click()

    submit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.button_submitTours)
    )
    assert submit_button.is_displayed() and submit_button.is_enabled(), "Кнопка отсутствует или не кликабельна"
    methods.do_click(driver, css_sl.button_submitTours)


@pytest.mark.sanity()
def test_form_hotel(driver):
    driver.get(configuration.URL)
    driver.execute_script("window.scrollBy(0, 175)")
    # Проверка формы поиска отелей
    hotel_sign = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.hotel_sign)
    )
    assert hotel_sign.is_enabled(), "Кнопка перехода к функциям поиска отелей недоступна"
    methods.do_click(driver, css_sl.hotel_sign)
    hotel_form = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.hotel_form)
    )
    assert hotel_form.is_enabled(), "Форма не активна или задисейблена"
    methods.do_send_keys(driver, css_sl.hotel_form, "Москва")
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.hotel_form)
    )
    assert len(driver.find_elements(*css_sl.hotel_form)) > 0, "Нет выпадающего списка городов"
    methods.do_click(driver, css_sl.hotel_form)
    # Проверка календаря
    calendar = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.hotel_checkin)
    )
    assert calendar.is_enabled(), "Календарь не активный"
    methods.do_click(driver, css_sl.hotel_checkin)
    methods.do_click(driver, css_sl.hotel_data)
    calendar2 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.hotel_data2)
    )
    assert calendar2.is_enabled(), "Календарь2 и дата не активны"
    methods.do_click(driver, css_sl.hotel_data2)
    # Проверка дропдауна + выбор кол-тво проживающих
    dropdown = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.hotel_dropdown)
    )
    assert dropdown.is_enabled(), "Дропдаун отелей не активный"
    methods.do_click(driver, css_sl.hotel_dropdown)
    add_guests = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.add_guests)
    )
    assert add_guests.is_enabled(), "Функция добавлений гостей недоступна"
    for i in range(4):
        add_guests.click()

    dropdown_kids = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.dropdown_kids_option)
    )
    assert dropdown_kids.is_enabled(), "Выпадающий список выбора кол-тва детей отсутствует"
    methods.do_click(driver, css_sl.dropdown_kids_option)
    add_kids = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.add_kids)
    )
    assert add_kids.is_enabled(), "Функция добавления кол-тва детей не активна"
    methods.do_click(driver, css_sl.add_kids)

    submit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.hotel_submit)
    )
    assert submit_button.is_displayed() and submit_button.is_enabled(), "Кнопка отсутствует или не кликабельна"
    methods.do_click(driver, css_sl.hotel_submit)


@pytest.mark.sanity()
def test_form_train(driver):
    driver.get(configuration.URL)
    driver.execute_script("window.scrollBy(0, 175)")
    # Проверка формы поиска билетов
    train_sign = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.train_sign)
    )
    assert train_sign.is_enabled() \
           and train_sign.is_displayed(), "Кнопка перехода к функциям жд билеты не активна или не кликабельна"

    methods.do_click(driver, css_sl.train_sign)

    train_form = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.train_form_first)
    )
    assert train_form.is_enabled(), "Форма не активна или элемент недоступен"
    methods.do_send_keys(driver, css_sl.train_form_first, "Воронеж")
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.list_station)
    )
    assert len(driver.find_elements(*css_sl.list_station)) > 0, "Видимый список отсутствует"
    methods.do_click(driver, css_sl.train_form_first)

    train_form2 = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.train_form_second)
    )
    assert train_form2.is_enabled(), "Форма поиска билетов не активна"
    methods.do_send_keys(driver, css_sl.train_form_second, "Санкт-Петербург")
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.list_station2)
    )
    assert len(driver.find_elements(*css_sl.list_station2)) > 0, "Видимый список отсутствует"
    methods.do_click(driver, css_sl.train_form_second)

    calendar = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.train_calendar)
    )
    assert calendar.is_enabled(), "Календарь не активный"
    methods.do_click(driver, css_sl.train_calendar)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.calendar_date)
    )
    methods.do_click(driver, css_sl.calendar_date)
    calendar_arrow = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.date_arrow)
    )
    assert calendar_arrow.is_enabled(), "Стрелка смены даты отсутствует"
    methods.do_click(driver, css_sl.date_arrow)
    calendar2 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.calendar_date2)
    )
    assert calendar2.is_enabled(), "В календаре отсутствует выбранное число"
    methods.do_click(driver, css_sl.calendar_date2)
    driver.implicitly_wait(3)
    submit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.train_submit)
    )
    assert submit_button.is_displayed() \
           and submit_button.is_enabled(), "Кнопка отсутствует или не кликабельна"
    methods.do_click(driver, css_sl.train_submit)


@pytest.mark.sanity()
def test_routs_form(driver):
    driver.get(configuration.URL)

    routs_sign = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.routs_sign)
    )
    assert routs_sign.is_enabled(), "Кнопка перехода к функциям поиска маршруты недоступна"
    methods.do_click(driver, css_sl.routs_sign)

    routs_form = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(css_sl.routs_form)
    )
    assert routs_form.is_enabled(), "Форма поиска маршрутов не активна"
    methods.do_send_keys(driver, css_sl.routs_form, "Краснодар")
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.routs_destinations1)
    )
    assert len(driver.find_elements(*css_sl.routs_destinations1)) > 0, "Видимый список городов отсутствует"
    methods.do_click(driver, css_sl.routs_form)

    routs_form2 = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(css_sl.routs_form2)
    )
    assert routs_form2.is_enabled(), "Форма поиска маршрута не активна"
    methods.do_send_keys(driver, css_sl.routs_form2, "Саратов")
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.routs_destinations2)
    )
    assert len(driver.find_elements(*css_sl.routs_destinations2)) > 0, "Выпадающий список городов"
    methods.do_click(driver, css_sl.routs_form2)

    submit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.routs_submit)
    )
    assert submit_button.is_displayed() \
           and submit_button.is_enabled(), "Кнопка отсутствует или не кликабельна"
    methods.do_click(driver, css_sl.routs_submit)


@pytest.mark.sanity()
def test_city_country(driver):
    global dropdown_city
    driver.get(configuration.URL)

    city = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.city_country_sign)
    )
    assert city.is_enabled(), "Кнопка к перехода к функциям поиска стран и городов не активна"
    methods.do_click(driver, css_sl.city_country_sign)
    dropdown_country = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.dropdown_country)
    )
    assert dropdown_country.is_enabled(), "Выпадающий список отсутствует"
    methods.do_click(driver, css_sl.dropdown_country)

    try:
        action = ActionChains(driver)
        enter_pressed = False
        while True:
            action.send_keys(Keys.DOWN).perform()
            time.sleep(0.5)
            if not dropdown_country.is_displayed():
                break
            if random.randint(1, 10) == 3:
                time.sleep(random.uniform(0.5, 2.0))
                action.send_keys(Keys.ENTER).perform()
                enter_pressed = True
                break
        if enter_pressed:
            dropdown_country.send_keys(Keys.ESCAPE)
    except:
        dropdown_city = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(css_sl.dropdown_city)
        )
        assert dropdown_country.is_enabled(), "Выпадающий список отсутствует"
        methods.do_click(driver, css_sl.dropdown_city)

    action = ActionChains(driver)
    enter_pressed = False
    while True:
        action.send_keys(Keys.DOWN).perform()
        time.sleep(0.5)
        if not dropdown_city.is_displayed():
            break
        if random.randint(1, 5) == 2:
            time.sleep(random.uniform(0.5, 2.0))
            action.send_keys(Keys.ENTER).perform()
            enter_pressed = True
            break
    if enter_pressed:
        driver.execute_script("window.stop()")
    else:
        submit_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(css_sl.c_c_submit)
        )
        assert submit_button.is_displayed() \
               and submit_button.is_enabled, "Кнопка отсутствует или не кликабельна"
        methods.do_click(driver, css_sl.c_c_submit)


@pytest.mark.sanity()
def test_motion_links(driver):
    driver.get(configuration.URL)
    tours = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.tours)
    )
    assert tours.is_enabled() and tours.is_displayed(), "Опция 'Туры' не активна или не кликабельная"
    methods.assert_visibility(driver, css_sl.tours)
    hotels = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.hotels)
    )
    assert hotels.is_enabled() and hotels.is_displayed(), "Опция 'Туры' не активна или не кликабельная"
    methods.assert_visibility(driver, css_sl.hotels)
    train = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.trains)
    )
    assert train.is_enabled() and train.is_displayed(), "Опция 'Туры' не активна или не кликабельная"
    methods.assert_visibility(driver, css_sl.trains)
    routs = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.routs)
    )
    assert routs.is_enabled() and routs.is_displayed(), "Опция 'Туры' не активна или не кликабельная"
    methods.assert_visibility(driver, css_sl.routs)
    attractions = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.attractions)
    )
    assert attractions.is_enabled() and attractions.is_displayed(), "Опция 'Туры' не активна или не кликабельная"
    methods.assert_visibility(driver, css_sl.attractions)


@pytest.mark.sanity()
def test_sliders(driver):
    driver.get(configuration.URL)
    driver.execute_script('window.scrollBy(0, 550)')

    adigay = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(css_sl.adigay)
    )
    assert adigay.is_enabled(), "Один из элементов слайдера не активный"

    baikal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(css_sl.baikal)
    )
    assert baikal.is_enabled(), "Один из слайдеров 'Туры' не активный"

    dagestan = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(css_sl.dagestan)
    )
    assert dagestan.is_enabled(), "Ошибка слайдера в блоке 'Туры'"

    next_arrow = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(css_sl.sliders_arrowR)
    )
    assert next_arrow.is_enabled(), "Навигационная стрелка не присутствует либо не кликабельна"
    methods.do_click(driver, css_sl.sliders_arrowR)
    back_arrow = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.sliders_arrowL)
    )
    assert back_arrow.is_displayed(), "Навигационная стрелка отсутствует"
    methods.do_click(driver, css_sl.sliders_arrowL)

    tour_switcher = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.tour_switcher)
    )
    assert tour_switcher.is_enabled(), "Смена туров не активна либо не кликабельна"
    methods.do_click(driver, css_sl.tour_switcher)

    WebDriverWait(driver, 5)

    next_arrow = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.slider_arrow)
    )
    assert next_arrow.is_displayed(), "Навигационная стрелка отсутствует"
    for i in range(3):
        methods.do_click(driver, next_arrow)

    order_tour = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(css_sl.tour_order)
    )
    assert order_tour.is_displayed(), "Навигационная ссылка заказать тур отсутствует"


@pytest.mark.sanity()
def test_sliders_article(driver):
    driver.get(configuration.URL)
    driver.execute_script('window.scrollBy(0, 1175)')
    time.sleep(3)

    displayed_arrow = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.slider_arrow3)
    )
    assert displayed_arrow.is_displayed(), "Стрелка не активна"
    for i in range(3):
        time.sleep(1)
        displayed_arrow.click()

    WebDriverWait(driver, 5)
    displayed_arrow_back = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.slider_arrow4)
    )
    assert displayed_arrow_back.is_displayed(), "Стрелка не активна"
    for i in range(3):
        time.sleep(1)
        displayed_arrow_back.click()

    country_container = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.country_container)
    )
    assert country_container.is_enabled(), "Контейнер не активный"
    methods.do_click(driver, css_sl.country_container)
    try:
        driver.execute_script("window.scrollBy(0,325)")
        time.sleep(3)
        action = ActionChains(driver)
        enter_pressed = False
        while True:
            action.send_keys(Keys.DOWN).perform()
            time.sleep(0.5)
            if not country_container.is_displayed():
                break
            if random.randint(1, 10) == 4:
                time.sleep(random.uniform(0.5, 2.0))
                action.send_keys(Keys.ENTER).perform()
                enter_pressed = True
                break
        if enter_pressed:
            country_container.send_keys(Keys.ESCAPE)
    except:
        city_container = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(css_sl.city_container)
        )
        assert city_container.is_displayed(), "Выпадающий список не активный"
        methods.do_click(driver, css_sl.city_container)
        try:
            action = ActionChains(driver)
            enter_pressed = False
            while True:
                action.send_keys(Keys.DOWN).perform()
                time.sleep(0.5)
                if not city_container.is_displayed():
                    break
                if random.randint(1, 5) == 2:
                    time.sleep(random.uniform(0.5, 2.0))
                    action.send_keys(Keys.ENTER).perform()
                    enter_pressed = True
                    break
            if enter_pressed:
                city_container.send_keys(Keys.ESCAPE)
        except:
            theme_container = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(css_sl.theme_container)
            )
            assert theme_container.is_displayed(), "Контейнер 'Темы' не активна"
            methods.do_click(driver, css_sl.theme_container)
            action = ActionChains(driver)
            enter_pressed = False
            while True:
                action.send_keys(Keys.DOWN).perform()
                time.sleep(0.5)
                if not theme_container.is_displayed():
                    break
                if random.randint(1, 5) == 2:
                    time.sleep(random.uniform(0.5, 2.0))
                    action.send_keys(Keys.ENTER)
                    enter_pressed = True
                    break
            if enter_pressed:
                driver.execute_script("window.stop()")
            else:
                methods.assert_text_visible(driver, css_sl.link_text)
                submit_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable(css_sl.submit_button)
                )
                assert submit_button.is_displayed() \
                       and submit_button.is_enabled(), "Кнопка не активна либо нек кликабельна"
                methods.do_click(driver, css_sl.submit_button)


@pytest.mark.sanity()
def test_sliders_attractions(driver):
    driver.get(configuration.URL)
    driver.execute_script("window.scrollBy(0,1750)")

    slider_next = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.slider_next)
    )
    assert slider_next.is_displayed(), "Навигационная стрелка не активна"
    for i in range(3):
        time.sleep(1)
        slider_next.click()

    slider_prev = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.slider_prev)
    )
    assert slider_prev.is_displayed(),\
        "Навигационная стрелка достопримечательностей отсутствует"
    for i in range(3):
        time.sleep(1)
        slider_prev.click()

    attractions_link = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(css_sl.attractions_link)
    )
    assert attractions_link.is_enabled(),\
        "Навигационная ссылка 'Все достопримечательности'не доступна"


@pytest.mark.sanity()
def test_slider_hotel(driver):
    driver.get(configuration.URL)

    driver.execute_script("window.scrollBy(0,2150)")
    hotel_arrow_next = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.hotel_slider_next)
    )
    assert hotel_arrow_next.is_displayed(), "Навигационная стрелка отсутствует"
    for i in range(5):
        time.sleep(1)
        hotel_arrow_next.click()

    hotel_arrow_prev = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.hotel_slider_prev)
    )
    assert hotel_arrow_prev.is_displayed(), "Навигационная стрелка отсутствует"
    for i in range(5):
        time.sleep(1)
        hotel_arrow_prev.click()
    else:
        hotel_link = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(css_sl.hotel_link_text)
        )
        assert hotel_link.is_displayed()\
               and hotel_link.is_enabled(), "Навигационная ссылка отсутствует или не кликабельна"


@pytest.mark.sanity()
def test_slider_train(driver):
    driver.get(configuration.URL)
    driver.execute_script("window.scrollBy(0,2550)")

    slider_train_next = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.slider_train_next)
    )
    assert slider_train_next.is_displayed(), "Test might be fallen"
    for i in range(5):
        time.sleep(1)
        slider_train_next.click()

    slider_train_prev = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.slider_train_prev)
    )
    assert slider_train_prev.is_displayed()\
           and slider_train_prev.is_enabled(), "Навигационная стрелка отсутствует"
    for i in range(5):
        time.sleep(1)
        slider_train_prev.click()
    else:
        train_link = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(css_sl.train_link_text)
        )
        assert train_link.is_displayed(),"Навигационная ссылка не активна"


@pytest.mark.sanity()
def test_slider_train(driver):
    driver.get(configuration.URL)
    driver.execute_script("window.scrollBy(0,3525)")

    news = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.news)
    )
    assert news.is_displayed(), "один из элементов блока 'новости' не активный"
    news1 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.news1)
    )
    assert news1.is_displayed(), "один из элементов блока 'новости' не активный"

    news2 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.news2)
    )
    assert news2.is_displayed(), "один из элементов блока 'новости' не активный"
    news3 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.news3)
    )
    assert news3.is_displayed(), "один из элементов блока 'новости' не активный"

    news4 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.news4)
    )
    assert news4.is_displayed(), "один из элементов блока 'новости' не активный"

    news_link_text = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(css_sl.news_link_text)
    )
    assert news_link_text.is_displayed(), "Навигационная ссылка не активна"

    photo1 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.photo1)
    )
    assert photo1.is_displayed(), "один из элементов блока 'новости' не активный"

    photo2 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.photo2)
    )
    assert photo2.is_displayed(), "один из элементов блока 'новости' не активный"

    photo3 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.photo3)
    )
    assert photo3.is_displayed(), "один из элементов блока 'новости' не активный"

    photo_link_text = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(css_sl.news_link_text)
    )
    assert photo_link_text.is_displayed(), "Навигационная ссылка не активна"

    koleydoskop1 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.koleydoskop1)
    )
    assert koleydoskop1.is_displayed(), "один из элементов блока 'новости' не активный"

    koleydoskop2 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.koleydoskop2)
    )
    assert koleydoskop2.is_displayed(), "один из элементов блока 'новости' не активный"

    koleydoskop3 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.koleydoskop3)
    )
    assert koleydoskop3.is_displayed(), "один из элементов блока 'новости' не активный"

    koleydoskop_link_text = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(css_sl.koleydoskop_link_text)
    )
    assert koleydoskop_link_text.is_displayed(), "Навигационная ссылка не активна"


@pytest.mark.sanity()
def test_slider_train(driver):
    driver.get(configuration.URL)
    driver.execute_script("window.scrollBy(0,3975)")

    other_delay_avia = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.other_delay_avia)
    )
    other_delay_avia.is_displayed(), "Услуга авиа-перелёты не активна"

    other_delay_attract = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.other_delay_attract)
    )
    other_delay_attract.is_displayed(), "Услуга авиа-перелёты не активна"

    other_delay_insurance = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.other_delay_insurance)
    )
    other_delay_insurance.is_displayed(), "Услуга авиа-перелёты не активна"

    other_delay_transfer = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.other_delay_transfer)
    )
    other_delay_transfer.is_displayed(), "Услуга авиа-перелёты не активна"

    other_delay_bus = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.other_delay_bus)
    )
    other_delay_bus.is_displayed(), "Услуга авиа-перелёты не активна"

    other_delay_rent = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(css_sl.other_delay_rent)
    )
    other_delay_rent.is_displayed(), "Услуга авиа-перелёты не активна"


@pytest.mark.sanity()
def test_slider_train(driver):
    driver.get(configuration.URL)
    driver.execute_script("window.scrollBy(0,4475)")

    comment_arrow = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.comment_arrowR)

    )
    assert comment_arrow.is_enabled(), "Шапка комментария не видна"
    for i in range(3):
        time.sleep(1)
        comment_arrow.click()

    comment_arrowL = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.comment_arrowL)
    )
    assert comment_arrowL.is_displayed(), "Навигационная стрелка не активна"
    for i in range(3):
        time.sleep(1)
        comment_arrowL.click()

    submit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(css_sl.comment_button)
    )
    assert submit_button.is_enabled()\
           and submit_button.is_displayed(), "Кнопка не активна либо не кликабльна"
    methods.do_click(driver, css_sl.comment_button)











