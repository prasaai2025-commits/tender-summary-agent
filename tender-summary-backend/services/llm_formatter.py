def format_summary(identity, dates, technical, eligibility, finance, penalties, filename):

    def section(title, content_dict):
        if not content_dict:
            return ""

        out = f"\n{title}\n" + "-" * len(title) + "\n"
        for k, v in content_dict.items():
            label = k.replace("_", " ").title()
            out += f"• {label}: {v}\n"
        return out

    summary = f"""
TENDER SUMMARY – EXECUTIVE VIEW

Source Document: {filename}

This document provides a high-level executive summary of the tender,
highlighting key commercial, technical, eligibility and risk parameters
to support bid decision-making.
"""

    summary += section("1. Tender Identity", identity)
    summary += section("2. Key Dates & Timeline", dates)
    summary += section("3. Technical Capacity & Highlights", technical)
    summary += section("4. Eligibility Criteria", eligibility)
    summary += section("5. Commercial Terms", finance)
    summary += section("6. Warranty & Penalties", penalties)

    summary += """
--------------------------------
Executive Note:
--------------------------------
This summary is auto-generated from the tender document.
In case of any ambiguity, the original tender document
shall prevail.
"""

    return summary.strip()
