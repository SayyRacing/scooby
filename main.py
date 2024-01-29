from getByName import get_wanted_by_last_name
from scrapydoo import scrapy_find_all

def console_menu():
    while True:
        print("1. Search by name")
        print("2. Scrape all and save to CSV")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ")
            get_wanted_by_last_name(name)
        elif choice == '2':
            print("WARNING This may take a while. Are you sure you want to continue? (y/n)")
            choice = input("Enter your choice: ")
            if choice == 'y':
                scrapy_find_all()
            else:
                print("Aborting...")
                continue
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

console_menu()

