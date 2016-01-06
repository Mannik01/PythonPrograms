import requests
from bs4 import BeautifulSoup
import operator

def begin(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.findAll('a', {'class': 'title text-semibold'}):
        content = post_text.text
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)


begin("https://www.thenewboston.com/forum/category.php?id=10")
