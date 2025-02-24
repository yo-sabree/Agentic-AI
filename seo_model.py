import requests
import json
from pytrends.request import TrendReq
import requests
from bs4 import BeautifulSoup

def get_seo_keywords(topic):
    """Fetch related keywords using Google Suggest API."""
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={topic}"
    response = requests.get(url)
    if response.status_code == 200:
        suggestions = json.loads(response.text)[1]
        return suggestions[:20]
    return []

def get_trending_keywords():
    """Fetch top trending Google search keywords."""
    url = "https://trends.google.com/trends/trendingsearches/daily?geo=IN"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    trends = soup.select(".title > .details > .title-container > a")
    return [trend.text for trend in trends[:10]]


