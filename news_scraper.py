import requests
from bs4 import BeautifulSoup

def get_news():
    url = "http://www.bbc.com/news"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h2', class_='sc-8ea7699c-3')

    news_list = []
    for headline in headlines[:5]:
        title = headline.text.strip()
        news_list.append(f"📰 {title}")

    return news_list

if __name__ == "__main__":
    news = get_news()
    for item in news:
        print(item)