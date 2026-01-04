# main.py (updated)
from app.extract import extract_text_from_pdf
from app.embeddings import similarity
from app.skills import extract_skills, skill_overlap

if __name__ == "__main__":
    jd = """
    We are looking for a Python backend developer with experience in FastAPI,
    SQL databases, Docker, and basic machine learning using scikit-learn.
    """
    
    # Extract JD skills (you'd parse this properly later)
    jd_skills = ['python', 'fastapi', 'sql', 'docker', 'scikit-learn', 'machine learning']
    
    pdf_path = "data/resumes/sample_resume.pdf"
    resume_text = extract_text_from_pdf(pdf_path)
    
    # Semantic similarity
    semantic_score = similarity(jd, resume_text)
    
    # Skill extraction
    resume_skills = extract_skills(resume_text)
    skill_score = skill_overlap(jd_skills, resume_skills)
    
    # Combined score (weighted)
    final_score = 0.7 * semantic_score + 0.3 * skill_score
    
    print(f"Resume text preview: {resume_text[:200]}...")
    print(f"Semantic similarity: {semantic_score:.4f}")
    print(f"Skills found: {resume_skills}")
    print(f"Skill overlap score: {skill_score:.4f}")
    print(f"Final score: {final_score:.4f}")
