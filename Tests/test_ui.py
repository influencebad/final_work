from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
import allure
from selenium import webdriver
from Pages.mainpage import MainPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


@allure.title('Поиск наличия трейлера')
def test_find_trailer(browser: WebDriver):
    main_page = MainPage(browser)
    with allure.step('Нажать кнопку смотреть'):
        main_page.click_watch_movie('//span[text() = "Смотреть"]')
    with allure.step("Найти на странице кнопку ТРЕЙЛЕР"):
        result = main_page.find_trailer('//button[text() = "Трейлер"]')
    with allure.step("Проверить, что кнопка имеет название Трейлер"):
        assert result == 'Трейлер'


@allure.title('Найти расширенный поиск')
def test_find_advanced_search(browser: WebDriver):
    main_page = MainPage(browser)
    with allure.step('Нажать кнопку РАСШИРЕННЫЫЙ ФИЛЬТР'):
        main_page.click_advanced_search('//a[contains(@aria-label, "Расширенный поиск")]')
    with allure.step('Проверить что открылась страница РАСШИРЕННЫЙ ПОИСК'):
        result = main_page.find_advanced_search('//span[text() = "Расширенный поиск"]')
        assert result == 'Расширенный поиск'


@allure.title('Найти просмотр ТВ')
def test_tv_search(browser: WebDriver):
    main_page = MainPage(browser)
    with allure.step('Нажать кнопку ТЕЛЕКАНАЛЫ'):
        main_page.watch_tv('//div[contains(@class, "sidebarContainer")]//a[normalize-space(text())="Телеканалы"]')
    with allure.step('Проверить что открылась страница СМОТРЕТЬ КАНАЛЫ'):
        result = main_page.check_tv('//h1[text() = "Смотреть каналы"]')
        assert result == 'Смотреть каналы'


@allure.title('Поиск фильма по названию')
def test_find_film(browser: WebDriver):
    main_page = MainPage(browser)
    with allure.step('Найти поле для поиска фильмов и ввести название'):
         main_page.input_name_film('//input[@name="kp_query"]', "Челюсти")
    with allure.step('Нажать кнопку поиск'):
        main_page.click_find('//button[contains(@aria-label, "Найти") and contains (@class, "styles_root")]')
    with allure.step('Проверить , что первый найденный фильм имеет искомое название'):
        result = main_page.check_finds('//a[text() = "Челюсти"]')
        assert result == 'Челюсти'


@allure.title('Проверка работы раздела билеты')
def test_find_movie_tickets(browser: WebDriver):
    main_page = MainPage(browser)
    with allure.step('Нажать кнопку БИЛЕТЫ В КИНО'):
        main_page.movie_tickets('//div[contains(@class, "styles_sticky__mDnbt")]//a[normalize-space(text())="Билеты в кино"]')
    with allure.step('Проверить что открылась страница Билеты в кино'):
        result = main_page.check_movie_tickets('//h1[text() = "Билеты в кино"]')
        assert result == 'Билеты в кино'
