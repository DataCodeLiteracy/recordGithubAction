import requests
from bs4 import BeautifulSoup
import re

url = 'https://ridibooks.com/category/bestsellers/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

class_regex = re.compile(r'fig-rs\d+')
elements = soup.select('div[class*="fig-"], a[class*="fig-rs"]')
for no, element in enumerate(elements, 1):
    if element.name == 'a':
        class_name = ' '.join(class_regex.findall(' '.join(element.get('class'))))
        print(no, element.text.strip(), class_name)
