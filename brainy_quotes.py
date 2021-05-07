import requests
from bs4 import BeautifulSoup as bs
import re

# url of the website content to be scraped
URL = "https://www.brainyquote.com/quote_of_the_day"

resp = requests.get(URL)
soup = bs(resp.content, features='html.parser')

quotes = [re.sub('\n+','', item.get_text()) for item in soup.find_all('a', class_='oncl_q') if len(item.get_text()) > 2]
authors = [item.get_text() for item in soup.find_all('a', class_='oncl_a')]
quote_type = [item.get_text() for item in soup.find_all('h2', class_='qotd-h2')]
quote_type.insert(0, soup.find('div', class_='qotdSubtInf').get_text().strip('\n')) # insert at start 'date'
# find all tag containers, get text while removing first '\n' chars and replacing subsequent '\n' with commas.
tags = [re.sub('[\W+]', ',', item.get_text().strip('\n')) for item in soup.find_all('div', class_='kw-box')]

# get today's birthdays
birthdays = [item.get_text() for item in soup.find_all('div', class_='boxy boxyPaddingBig')]

print('~'*100)
print("YOUR QUOTES OF THE DAY:\n")
for i, quote in enumerate(quotes):
	print(i+1, "{}: '{}' - {} [{}]".format(quote_type[i], quote, authors[i], tags[i]))
print('-'*100)
for b in birthdays:
	print(b)
print('_'*100)