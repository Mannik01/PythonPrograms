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

            word_list.append(each_word)
    clean_a_list(word_list)

# function to sort out only words
def clean_a_list(word_list):
    clean_words_list = []
    for words in word_list:
        symbols = "!@#$%^&*()_-+={[}]|:;/<,>.?/"
        for k in range(0, len(symbols)):
            words = words.replace(symbols[k], "")
        if len(words) > 0:
            print(words)
            clean_words_list.append(words)

begin("https://www.thenewboston.com/forum/category.php?id=10") # starts the process of word counting from the website in the parenthesis
