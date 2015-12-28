# make sure to install the modules if not present

import requests  
from bs4 import BeautifulSoup

# Function that takes in number of pages to crawl as parameter and collects the titles and links to the respective titles
def trade_spyder(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://codecanyon.net/search?date=&page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.findAll('a', {'class': 'js-google-analytics__list-event-trigger t-link -color-inherit -decoration-reversed'}):
            href = "http://codecanyon.net" + link.get('href')  # gets the link and stores to 'href'
            title = link.string # gets the title of the items corresponding to the links and stores in 'title'
            print(href)
            print(title)

        page += 1  # updates page number

trade_spyder(1)



