# main.py
from app.extract import extract_text_from_pdf
from app.embeddings import similarity

if __name__ == "__main__":
    jd = """
    We are looking for a Python backend developer with experience in FastAPI,
    SQL databases, and basic machine learning.
    """

    pdf_path = "data/resumes/sample_resume.pdf"  # put one test resume here
    resume_text = extract_text_from_pdf(pdf_path)

    score = similarity(jd, resume_text)
    print(f"Similarity score: {score:.4f}")
