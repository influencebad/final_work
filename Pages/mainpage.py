from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.kinopoisk.ru')

    def click_capcha(self, element):
        self.driver.find_element(By.CSS_SELECTOR, element).click()

    def click_pop_up(self, element):
        self.driver.find_element(By.CSS_SELECTOR, element).click()

    def click_watch_movie(self, element):
        self.driver.find_element(By.NAME, element).click()

    def click_watch_trailer(self, element):
        self.driver.find_element(By.NAME, element).click()

    def waiting_element(self, driver, element):
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.presence_of_element_located(By.XPATH, element))
