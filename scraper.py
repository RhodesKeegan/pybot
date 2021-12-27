from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        self.url = 'https://www.gamestop.com/products/microsoft-xbox-series-x/224744.html'

    def check_availability(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        button = soup.find(id='add-to-cart-buttons')
        return button.get_text()