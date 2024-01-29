import requests
from bs4 import BeautifulSoup
import csv
from datetime import date
from dictionaries import polish_police_dict

def get_wanted_by_last_name(name):
    try:
        name = name.upper()  # Convert the name to uppercase
        first_letter = name[0]  # Get the first letter of the name
        letter_filter = polish_police_dict[first_letter]  # Match the first letter with a number from the dictionary

        page_number = 0  # Addon to the url to get the next page
        while True:    
            source = requests.get(f'https://poszukiwani.policja.pl/pos/form/5,Poszukiwani.html?l={letter_filter}' + f'&page={page_number}')
            print(source.url)
            source.raise_for_status()
            soup = BeautifulSoup(source.text, 'html.parser')
            wanted = soup.find_all('li', class_='threeRows thumbList')

            if not wanted:  # If no li elements are found, break the loop
                break
            
            for person in wanted:
                wanted = person.find('strong').text
                if name in wanted:
                    wantedLink = person.find('a')['href']
                    print(f"{wanted} - https://poszukiwani.policja.pl{wantedLink}")
            page_number += 1
            

    except Exception as e:
        print(e)
