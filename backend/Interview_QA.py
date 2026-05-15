import dotenv
import os
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


def Generate_QA(resume_info, job_role, job_description=None):
    prompt = f"""
    Analyze this candidate for the role: {job_role}

    Resume:
    {resume_info}

    Job Description:
    {job_description or "Not provided"}

    Return ONLY valid JSON:

    {{
    "missing_skills": [
        {{
        "skill": "",
        "reason": "",
        "priority": "high|medium|low"
        }}
    ],
    "project_suggestions": [
        {{
        "title": "",
        "description": "",
        "skills_targeted": [],
        "difficulty": "beginner|intermediate|advanced"
        }}
    ],
    "interview_QA": [
        {{
        "question": "",
        "answer": "",
        "category": "technical|behavioral|situational",
        "difficulty": "easy|medium|hard"
        }}
    ]
    }}

    Tasks:
    - Identify missing skills
    - Suggest 3 high impact projects which improves my resume and skills
    - Generate 3 interview questions per category
    - Keep answers concise
    - Do not invent experience
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
            max_tokens=2500
        )
        print(response)
        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return {
            "missing_skills": [
                {
                    "skill": "",
                    "reason": "",
                    "priority": ""
                }
            ],
            "project_suggestions": [
                {
                    "title": "",
                    "description": "",
                    "skills_targeted": [],
                    "difficulty": ""
                }
            ],
            "interview_QA": [
                {
                    "question": "",
                    "answer": "",
                    "category": "",
                    "difficulty": ""
                }
            ]
        }

