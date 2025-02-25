import requests
import json
from pytrends.request import TrendReq
import requests
from bs4 import BeautifulSoup
import feedparser

def get_seo_keywords(topic):
    """Fetch related keywords using Google Suggest API."""
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={topic}"
    response = requests.get(url)
    if response.status_code == 200:
        suggestions = json.loads(response.text)[1]
        return suggestions[:20]
    return []


def get_trending_keywords():
    url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=IN"
    feed = feedparser.parse(url)
    return [entry["title"] for entry in feed.entries]





