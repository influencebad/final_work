from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.kinopoisk.ru')

    def click_watch_movie(self, element):
        """
            эта функция ищет кнопку СМОТРЕТЬ и нажимает ее
        """
        self.driver.find_element(By.XPATH, element).click()

    def find_trailer(self, element):
        """
            эта функция ищет кнопку ТРЕЙЛЕР, и возвращает текст кнопки
        """
        return self.driver.find_element(By.XPATH, element).text

    def click_advanced_search(self, element):
        """
            эта функция ищет кнопку РАСШИРЕННЫЙ ПОИСК, и нажимает ее
        """
        self.driver.find_element(By.XPATH, element).click()

    def find_advanced_search(self, element):
        """
            эта функция находит заголовок страницы и возвращает ее название
        """
        return self.driver.find_element(By.XPATH, element).text

    def watch_tv(self, element):
        """
            эта функция находит кнопку смотреть ТВ  и нажимает ее
        """
        self.driver.find_element(By.XPATH, element).click()

    def check_tv(self, element):
        """
            эта функция находит заголовок страницы и возвращает ее название
        """
        return self.driver.find_element(By.XPATH, element).text

    def input_name_film(self, element, value):
        """
            эта функция находит поисковую строку и вводит в нее название искомого фильма
        """
        self.driver.find_element(By.XPATH, element).send_keys(value)

    def click_find(self, element):
        """
            эта функция находит кнопку найти фильм и нажимает ее
        """
        self.driver.find_element(By.XPATH, element).click()

    def check_finds(self, element):
        """
            эта функция находит название первого найденного на странице фильма и возвращвет его название
        """
        return self.driver.find_element(By.XPATH, element).text

    def movie_tickets(self, element):
        """
            эта функция находит кнопку БИЛЕТЫ В КИНО  и нажимает ее
        """
        self.driver.find_element(By.XPATH, element).click()

    def check_movie_tickets(self, element):
        """
            эта функция находит заголовок страницы и возвращает ее название
        """
        return self.driver.find_element(By.XPATH, element).text
