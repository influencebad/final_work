import requests


class Kinopoisk:

    def __init__(self, url) -> None:
        self.url = url

    def get_by_name(self, value, headers):
        """
            эта функция принимает параметры, один из которых название искомого фильма,
            его мы передаем в виде значения(value), так же передаем headers,
            в котором содержится API-KEY
        """
        my_params = {
            'page': '1',
            'limit': '10',
            'query': value
        }
        response = requests.get(self.url+'/search', params=my_params, headers=headers)
        return response

    def get_by_date(self, value, headers):
        """
            эта функция принимает параметры, один из которых год выпуска искомого фильма,
            его мы передаем в виде значения(value), так же передаем headers,
            в котором содержится API-KEY
        """
        params = {
            'page': '1',
            'limit': '10',
            'year': value
        }
        response = requests.get(self.url, params, headers=headers)
        return response

    def get_by_rating(self, value, headers):
        """
            эта функция принимает параметры, один из которых рейтинг кинопоиска,
            который мы передаем в значении value, так же передаем headers,
            в котором содержится API-KEY
        """
        params = {
            'page': '1',
            'limit': '10',
            'rating.kp': value
        }
        response = requests.get(self.url, params, headers=headers)
        return response

    def get_by_type(self, value, headers):
        """
            эта функция принимает параметры, один из которых вид, например мультфильм,
            который мы передаем в значении value, так же передаем headers,
            в котором содержится API-KEY
        """
        params = {
            'page': '1',
            'limit': '10',
            'type': value
        }
        response = requests.get(self.url, params, headers=headers)
        return response

    def get_list_top_250(self, headers):
        """
            эта функция  получает список фильмов ТОП-250, передает headers,
            в котором содержится API-KEY
        """
        params = {
            'limit': 250,
            'lists': 'top250'
        }
        response = requests.get(self.url, params, headers=headers)
        return response
