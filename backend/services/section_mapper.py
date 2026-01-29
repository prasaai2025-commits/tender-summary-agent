def map_sections(text):
    sections = {
        "eligibility": [],
        "technical": [],
        "payment": [],
        "penalty": []
    }

    lines = text.split("\n")
    for i, line in enumerate(lines):
        l = line.lower()

        if any(x in l for x in ["eligibility", "pre-qualification", "qualification"]):
            sections["eligibility"].append(i)

        if any(x in l for x in ["technical", "specification", "scope of work"]):
            sections["technical"].append(i)

        if any(x in l for x in ["payment", "milestone", "billing"]):
            sections["payment"].append(i)

        if any(x in l for x in ["penalty", "liquidated damages", "ld"]):
            sections["penalty"].append(i)

    return {"lines": lines, "sections": sections}
