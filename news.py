import requests


newsapi = "Your News API key"
def fetch_news():
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
    if r.status_code == 200:
        # Parse the JSON response
        data = r.json()
        
        articles = data.get('articles', [])
        
        # Print the headlines
        for article in articles:
            news = article["title"]
            return news
            # print(news)