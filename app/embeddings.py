# app/embeddings.py
from sentence_transformers import SentenceTransformer, util

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def similarity(jd_text: str, resume_text: str) -> float:
    model = get_model()
    jd_emb = model.encode(jd_text, convert_to_tensor=True)
    res_emb = model.encode(resume_text, convert_to_tensor=True)
    sim = util.cos_sim(jd_emb, res_emb)
    return float(sim.item())
