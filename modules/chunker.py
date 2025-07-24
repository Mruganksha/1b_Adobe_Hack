def chunk_text(pages, chunk_size=300):
    chunks = []
    for page in pages:
        words = page["text"].split()
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            if chunk.strip():
                chunks.append({
                    "page": page["page"],
                    "text": chunk
                })
    return chunks
