def chunk_chapter(md: str, chapter: str = "12 kap.") -> list[dict]:
    """Splits a chapter into one chunk per paragraph (§), with the heading above it as title."""
    section = md.split("\n## AVD.")[0]

    # Split the text at every bold paragraph start (e.g., "**1 §**", "**6 a §**")
    raw_chunks = section.split("\n**")

    chunks = []
    # Skip index 0 (chapter intro before 1 §) and enumerate from 1 for unique IDs
    for i, raw in enumerate(raw_chunks[1:], start=1):
        # Skip repealed paragraphs ("Har upphävts")
        if "Har upphävts" in raw:
            continue

        # Extract the paragraph number before " §**" (e.g., "1" or "6 a")
        paragraph_nr = raw.split(" §**")[0].strip()

        chunks.append({
            "chunk_id": f"il_12_{i}",
            "paragraph_nr": paragraph_nr,
            # Re-attach the leading "**" lost during split and prepend chapter context
            "content": f"{chapter} **{raw.strip()}",
        })

    return chunks