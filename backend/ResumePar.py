import spacy
import re
import json
from Skillset import job_roles_skills, skills_db
import dotenv
import os
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

nlp = spacy.load('en_core_web_sm')

def extract_email(text):
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return emails[0] if emails else None

def extract_phone(text):
    phones = re.findall(r"\+?\d[\d\s-]{8,}\d", text)
    return phones[0] if phones else None

def extract_linkedin(text):
    urls = re.findall(r"(?:https?://)?(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+/?", text)
    if urls:
        url = urls[0]
        if not url.startswith("http"):
            url = "https://" + url
        return url
    return None

def extract_github(text):
    urls = re.findall(r"(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9_-]+/?", text)
    if urls:
        url = urls[0]
        if not url.startswith("http"):
            url = "https://" + url
        return url
    return None

def extract_name(text):
    doc = nlp(text[:1000])
    person_entities = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

    if person_entities:
        return person_entities[0]
    return None

escaped_skills = [re.escape(skill) for skill in skills_db]
SKILLS_REGEX = re.compile(r"\b(" + "|".join(escaped_skills) + r")\b", re.IGNORECASE)

def extract_skills(text):
    text = text.lower()
    found_skills = SKILLS_REGEX.findall(text)
    return list(set(found_skills))

def analyse_skills(text,job_role):
    job_role = job_role.lower()
    if job_role not in job_roles_skills:
        raise ValueError(f"Unsupported job role {job_role}")

    text = text.lower()
    required_skills = job_roles_skills[job_role]
    found_skills = []
    missing_skills = []

    for skill in required_skills:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)
        else:
            missing_skills.append(skill)
    return found_skills, missing_skills

def clean_llm_output(text):
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        return None

    json_str = text[start:end+1]

    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return None

def analyse_sections(text):
    prompt = f"""
    Extract structured resume data.

    Return ONLY valid JSON matching this schema:

    {{
    "education": [
        {{
        "degree": "",
        "institution": "",
        "year": ""
        }}
    ],
    "experience": [
        {{
        "title": "",
        "company": "",
        "duration": "",
        "description": ""
        }}
    ],
    "projects": [
        {{
        "title": "",
        "description": "",
        "technologies": []
        }}
    ],
    "certifications": []
    }}

    Important rules:
    - education items MUST be objects with degree, institution, year fields
    - experience items MUST be objects with title, company, duration, description fields
    - projects items MUST be objects with title, description, technologies fields
    - certifications can be plain strings
    - If a field is unknown, use an empty string

    Resume:
    {text[:4000]}
    """



    try:
        print(prompt)
        print(f"Length of prompt is: {len(prompt)}")
        response = client.chat.completions.create(
            model="inclusionai/ring-2.6-1t:free",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ],
            temperature=0.1,
            response_format={"type":"json_object"},
            max_tokens=2000
        )
        print(response)
        return response.choices[0].message.content
    except Exception as e:
        print("\n ---- Exception Occured ----\n")
        print(e)

        return {
            "error": str(e),
            "education": [],
            "experience": [],
            "projects": [],
            "certifications": []
        }

