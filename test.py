import requests
from bs4 import BeautifulSoup
import re

url = 'https://ridibooks.com/category/bestsellers/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

class_regex = re.compile(r'fig-rs\d+')
elements = soup.select('a[class*="fig-rs"]')
for no, element in enumerate(elements, 1):
    if element.name == 'a':
        print(no, element.text.strip())
