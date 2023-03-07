import webbrowser
from bs4 import BeautifulSoup
import requests

# Information input
fname = input('First Name')
lname = input('Last Name ')

city = input('City')

# Checks the first page for the inmate
try:
    url = f'https://thegeorgiagazette.com/{city}/{fname}-{lname}/'
    response = requests.get(url)
    result = BeautifulSoup(response.text, 'html.parser')

    # Checks if the page exists
    try:
        response.raise_for_status()

    # If the page doesn't exist, it prints an error
    except requests.exceptions.HTTPError as error:
        print(error)

    # If the page exists, the url/urls are opened
    else:
        webbrowser.open(url)
        reasonForArrest = result.findAll('p')
        for reasons in reasonForArrest:
            for x in reasons:
                print(x.text)


except:
    pass

# Checks pages 2-10 for the inmate
for x in range(2, 10):
    url = f'https://thegeorgiagazette.com/{city}/{fname}-{lname}-{x}/'
    response = requests.get(url)
    result = BeautifulSoup(response.text, 'html.parser')

    try:
        response.raise_for_status()

    except requests.exceptions.HTTPError as error:
        print(x, error)
        if x == 10:
            try:
                webbrowser.open(f'https://thegeorgiagazette.com/{fname}-{lname}/')
            except requests.exceptions.HTTPError:
                print(error)

    else:
        webbrowser.open(url)
        reasonForArrest = result.findAll('p')

        print(x)
        for reasons in reasonForArrest:
            for x in reasons:
                print(x.text)
