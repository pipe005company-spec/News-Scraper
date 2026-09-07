import requests
from bs4 import BeautifulSoup

def see_all_headlines():
    url = "http://www.bbc.com/news"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get all h2 tags (BBC uses these for headlines)
    all_h2 = soup.find_all('h2')
    
    print(f"Found {len(all_h2)} h2 tags:\n")
    for i, h2 in enumerate(all_h2[:10]):
        text = h2.text.strip()
        if text:
            print(f"{i+1}. {text}")

if __name__ == "__main__":
    see_all_headlines()