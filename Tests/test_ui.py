from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
from selenium import webdriver
from Pages.mainpage import MainPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(8)
    yield driver
    driver.quit()


def test_to_watch_trailer(browser: WebDriver):

    main_page = MainPage(browser)

    main_page.click_capcha('.CheckboxCaptcha-Checkbox')

    main_page.click_pop_up('.styles_closeIcon__Zvc5W')

    main_page.click_watch_movie()

    main_page.click_watch_trailer('Trailer')

    assert main_page.waiting_element(browser, "//div[contains(@class, 'styles_bufferedRangesBar__y1jyY')]")
