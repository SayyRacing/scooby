import requests
from bs4 import BeautifulSoup

try:
    source = requests.get('https://poszukiwani.policja.pl/pos/form/5,Poszukiwani.html')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    wanted = soup.find_all('li', class_='threeRows thumbList')

    for person in wanted:

        wanted = person.find('strong').text
        wantedLink = person.find('a')['href']
        print(f"{wanted} https://poszukiwani.policja.pl{wantedLink}")

except Exception as e:
    print(e)
