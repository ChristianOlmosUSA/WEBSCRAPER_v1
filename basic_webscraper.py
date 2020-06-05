import requests
from bs4 import BeautifulSoup
import urllib.request

url = "http://reddit.com/r/babyYoda"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

#print a.prettify()
#print a.title.string
images = soup.findAll("img", attrs = {"alt": "Post image"})

number = 0

for image in images:
    image_src = image["src"]
    print(image_src)
    urllib.request.ulretrieve(image_src, str(number))
    number +=1
    
    ## This didnt bloody work, just saved for reference. https://www.youtube.com/watch?v=RkaHdOje-cI