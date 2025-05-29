from fastapi import FastAPI, Query
from agents.api_agent import api_agent
from agents.scraping_agent import scraping_agent
from agents.analysis_agent import analyze_portfolio, analyze_earnings
from agents.language_agent import generate_summary

app = FastAPI(title="Agentic Finance Assistant")

# --- 1. API Agent ---
@app.get("/api-agent")
def get_api_data(ticker: str = "TSMC"):
    result = api_agent(ticker)
    return {"message": result}


# --- 2. Scraping Agent ---
@app.get("/scraping-agent")
def get_scraped_news(company: str = "TSMC"):
    result = scraping_agent(company)
    return {"news": result}


# --- 3. Portfolio Analysis Agent ---
@app.post("/analyze-portfolio")
def portfolio_analysis():
    # Sample static input
    portfolio_data = {
        "Asia_Tech": {"today": 22, "yesterday": 18}
    }
    result = analyze_portfolio(portfolio_data)
    return {"analysis": result}


# --- 4. Earnings Analysis Agent ---
@app.post("/analyze-earnings")
def earnings_analysis():
    # Sample input
    earnings_data = [
        {"company": "TSMC", "actual": 1.04, "estimate": 1.00},
        {"company": "Samsung", "actual": 0.98, "estimate": 1.00}
    ]
    result = analyze_earnings(earnings_data)
    return {"earnings_summary": result}


# --- 5. LLM Language Agent ---
@app.get("/llm-summary")
def run_language_agent(query: str = "Summarize today's market risk exposure"):
    result = generate_summary(query, retriever=None)  # Plug retriever if needed
    return {"summary": result}
