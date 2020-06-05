from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.reddit.com/r/babyYoda').text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())



