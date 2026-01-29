import re

def extract_technical(text: str):
    tech = {}
    t = re.sub(r"\s+", " ", text)

    m = re.search(r"(IT Load|Power Load).*?([\d\.]+)\s*KW", t, re.IGNORECASE)
    if m:
        tech["it_load_kw"] = m.group(2) + " KW"

    racks = re.findall(r"(\d+)\s*(IT|Server)\s*Racks", t, re.IGNORECASE)
    if racks:
        tech["rack_count"] = ", ".join(sorted(set(r[0] for r in racks)))

    cooling = re.findall(r"(Chiller|PAC).*?([\d\.]+)\s*(TR|KW)", t, re.IGNORECASE)
    if cooling:
        tech["cooling"] = ", ".join(f"{c[1]} {c[2]}" for c in cooling)

    ups = re.findall(r"UPS.*?([\d\.]+)\s*KVA", t, re.IGNORECASE)
    if ups:
        tech["ups"] = ", ".join(sorted(set(ups)))

    if re.search(r"N\+1", t):
        tech["redundancy"] = "N+1"
    elif re.search(r"N\+N", t):
        tech["redundancy"] = "N+N"

    return tech
