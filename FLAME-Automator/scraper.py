import requests
from bs4 import BeautifulSoup
import schedule
import time

def scrape_quotes():
    # URL of the page we want to scrape
    url = 'http://quotes.toscrape.com'

    # Send a request to get the content of the page
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all quotes on the page
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    # Print the quotes and authors
    for i in range(len(quotes)):
        print(f'Quote: {quotes[i].text}')
        print(f'Author: {authors[i].text}')
        print('---')

# Schedule the scraper to run every 10 seconds
schedule.every(10).seconds.do(scrape_quotes)

while True:
    schedule.run_pending()
    time.sleep(1)

