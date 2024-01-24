import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

def scrape_and_save_to_csv():
    try:
        page_number = 0
        results = []
        
        while True:
            print(page_number)
            source = requests.get(f'https://poszukiwani.policja.pl/pos/form/5,Poszukiwani.html?page={page_number}')
            source.raise_for_status()
            soup = BeautifulSoup(source.text, 'html.parser')
            wanted = soup.find_all('li', class_='threeRows thumbList')
            
            if not wanted:
                break
            
            for person in wanted:
                wanted = person.find('strong').text
                wantedLink = person.find('a')['href']
                results.append({'Name': wanted, 'Link': f"https://poszukiwani.policja.pl{wantedLink}"})
            
            page_number += 1

        today = date.today()
        file_name = f"results_{today}.csv"

        with open(file_name, 'w', newline='') as file:
            fieldnames = ['Name', 'Link']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

        print(f"Scraping completed. Results saved to {file_name}")

    except Exception as e:
        print(e)

polish_police_dict = {
    'A': 2,
    'B': 3,
    'C': 4,
    'Ć': 5,
    'D': 6,
    'E': 7,
    'Ę': 8,
    'F': 9,
    'G': 10,
    'H': 11,
    'I': 12,
    'J': 13,
    'K': 14,
    'L': 15,
    'Ł': 16,
    'M': 17,
    'N': 18,
    'O': 19,
    'Ó': 20,
    'P': 21,
    'Q': 22,
    'R': 23,
    'S': 24,
    'Ś': 25,
    'T': 26,
    'U': 27,
    'V': 28,
    'W': 29,
    'X': 30,
    'Y': 31,
    'Z': 32,
    'Ż': 33,
    'Ź': 34,
}

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

#scrape_and_save_to_csv()

get_wanted_by_last_name('kojot')

