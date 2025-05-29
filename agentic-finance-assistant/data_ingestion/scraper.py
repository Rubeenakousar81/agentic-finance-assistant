import requests
from bs4 import BeautifulSoup

def scrape_earnings_news(query="TSMC"):
    """
    Scrapes Yahoo Finance news search results for a given company name or ticker.
    """
    search_url = f"https://finance.yahoo.com/quote/{query}/news"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error during scraping:", e)
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    for item in soup.find_all("li", class_="js-stream-content"):
        headline = item.find("h3")
        summary = item.find("p")
        link = item.find("a", href=True)
        if headline and link:
            articles.append({
                "title": headline.text.strip(),
                "summary": summary.text.strip() if summary else "",
                "link": f"https://finance.yahoo.com{link['href']}"
            })

    return articles
