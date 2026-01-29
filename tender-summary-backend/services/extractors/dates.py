import re

def extract_dates(text: str):
    dates = {}
    t = re.sub(r"\s+", " ", text.lower())

    patterns = {
        "last_date_of_submission": r"(last date|submission deadline).*?(\d{1,2}[./-]\d{1,2}[./-]\d{2,4})",
        "technical_bid_opening": r"(technical bid).*?(opening)?.*?(\d{1,2}[./-]\d{1,2}[./-]\d{2,4})",
        "financial_bid_opening": r"(financial bid).*?(opening)?.*?(\d{1,2}[./-]\d{1,2}[./-]\d{2,4})",
        "completion_period": r"(completion|delivery|project duration).*?(\d+\s*(days|months|weeks))"
    }

    for k, pat in patterns.items():
        m = re.search(pat, t, re.IGNORECASE)
        if m:
            dates[k] = m.group(m.lastindex)

    return dates
