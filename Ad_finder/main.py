
import sys
sys.path.insert(1, '/Users/mm.m.mm/Desktop/divar project 1/')

from utils.functions import clear
from requests import get
from bs4 import BeautifulSoup
from os import makedirs







if __name__ == '__main__':
    clear()
    main_url = 'https://www.divar.ir'
    
    raw = get('https://divar.ir/s/tehran')
    html_file = BeautifulSoup(raw.text, 'html.parser')
    
    categories = html_file.find_all('a', {'class': 'kt-accordion-item__header'})
    
    links = []
    for c in categories:
        links.append(c.get('href'))
     
   
    for link in links:
        clear()
        print(f'ads on {link}:\n')
        
        raw = get(f'{main_url}{link}')
        html_file = BeautifulSoup(raw.text, 'html.parser')
        
        ads = html_file.find_all('div', {'class': 'post-card-item'})
        ads = ads[:10]
        for ad in ads:
            title = ad.find_all('h2', {'class': 'kt-post-card__title'})[0].text
            print(title)
            print(f'{ad.find("a").get("href")}\n')
        
        input('\n\npress enter to continue...')
        