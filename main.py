from bs4 import BeautifulSoup
import requests


l = []

for x in range(10):
    url = 'https://thegeorgiagazette.com/fayette/page/'+f'{x}/'

    # Initiate bs4
    response = requests.get(url)
    result = BeautifulSoup(response.text, 'html.parser')

    inmates = (result.findAll('a'))

    for i in inmates:
        l += [i['href']]

l = [x.strip('https://thegeorgiagazette.com/fayette/') for x in l]

search = input()



for index , x in enumerate(l):
    if x == search:
        print(index, 'found', x)

print(l)

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print(error)
else:
    print(response.content)