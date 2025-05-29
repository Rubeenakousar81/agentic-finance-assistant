def analyze_portfolio(allocation_data: dict) -> str:
    """
    Analyzes the allocation of assets in a portfolio.
    Expects a dictionary like:
    {
        "Asia_Tech": {
            "today": 22,
            "yesterday": 18
        },
        ...
    }
    Returns a human-readable summary.
    """
    print("[Analysis Agent] Analyzing portfolio data...")

    if not allocation_data or "Asia_Tech" not in allocation_data:
        return "No Asia Tech allocation data available."

    asia_today = allocation_data["Asia_Tech"]["today"]
    asia_yesterday = allocation_data["Asia_Tech"]["yesterday"]

    change = asia_today - asia_yesterday
    direction = "up" if change > 0 else "down" if change < 0 else "unchanged"
    summary = (
        f"Your Asia tech allocation is {asia_today}% of AUM, "
        f"{direction} from {asia_yesterday}% yesterday."
    )

    return summary


def analyze_earnings(earnings_data: list) -> str:
    """
    Analyzes earnings performance from a list of dicts like:
    [
        {"company": "TSMC", "actual": 1.04, "estimate": 1.00},
        {"company": "Samsung", "actual": 0.98, "estimate": 1.00},
    ]
    """
    print("[Analysis Agent] Analyzing earnings data...")
    output = []

    for entry in earnings_data:
        company = entry["company"]
        actual = entry["actual"]
        estimate = entry["estimate"]

        diff_percent = round((actual - estimate) / estimate * 100, 2)
        result = (
            f"{company} beat estimates by {abs(diff_percent)}%"
            if diff_percent > 0
            else f"{company} missed estimates by {abs(diff_percent)}%"
            if diff_percent < 0
            else f"{company} met estimates exactly"
        )
        output.append(result)

    return "\n".join(output)
