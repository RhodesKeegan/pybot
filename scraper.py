from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        self.url = 'https://runpee.com/?s='

    def keywords_search_words(self, message):
        words = message.split()[1:]
        keywords = '+'.join(words)
        search_words = ' '.join(words)
        return keywords, search_words

    def search(self, keywords):
        response = requests.get(self.url+keywords, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        result_links = soup.findAll('a')
        return result_links

    def send_link(self, result_links, search_words):
        send_link = set()
        for link in result_links:
            text = link.text.lower()
            if search_words in text:
                send_link.add(link.get('href'))
        return send_link