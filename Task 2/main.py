import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.shadowfox.in/")

web = BeautifulSoup(url.content,"html.parser")

web.prettify()

print(web.title)
print(web.title.name)
print(web.a)
print(web.p)
print(web.h1)