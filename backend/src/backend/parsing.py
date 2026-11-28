def chunk_chapter(md: str, chapter: str = "12 kap.") -> list[dict]:
    """Splits a chapter into one chunk per paragraph (§), with the heading above it as title."""
    section = md.split("\n## AVD.")[0]

    # Split the text at every bold paragraph start (e.g., "**1 §**", "**6 a §**")
    raw_chunks = section.split("\n**")

    chunks = []
    title = ""
    for raw in raw_chunks:
        # Separate the paragraph text from the heading(s) that belong to the NEXT paragraph
        parts = raw.split("\n#### ")
        text = parts[0]

        # Only real paragraphs, skip repealed ones ("Har upphävts")
        if " §**" in text and "Har upphävts" not in text:
            # Extract the paragraph number before " §**" (e.g., "1" or "6 a")
            paragraph_nr = text.split(" §**")[0].strip()

            chunk_id = f"il_12_{paragraph_nr.replace(' ', '')}"
            if "Träder i kraft" in text:
                chunk_id += "_ny"

            chunks.append({
                "chunk_id": chunk_id,
                "paragraph_nr": paragraph_nr,
                # Re-attach the leading "**" lost during split and prepend chapter + heading
                "content": f"{chapter} {title}\n**{text.strip()}",
            })

        # Remember the last heading, it belongs to the next paragraph
        if len(parts) > 1:
            title = parts[-1].strip()

    return chunks