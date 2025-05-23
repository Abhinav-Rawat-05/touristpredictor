import requests
from datetime import timedelta


def get_articles_for_location(location, date):
    from_date = (date - timedelta(days=2)).strftime('%Y-%m-%d')
    to_date = (date + timedelta(days=2)).strftime('%Y-%m-%d')
    api_key = "YOUR-API-KEY"

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={location}%20Uttarakhand&"
        f"from={from_date}&to={to_date}&"
        f"language=en&sortBy=publishedAt&"
        f"apiKey={api_key}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data for {location}. Error: {response.status_code}")
        return []

    articles = response.json().get("articles", [])
    return articles





