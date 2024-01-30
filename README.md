# Scooby 

Autorzy:

- Szymon Paluszewski. Nr. 58193 @SayyRacing,

- Bartosz Rokita. Nr. 58197 @ketrabx1x

Praca wykonana na potrzeby zaliczenia przedmiotu "OSINT - narzędzia i rozwiązywanie spraw" prowadzonego przez mgr Grzegorza Piotrowskiego na Uniwersytecie WSB Merito w Gdańsku.

Cel projektu:
Celem projektu było stworzenie crawlera do pobierania listy osób poszukiwanych na terenie Polski ze strony internetowej policji:
https://poszukiwani.policja.pl/pos/form/5,Poszukiwani.html

Opis narzędzia:
Program o nazwie „Scooby” został napisany w języku python. Program pracuje na licencji MIT. Program jest prostą aplikacją konsolową pozwalającą na wyszukanie osób poszukiwanych poprzez podanie nazwiska. Po wpisaniu nazwiska osoby poszukiwanej program rozpoznaje pierwszą literę nazwiska, następnie odwiedzą odpowiednio posortowaną stronę i wyszukuje wszystkie pasujące rekordy. Program posiada również opcje pobrania wszystkich osób poszukiwanych na terenie RP i zapisania ich w pliku CSV.
W celu uruchomienia programu należy pobrać pliki z repozytorium na swój komputer a następnie otworzyć projekt edytorze kodu np. Visual Studio Code. 
Program do uruchomienia wymaga posiadanego zainstalowanego języka Python oraz następujących bibliotek: requests, beautifulsoup4, scrapy.
Aby zainstalować powyższe biblioteki należy użyć tych poleceń w terminalu:
pip install requests
pip install beautifulsoup4
pip install scrapy


Zastosowanie nr. 1: 
W celu przetestowania pierwszej funkcji programu polegającej na wyszukaniu osób o konkretnym nazwisku ustawiamy parametr wejściowy na „Ewert”
Wynik testu:

![image](https://github.com/SayyRacing/scooby/assets/93188612/5b249d6a-7ca9-4e0c-8625-39b367fbd689)

Zastosowanie nr. 2:
Ponieważ kod drugiej funkcji jest ustawiony tak aby rozpocząć pobieranie danych ze wszystkich stron z listą osób poszukiwanych proces ten jest długotrwały. Na potrzeby testu zmodyfikujemy kod tak aby obsłużył ostatnie 10 stron z osobami poszukiwanymi.
Wynik testu:

![image](https://github.com/SayyRacing/scooby/assets/93188612/aafddad0-0b5e-4347-be93-509feb25d2c7)


Podsumowanie:
Scooby to efektywny crawler, który skanuje strony internetowe z osobami poszukiwanymi przez policję. Program oferuje dwie główne funkcje, które są użyteczne i spełniają swoje zadanie w sposób zadowalający. Jednakże, istnieją pewne obszary do poprawy. Mechanizm dopasowywania w wyszukiwaniu osób poszukiwanych może wymagać pewnych poprawek, a proces pobierania i zapisywania danych do pliku CSV może trwać dłużej ze względu na dużą ilość stron i rekordów do pobrania. Mimo tych wyzwań, Scooby to solidny program, który ma duży potencjał do dalszego rozwoju.
