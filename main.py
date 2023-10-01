import requests
from bs4 import BeautifulSoup
import json



url = 'https://quotes.toscrape.com/'
response = requests.get(url) 
soup = BeautifulSoup(response.text,"lxml")
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
some_data = dict()
for i in range(len(quotes)):
    some_data[authors[i].text] = quotes[i].text
print(some_data)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(some_data, file)
    

    #print(quotes[i].text)
    #print(authors[i].text)