import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin

def scrape_1a_video_cards():
    base_url = "https://www.1a.lv"
    url = "https://www.1a.lv/c/datoru-komponentes-tikla-produkti/komponentes/video-kartes/2vs"
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    data = []
    
    try:
        # Get main page
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all products
        for product in soup.find_all('div', class_='catalog-taxons-product'):
            # Get name and price
            name = product.find('a', class_='catalog-taxons-product__name').get_text(strip=True)
            price = product.find('span', class_='catalog-taxons-product-price__price-number')
            price = price.get_text(strip=True) if price else 'N/A'
            
            # Get specs from product page
            specs = []
            try:
                product_url = urljoin(base_url, product.find('a')['href'])
                product_page = requests.get(product_url, headers=headers).text
                product_soup = BeautifulSoup(product_page, 'html.parser')
                
                for spec in product_soup.find_all('li', class_='catalog-taxons-product-key-attribute-list__item'):
                    specs.append(spec.get_text(' ', strip=True))
            except:
                specs = ['Could not load specs']
            
            # Combine name and specs
            description = name + '\n' + '\n'.join(specs)
            data.append({'Video Card': description, 'Price': price})
            time.sleep(1)
        
        # Save to Excel
        pd.DataFrame(data).to_excel('video_cards.xlsx', index=False)
        print(f"Saved {len(data)} products")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_1a_video_cards()