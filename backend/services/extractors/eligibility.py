import re

def extract_eligibility(text: str):
    e = {}
    t = re.sub(r"\s+", " ", text)

    e["bidder_type"] = "Consortium allowed" if re.search(r"consortium", t, re.IGNORECASE) else "Sole bidder"

    m = re.search(r"turnover.*?Rs\.?\s?([\d,\.]+)\s*Cr", t, re.IGNORECASE)
    if m:
        e["turnover"] = f"Minimum turnover Rs. {m.group(1)} Cr"

    if re.search(r"experience.*data centre|datacenter", t, re.IGNORECASE):
        e["experience"] = "Data Centre experience required"

    if re.search(r"CDCP|CDCS|CDCE", t):
        e["certifications"] = "Certified DC professionals required"

    if re.search(r"Manufacturer Authorization|MAF", t, re.IGNORECASE):
        e["maf"] = "OEM MAF required"

    return e
