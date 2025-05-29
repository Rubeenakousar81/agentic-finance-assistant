from data_ingestion.api_loader import fetch_stock_data

def api_agent(ticker):
    data = fetch_stock_data(ticker)
    change = round((data['Close'][-1] - data['Close'][-2]) / data['Close'][-2] * 100, 2)
    return f"{ticker} change: {change}%"
