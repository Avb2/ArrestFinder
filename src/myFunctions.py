from bs4 import BeautifulSoup
import requests
import webbrowser


def runSearch(county, fname, lname):
    def get_response(url):
        return requests.get(url)

    def get_result(response):
        return BeautifulSoup(response.text, 'html.parser')

    # Main url
    url = f'https://thegeorgiagazette.com/{county.get()}/{fname.get()}-{lname.get()}/'

    # Checks the first page for the inmate
    try:
        response = get_response(url)
        result = get_result(response)

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
    except requests.exceptions.HTTPError:
        pass

    # Checks pages 2-10 for the inmate
    for x in range(2, 10):
        url = f'https://thegeorgiagazette.com/{county.get()}/{fname.get()}-{lname.get()}-{x}/'
        response = get_response(url)
        result = get_result(response)

        try:
            response.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(x, error)
            if x == 10:
                try:
                    webbrowser.open(f'https://thegeorgiagazette.com/{fname.get()}-{lname.get()}/')
                except requests.exceptions.HTTPError:
                    print(error)

        else:
            webbrowser.open(url)
