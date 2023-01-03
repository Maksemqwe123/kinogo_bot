import time
import requests
from bs4 import BeautifulSoup


start_time = time.time()

items = []
urls = []
spend = []


class Parser:
    def __init__(self, pages: range):
        self.pages = pages
        self.items = items
        self.urls = urls

        self._get_html()

    def _get_html(self):
        for page in self.pages:
            if page == 1:
                url = 'https://kinogo.film/films-2021/'
            else:
                url = f'https://kinogo.film/films-2021/page/{page}/'

            response = requests.get(url=url)

            try:
                assert response.status_code == 200
                html_source = response.text
                self._get_info(html_source)
            except AssertionError as e:
                print(f'ERROR: {repr(e)}')
                print(response.status_code)

    def _get_info(self, html_source):
        pages_info = BeautifulSoup(html_source, 'html.parser')

        films_names = pages_info.find_all('h2', class_='zagolovki')
        for name in films_names:
            self.items.append(name.text)
            films_urls_kinogo = name.find('a').get('href')
            self.urls.append(films_urls_kinogo)


parse = Parser(range(1, 10))
all_info = list(zip(items, urls))
for i in all_info:
    list_kinogo = f'Название: {i[0].strip()} \nСсылка: {i[1]}'
    spend.append(list_kinogo)
    # end_time = time.time() - start_time
    # print(f'\nВремя работы: {end_time} секунд')
