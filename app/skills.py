# app/skills.py
import re

# Common skills (expand this list as needed)
COMMON_SKILLS = [
    # Programming
    'python', 'java', 'javascript', 'js', 'c++', 'c#', 'go', 'rust', 'scala', 'php',
    'react', 'angular', 'vue', 'node.js', 'nodejs', 'django', 'flask', 'fastapi', 'spring',
    
    # ML/AI
    'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'scikit-learn',
    'numpy', 'pandas', 'sql', 'postgresql', 'mysql',
    
    # Cloud/DevOps
    'aws', 'gcp', 'docker', 'kubernetes', 'jenkins', 'git', 'linux',
    
    # Other
    'api', 'rest', 'microservices', 'agile', 'docker'
]

def extract_skills(text: str) -> list[str]:
    """
    Extract skills from resume text (simple keyword matching)
    """
    text_lower = text.lower()
    found_skills = []
    
    for skill in COMMON_SKILLS:
        # Look for whole words or phrases
        if re.search(rf'\b{re.escape(skill)}\b', text_lower):
            found_skills.append(skill)
    
    return found_skills

def skill_overlap(jd_skills: list[str], resume_skills: list[str]) -> float:
    """
    Jaccard similarity between skill sets
    """
    intersection = len(set(jd_skills) & set(resume_skills))
    union = len(set(jd_skills) | set(resume_skills))
    return intersection / union if union > 0 else 0.0
