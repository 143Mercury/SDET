from selenium.webdriver.common.by import By

city_dropdown = (By.ID, "s-query")
city_dropdown_item = (By.CSS_SELECTOR, '[id="search-results-rutours"]')

form_attractions = (By.XPATH, '/html/body/section[2]/div/div[1]/form[2]/div[2]/input[1]')
attractions_checkbox = (By.CSS_SELECTOR, '[class="search__item second typelist"]')

type_attractions = (By.XPATH, '/html/body/section[3]/div/div/form/div[1]/label')

click_on_calendar = (By.XPATH, '/html/body/section[2]/div/div[1]/form[2]/div[3]/input')

pick_the_data = (By.XPATH,  '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[2]')

click_on_calendar2 = (By.ID, 's-dateto')

pick_the_data2 = (By.CSS_SELECTOR, '[data-title="Выберите дату выезда"]')

displayed_button = (By.XPATH, '/html/body/section[2]/div/div[1]/form[2]/input')

chose_option = (By.CSS_SELECTOR, '[class="block-btns__btn world-tours"]')

where = (By.CSS_SELECTOR, '[placeholder="Куда едете?"]')
list_destinations = (By.XPATH, '//*[@id="search-results-tours"]/ul')

city = (By.CSS_SELECTOR, '[placeholder="Откуда вылет"]')
departure_items = (By.CSS_SELECTOR, '[class="item departure-cities__item"]')
remove_arguments = (By.CSS_SELECTOR, '[value="Москва"]')

calendar_checkin = (By.CSS_SELECTOR, '[placeholder="Дата"]')
next_arrow = (By.CSS_SELECTOR, '[data-handler="next"]')

choose_date = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[3]/a')

dropdown_select = (By.CSS_SELECTOR, '[class="set-nights__number"]')
dropdown_select_from = (By.CSS_SELECTOR, '[class="input-plus-t input-change input-plus-first"]')
dropdown_select_to = (By.CSS_SELECTOR, '[class="input-plus-t input-change input-plus-second"]')

dropdown_select_tourist = (By.CSS_SELECTOR, '[class="dropdown__btn hotels-search__item  br-left"]')
dropdown_select_by = (By.CSS_SELECTOR, '[class="input-plus input-plus_adults"]')
dropdown_select_by_child = (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[2]/div[2]')

button_submitTours = (By.XPATH, '//*[@id="tours-search-form"]/button')

hotel_sign = (By.XPATH, '/html/body/div[2]/div/div[2]')
hotel_form = (By.CSS_SELECTOR, '[style="border-left: none"]')

hotel_checkin = (By.XPATH, '//*[@id="h-checkin"]')
hotel_data = (By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[3]/td[2]')
hotel_checkout = (By.CSS_SELECTOR, "h-checkout")
hotel_data2 = (By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[5]/td[6]')

hotel_dropdown = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[1]')
add_guests = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[2]/div[1]/div/span[2]')
dropdown_kids_option = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[2]/div[2]/div[1]')
add_kids = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[2]/div[2]/div[2]/div/span[4]')

hotel_submit = (By.XPATH, '//*[@id="reservation-form"]/input[4]')

train_sign = (By.XPATH, '/html/body/div[2]/div/div[3]')

train_form_first = (By.CSS_SELECTOR, '[class="search__item first_tickets"]')
list_station = (By.XPATH, '//*[@id="search-form_tickets"]/div[1]/div/ul')
train_form_second = (By.CSS_SELECTOR, '[class="search__item second_tickets"]')
list_station2 = (By.CSS_SELECTOR, '[class="list station__list dropdown open"]')

train_calendar = (By.XPATH, '//*[@id="t-datefrom"]')
calendar_date = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[7]')

date_arrow = (By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]')
calendar_date2 = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[2]/a')


train_submit = (By.XPATH, '//*[@id="search-form_tickets"]/button')

routs_sign = (By.XPATH, '/html/body/div[2]/div/div[4]')
routs_form = (By.XPATH, '/html/body/section[2]/div/div[4]/form/div[1]/input')
routs_destinations1 = (By.XPATH, '/html/body/section[2]/div/div[4]/form/div[1]/div/ul')
routs_form2 = (By.CSS_SELECTOR, '[class="search__item second_auto"]')
routs_destinations2 = (By.XPATH, '/html/body/section[2]/div/div[4]/form/div[2]/div/ul')

routs_submit = (By.XPATH, '/html/body/section[2]/div/div[4]/form/button')

city_country_sign = (By.XPATH, '/html/body/div[2]/div/div[5]')

dropdown_country = (By.CSS_SELECTOR, '[title="Выбрать страну"]')

dropdown_city = (By.XPATH, '//*[@id="select2-search-city-container"]')

c_c_submit = (By.XPATH, '/html/body/section[2]/div/div[5]/form/button')

tours = (By.LINK_TEXT, "Туры")
hotels = (By.LINK_TEXT, "Отели")
trains = (By.LINK_TEXT, "ЖД Билеты")
routs = (By.LINK_TEXT, "Маршруты")
attractions = (By.LINK_TEXT, "Достопримечательности")

adigay = (By.CSS_SELECTOR, '[alt="в Адыгею"]')
baikal = (By.CSS_SELECTOR, '[alt="на Байкал"]')
dagestan = (By.CSS_SELECTOR, '[alt="в Дагестан"]')

slider_container = (By.XPATH, '/html/body/section[5]/div')
slider4 = (By.CSS_SELECTOR, '[alt="в Карелию"]')
slider5 = (By.CSS_SELECTOR, '[alt="на Кавказ"]')
slider6 = (By.CSS_SELECTOR, '[alt="в Сочи"]')
sliders_arrowR = (By.XPATH, '/html/body/section[5]/div/div/div/div[1]/div[3]')
sliders_arrowL = (By.XPATH, '/html/body/section[5]/div/div/div/div[1]/div[2]')
slider_arrow = (By.XPATH, '/html/body/section[5]/div/div/div/div[2]/div[3]')
tour_switcher = (By.CSS_SELECTOR, '[class="tours__switcher"]')

egypt = (By.LINK_TEXT, 'в Египет')
spain = (By.CSS_SELECTOR, 'alt="в Испанию"')
italy = (By.CSS_SELECTOR, 'alt="в Италию"')
tour_order = (By.XPATH, '/html/body/section[5]/div/div/div/div[5]/a/span')

slider_arrow3 = (By.CSS_SELECTOR, '[class="swiper-button-next articles__slider_next"]')
slider_arrow4 = (By.CSS_SELECTOR, '[class="swiper-button-prev articles__slider_prev"]')

country_container = (By.ID, 'select2-country-container')
city_container = (By.ID,  'select2-city-container')
theme_container = (By.ID, 'select2-theme-container')

submit_button = (By.CSS_SELECTOR, '[class="articles__search-btn"]')
link_text = (By.CSS_SELECTOR, 'class="articles__order"')

slider_next = (By.CSS_SELECTOR, '[class="swiper-button-next places__slider_next"]')
slider_prev = (By.CSS_SELECTOR, '[class="swiper-button-prev places__slider_prev"]')
attractions_link = (By.XPATH, '/html/body/section[7]/div/div[2]/a/span')

praga = (By.CSS_SELECTOR, '[alt="Отели в Венеции"]')
hotel_slider_next = (By.CSS_SELECTOR, '[class="swiper-button-next hotels__slider_next"]')
hotel_slider_prev = (By.CSS_SELECTOR, '[class="swiper-button-prev hotels__slider_prev"]')
hotel_link_text = (By.XPATH, '/html/body/section[8]/div/div/div/div[2]/a/span')

slider_train_prev = (By.CSS_SELECTOR, '[class="swiper-button-prev tickets__slider_prev"]')
slider_train_next = (By.CSS_SELECTOR, '[class="swiper-button-next tickets__slider_next"]')
train_link_text = (By.XPATH, '/html/body/section[9]/div/div/div/div[2]/a/span')

news = (By.CSS_SELECTOR, '[alt="«Аэрофлот» в 6 раз увеличит количество рейсов на линии Москва – Анталья"]')
news1 = (By.XPATH, '/html/body/article/div/section[1]/div[1]/div[1]/h4/a')
news2 = (By.XPATH, '/html/body/article/div/section[1]/div[1]/div[3]/h4/a')
news3 = (By.XPATH, '/html/body/article/div/section[1]/div[1]/div[4]/h4/a')
news4 = (By.CSS_SELECTOR, '[alt="В Казахстане среди туристов вновь лидируют россияне"]')
news_link_text = (By.XPATH, '/html/body/article/div/section[1]/div[2]/a/span')
photo1 = (By.XPATH, '/html/body/article/div/section[2]/div[1]/div[1]/a/picture/img')
photo2 = (By.XPATH, '/html/body/article/div/section[2]/div[1]/div[2]/a/picture/img')
photo3 = (By.XPATH, '/html/body/article/div/section[2]/div[1]/div[3]/a/picture/img')
photo_link_text = (By.XPATH, '/html/body/article/div/section[2]/div[3]/a/span')
koleydoskop1 = (By.XPATH, '/html/body/article/div/section[3]/div[1]/div[1]/a/picture/img')
koleydoskop2 = (By.XPATH, '/html/body/article/div/section[3]/div[1]/div[2]/a/picture/img')
koleydoskop3 = (By.XPATH, '/html/body/article/div/section[3]/div[1]/div[3]/a/picture/img')
koleydoskop_link_text = (By.XPATH, '/html/body/article/div/section[3]/div[3]/a/span')

other_delay_avia = (By.CSS_SELECTOR, '[alt="Авиабилеты"]')
other_delay_attract = (By.CSS_SELECTOR, '[alt="Экскурсии"]')
other_delay_insurance = (By.CSS_SELECTOR, '[alt="Страховки"]')
other_delay_transfer = (By.CSS_SELECTOR, '[alt="Трансферы"]')
other_delay_bus = (By.CSS_SELECTOR, '[alt="Автобусы"]')
other_delay_rent = (By.CSS_SELECTOR, '[alt="Аренда авто"]')

review_head1 = (By.XPATH, '//*[@id="swiper-wrapper-9e4bb355ed3a8d5e"]/div[7]/div[1]')
review_head2 = (By.XPATH, '//*[@id="swiper-wrapper-9e4bb355ed3a8d5e"]/div[6]/div[1]')
review_head3 = (By.XPATH, '//*[@id="swiper-wrapper-9e4bb355ed3a8d5e"]/div[5]/div[1]')
comment_arrowR = (By.CSS_SELECTOR, '[class="swiper-button-next reviews__slider_next"]')
comment_arrowL = (By.CSS_SELECTOR, '[class="swiper-button-prev reviews__slider_prev"]')

comment_button = (By.CSS_SELECTOR, '[class="reviews__btn"]')

