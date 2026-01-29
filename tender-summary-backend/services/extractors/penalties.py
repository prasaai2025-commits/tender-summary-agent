import re

def extract_penalties(text: str):
    p = {}
    t = re.sub(r"\s+", " ", text)

    if re.search(r"warranty", t, re.IGNORECASE):
        p["warranty"] = "Warranty applicable as per tender"

    if re.search(r"liquidated damages|delay", t, re.IGNORECASE):
        p["delay_penalty"] = "Delay penalties applicable"

    if re.search(r"uptime", t, re.IGNORECASE):
        p["uptime"] = "Uptime based penalties applicable"

    return p
