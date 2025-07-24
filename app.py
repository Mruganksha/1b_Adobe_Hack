import os
from modules import pdf_parser, chunker, ranker, summarizer, output_formatter

def main():
    print("\n Persona-Driven Document Intelligence System\n")

    # Step 1: User Inputs
    folder = input("Enter the folder path containing PDF files (e.g., test_documents): ").strip()
    persona = input("Enter the persona (e.g., Investment Analyst): ").strip()
    job = input("Enter the job-to-be-done (e.g., Analyze revenue trends and R&D spend): ").strip()

    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' does not exist.")
        return

    pdf_files = [f for f in os.listdir(folder) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print("No PDF files found in the folder.")
        return

    print(f"\n Found {len(pdf_files)} document(s). Processing...\n")

    # Step 2: Extract and Chunk Text
    all_chunks = []
    for file in pdf_files:
        path = os.path.join(folder, file)
        pages = pdf_parser.extract_text_from_pdf(path)
        chunks = chunker.chunk_text(pages)
        for chunk in chunks:
            chunk["doc"] = file
        all_chunks.extend(chunks)

    # Step 3: Rank Chunks
    ranked_chunks = ranker.rank_chunks(all_chunks, persona, job)
    top_chunks = ranked_chunks[:3]  # top 3 most relevant

    # Step 4: Summarize Top Chunks
    for chunk in top_chunks:
        chunk["summary"] = summarizer.summarize_text(chunk["text"])

    # Step 5: Create Output
    metadata = {
        "docs": pdf_files,
        "persona": persona,
        "job": job
    }

    output_formatter.create_output(metadata, top_chunks)

    print(" Output generated: challenge1b_output.json")

if __name__ == "__main__":
    main()
