from bs4 import BeautifulSoup
import requests

def scrape_quots(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content,'html.parser')

    quotes =[]

    for quote_element in soup.find_all('blockquote'):
        quote_text = quote_element.find('q').text.strip()
        quote_author = quote_element.find('a',class_='authorname').text.strip()
        quotes.append(f'"{quote_text}" - {quote_author}')

    return quotes


url='https://www.famousquotes123.com/public-quotes.html'
quotes=scrape_quots(url)

for quote in quotes:
    print(quote)