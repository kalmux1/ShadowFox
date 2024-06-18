                                # IF ELSE TASK IN Beginner Level
#-------------------------------------------------------------------------------------------------------------------#


import requests                     # Importing Requests Module
from bs4 import BeautifulSoup       # Inporting Beautifulsoup Module

url = requests.get("https://www.shadowfox.in/")         # Storing all the HTML data from the website in url variable
print(url.content)                                      # Displaying all the content of url variable

web = BeautifulSoup(url.content,"html.parser")          # Parsing the raw data using html.parser

print(web.prettify())               # Displaying the formatted data usinng prettify function

# Displaying Website Title
print(web.title)

# Displaying Website Title Name
print(web.title.name)

# Displaying Website Title String
print(web.title.string)

# Displaying Website Link or Anchor Tag
print(web.a)

# Displaying Website First Para tag
print(web.p)

# Displaying Website First Heading Tag
print(web.h1)

# Finding Website First Anchor tag
print(web.find("a"))

# Finding Website All H1 or Heading Tag
print(web.find_all("h1"))

# Finding Website Data Using id attribute 
print(web.find(id= "nav-bar"))