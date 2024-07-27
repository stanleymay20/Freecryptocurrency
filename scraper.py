import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_coinlaunch():
    url = "https://coinlaunch.io/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    offers = []
    for item in soup.find_all('div', class_='giveaway'):
        title = item.find('h2').text if item.find('h2') else "No title"
        link = item.find('a', href=True)['href'] if item.find('a', href=True) else "#"
        offers.append({'title': title, 'link': link, 'source': 'CoinLaunch'})
    return offers

def scrape_cryptonews():
    url = "https://cryptonews.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    offers = []
    for item in soup.find_all('div', class_='giveaway'):
        title = item.find('h2').text if item.find('h2') else "No title"
        link = item.find('a', href=True)['href'] if item.find('a', href=True) else "#"
        offers.append({'title': title, 'link': link, 'source': 'CryptoNews'})
    return offers

def scrape_coinmarketcap():
    url = "https://coinmarketcap.com/airdrops/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    offers = []
    for item in soup.find_all('div', class_='content'):
        title = item.find('h2').text if item.find('h2') else "No title"
        link = item.find('a', href=True)['href'] if item.find('a', href=True) else "#"
        offers.append({'title': title, 'link': link, 'source': 'CoinMarketCap'})
    return offers

def scrape_airdropalert():
    url = "https://airdropalert.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    offers = []
    for item in soup.find_all('div', class_='airdrop'):
        title = item.find('h3').text if item.find('h3') else "No title"
        link = item.find('a', href=True)['href'] if item.find('a', href=True) else "#"
        offers.append({'title': title, 'link': link, 'source': 'AirdropAlert'})
    return offers

def scrape_airdropsio():
    url = "https://airdrops.io/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    offers = []
    for item in soup.find_all('div', class_='airdrops'):
        title = item.find('h2').text if item.find('h2') else "No title"
        link = item.find('a', href=True)['href'] if item.find('a', href=True) else "#"
        offers.append({'title': title, 'link': link, 'source': 'Airdrops.io'})
    return offers

def scrape_coingecko():
    url = "https://www.coingecko.com/en/airdrops"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    offers = []
    for item in soup.find_all('div', class_='card-body'):
        title = item.find('h5').text if item.find('h5') else "No title"
        link = item.find('a', href=True)['href'] if item.find('a', href=True) else "#"
        offers.append({'title': title, 'link': link, 'source': 'CoinGecko'})
    return offers

def scrape_all():
    all_offers = []
    all_offers.extend(scrape_coinlaunch())
    all_offers.extend(scrape_cryptonews())
    all_offers.extend(scrape_coinmarketcap())
    all_offers.extend(scrape_airdropalert())
    all_offers.extend(scrape_airdropsio())
    all_offers.extend(scrape_coingecko())
    return pd.DataFrame(all_offers)

if __name__ == "__main__":
    df = scrape_all()
    df.to_csv('crypto_giveaways.csv', index=False)
