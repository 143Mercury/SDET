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
        EC.element_to_be_clickable(css_sl. click_on_calendar)
    )
    methods.do_double_click(driver, css_sl.click_on_calendar)
    assert calendar_icon.is_enabled(), "Календарь не открылся"
    methods.do_click(driver, css_sl.pick_the_data)
    calendar_icon2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(css_sl.click_on_calendar2)
    )
    methods.do_click(driver, css_sl.click_on_calendar2)
    assert calendar_icon2.is_enabled(), "Календарь-2 не открылся "
    methods.do_click(driver, css_sl. pick_the_data2)

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
    methods.do_click(driver, css_sl. chose_option)
    assert choose_option.is_enabled() \
           and choose_option.is_displayed(), "Кнопка смены опции вида тура не доступна и не встроена "
    where = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(css_sl.where)
    )
    methods.do_send_keys(driver, css_sl. where, "Москва")
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
    methods.do_click(driver, css_sl. hotel_dropdown)
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
        EC.visibility_of_element_located(css_sl. add_kids)
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
    assert train_sign.is_enabled()\
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
    assert submit_button.is_displayed()\
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
    driver.implicitly_wait(3)

    slider = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(css_sl.sliders1)
    )
    assert slider.is_displayed(), "Один из элементов слайдера не активный"
