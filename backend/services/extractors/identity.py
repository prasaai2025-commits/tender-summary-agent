import re

def extract_identity(text: str):
    data = {
        "end_user": "Not specified",
        "tender_no": "Not specified",
        "tender_title": "Not specified",
        "tender_type": "Not specified",
        "tender_mode": "Not specified"
    }

    t = re.sub(r"\s+", " ", text)

    # END USER
    for pat in [
        r"(End User|Client|Department|Organization)\s*[:\-]\s*(.{5,100})",
        r"(Centre for Development of Advanced Computing|C-DAC|CDAC)"
    ]:
        m = re.search(pat, t, re.IGNORECASE)
        if m:
            data["end_user"] = m.group(m.lastindex).strip()
            break

    # TENDER NUMBER
    for pat in [
        r"(Tender|NIT|Bid|Reference)\s*(No\.?|Number)?\s*[:\-]?\s*([A-Z0-9\/\-\.]{6,})",
        r"(GEM\/[A-Z0-9\/\-]+)"
    ]:
        m = re.search(pat, t, re.IGNORECASE)
        if m:
            data["tender_no"] = m.group(m.lastindex)
            break

    # TITLE
    for pat in [
        r"(Tender for|RFP for|E-Tender for)\s+(.{10,120})",
        r"(Design|Supply|Construction|Setting up)\s+of\s+(.{10,120})"
    ]:
        m = re.search(pat, t, re.IGNORECASE)
        if m:
            data["tender_title"] = m.group(m.lastindex).strip()
            break

    # TYPE
    if re.search(r"two[- ]bid|2[- ]bid", t, re.IGNORECASE):
        data["tender_type"] = "Two Bid System"
    elif re.search(r"single[- ]bid|one[- ]bid", t, re.IGNORECASE):
        data["tender_type"] = "Single Bid System"

    # MODE
    if re.search(r"online|e[- ]tender|gem", t, re.IGNORECASE):
        data["tender_mode"] = "Online"
    elif re.search(r"offline", t, re.IGNORECASE):
        data["tender_mode"] = "Offline"

    return data
