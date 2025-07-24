import json
from datetime import datetime

def create_output(metadata, top_chunks, output_file="challenge1b_output.json"):
    output = {
        "metadata": {
            "input_documents": metadata["docs"],
            "persona": metadata["persona"],
            "job_to_be_done": metadata["job"],
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for i, chunk in enumerate(top_chunks):
        output["extracted_sections"].append({
            "document": chunk["doc"],
            "page_number": chunk["page"],
            "section_title": f"Chunk {i+1}",
            "importance_rank": i + 1
        })
        output["subsection_analysis"].append({
            "document": chunk["doc"],
            "page_number": chunk["page"],
            "refined_text": chunk["summary"]
        })

    with open(output_file, "w") as f:
        json.dump(output, f, indent=4)
