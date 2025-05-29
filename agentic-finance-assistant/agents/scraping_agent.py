from data_ingestion.scraper import scrape_earnings_news

def scraping_agent(company_name="TSMC"):
    """
    Calls the scraping function and formats the output for downstream agents.
    """
    print(f"[Scraping Agent] Fetching earnings news for: {company_name}")
    news_data = scrape_earnings_news(company_name)

    if not news_data:
        return f"No recent earnings news found for {company_name}."

    # Format the news into a single text block for downstream processing
    summary_text = ""
    for article in news_data[:3]:  # Limit to top 3 articles
        summary_text += f"Title: {article['title']}\n"
        summary_text += f"Summary: {article['summary']}\n"
        summary_text += f"Link: {article['link']}\n\n"

    return summary_text.strip()
