import re

def extract_finance(text: str):
    f = {}
    t = re.sub(r"\s+", " ", text)

    m = re.search(r"(EMD|Bid Security).*?Rs\.?\s?([\d,\.]+)", t, re.IGNORECASE)
    if m:
        f["emd"] = f"Rs. {m.group(2)}"

    m = re.search(r"Tender Fee.*?Rs\.?\s?([\d,\.]+)", t, re.IGNORECASE)
    if m:
        f["tender_fee"] = f"Rs. {m.group(1)}"

    m = re.search(r"(PBG|Performance Bank Guarantee).*?(\d+)\s*%", t, re.IGNORECASE)
    if m:
        f["pbg"] = f"{m.group(2)}% of Contract Value"

    return f
