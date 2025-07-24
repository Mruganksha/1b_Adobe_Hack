import torch
from modules.embedding import get_embedding

def rank_chunks(chunks, persona, job):
    query = f"{persona}. Task: {job}"
    query_vec = get_embedding(query)

    for chunk in chunks:
        chunk_vec = get_embedding(chunk["text"])
        similarity = torch.nn.functional.cosine_similarity(query_vec, chunk_vec, dim=0).item()
        chunk["score"] = similarity

    return sorted(chunks, key=lambda x: x["score"], reverse=True)
