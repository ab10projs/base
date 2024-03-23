import requests
from bs4 import BeautifulSoup


page = requests.get(r'https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_31082023.csv')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)