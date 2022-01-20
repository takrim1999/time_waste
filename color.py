#!/usr/bin/python3
import re
import requests
from bs4 import BeautifulSoup as BS
import lxml
result = requests.get("https://simple.wikipedia.org/wiki/Web_color").content
soup = BS(result,"lxml")
for i in soup.find_all('tr'):
    if len(i.text.split()[-1].split()) == 3:
        print(i.text)