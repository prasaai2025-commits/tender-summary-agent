def chunk_text(text, mode, mapped):
    chunks = []
    lines = mapped["lines"]
    sections = mapped["sections"]

    if mode == "NORMAL":
        size = 2500
        for i in range(0, len(text), size):
            chunks.append(text[i:i+size])

    else:
        important_lines = []
        for key in sections:
            for idx in sections[key]:
                start = max(0, idx - 5)
                end = min(len(lines), idx + 40)
                important_lines.extend(lines[start:end])

        chunks.append("\n".join(important_lines))

    return chunks
