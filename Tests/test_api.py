import allure
from Pages.kinopoisk_api import Kinopoisk


api = Kinopoisk("https://api.kinopoisk.dev/v1.4/movie")

headers = {
    "accept": "application/json",
    "X-API-KEY": "97KBPH5-JBC4BVG-J4GF84X-6BG2N7T"
    }


@allure.title('Поиск фильма по названию')
def test_get_movie_by_name():
    with allure.step('Получить список фильмов с названием Jaws'):
        resp = api.get_by_name("Jaws", headers)
        response = resp.json()['docs'][0]['internalNames']
    with allure.step('Проверить, что полученые фильмы имеют искомое название'):
        assert response.count('Jaws')
    with allure.step('Проверить, что статус код = 200'):
        assert resp.status_code == 200


@allure.title('Поиск фильма по году выпуска')
def test_get_movie_by_date():
    with allure.step('Получить список фильмов 2023 года выпуска'):
        resp = api.get_by_date(2023, headers)
        response = resp.json()['docs'][0]['year']
    with allure.step('Проверить, что полученые фильмы имеют 2023 год выпуска'):
        assert response == 2023
    with allure.step('Проверить, что статус код = 200'):
        assert resp.status_code == 200


@allure.title('Поиск фильма по рейтингу кинопоиска')
def test_movie_by_rating():
    with allure.step('Получить список фильмов c рейтингом кинопоиска 7'):
        resp = api.get_by_rating(7, headers)
        response = resp.json()['docs'][0]['rating']['kp']
    with allure.step('Проверить, что полученые фильмы имеют рейтинг кинопоиска 7'):
        assert response == 7
    with allure.step('Проверить, что статус код = 200'):
        assert resp.status_code == 200


@allure.title('Получить список мультфильмов')
def test_movie_by_type():
    with allure.step('Получить список мультфильмов'):
        resp = api.get_by_type("cartoon", headers)
        response = resp.json()['docs'][0]['type']
    with allure.step('Проверить, что получили список мультфильмов'):
        assert response == 'cartoon'
    with allure.step('Проверить, что статус код = 200'):
        assert resp.status_code == 200


@allure.title('Получить список фильмов ТОП-250')
def test_get_list_top_250():
    with allure.step('Получить список фильмов ТОП-250'):
        resp = api.get_list_top_250(headers)
        response = resp.json()['docs']
    with allure.step('Проверить, что получили список из 250 фильмов'):
        assert len(response) == 250
    with allure.step('Проверить, что статус код = 200'):
        assert resp.status_code == 200
