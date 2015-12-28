import requests
from bs4 import BeautifulSoup

def trade_spyder(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://codecanyon.net/search?date=&page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.findAll('a', {'class': 'js-google-analytics__list-event-trigger t-link -color-inherit -decoration-reversed'}):
            href = "http://codecanyon.net" + link.get('href')
            title = link.string
            print(href)
            print(title)

        page += 1

trade_spyder(1)



