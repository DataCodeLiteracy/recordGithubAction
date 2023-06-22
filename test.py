import requests
from bs4 import BeautifulSoup
import re

url = 'https://ridibooks.com/category/bestsellers/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

class_regex = re.compile(r'fig-\d+')
bookservices = soup.select('[class*="fig-"]')
for no, book in enumerate(bookservices, 1):
    class_name = ' '.join(class_regex.findall(' '.join(book.get('class'))))
    print(no, book.text.strip(), class_name)
