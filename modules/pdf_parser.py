import fitz

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    extracted = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            extracted.append({
                "page": i + 1,
                "text": text
            })
    return extracted