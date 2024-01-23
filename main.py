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

scrape_and_save_to_csv()