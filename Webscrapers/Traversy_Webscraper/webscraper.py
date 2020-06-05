from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.reddit.com/r/babyYoda').text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

## https://www.youtube.com/watch?v=ng2o98k983k&t=187s   21.29 first commit.


