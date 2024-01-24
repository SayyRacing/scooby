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

def get_wanted_by_name(name):
    try:
        addon = 0
        while True:    
            source = requests.get(f'https://poszukiwani.policja.pl/pos/form/5,Poszukiwani.html?l=19' + f'&page={addon}')
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
            addon += 1
            

    except Exception as e:
        print(e)

#scrape_and_save_to_csv()

get_wanted_by_name('OSTROWSKI')

