# 📄 Smart Resume Analyzer

> An AI-powered Resume Analyzer that evaluates resumes against target job roles, identifies missing skills, suggests impactful projects, and generates personalized interview questions using Large Language Models (LLMs).

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM-orange)
![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 🚀 Overview

Smart Resume Analyzer helps job seekers evaluate how well their resume matches a target role.

Instead of only extracting resume information, the application performs an end-to-end AI analysis by:

- Parsing resume content
- Extracting candidate information
- Matching skills against industry role requirements
- Calculating skill match
- Identifying missing skills
- Recommending projects to improve the resume
- Generating personalized interview questions and answers

The application is built with **FastAPI**, **React**, **spaCy**, and **OpenRouter LLMs**, making it a complete AI-powered resume evaluation platform.

---

# ✨ Features

## 📄 Resume Parsing

- Upload PDF or DOCX resumes
- Extracts:
  - Name
  - Email
  - Phone Number
  - GitHub Profile
  - LinkedIn Profile
  - Skills

---

## 🎯 Job Role Analysis

Supports multiple predefined software roles such as:

- AI Engineer
- Machine Learning Engineer
- Data Scientist
- Backend Developer
- Frontend Developer
- Full Stack Developer
- Python Developer
- and many more.

---

## 📊 ATS-style Skill Matching

The analyzer compares extracted skills with required skills for the selected job role.

Provides:

- Matching Skills
- Missing Skills
- Match Percentage
- Resume Strength

---

## 🤖 AI Resume Review

Using OpenRouter LLMs, the application:

- Reviews the resume
- Identifies missing technical skills
- Suggests improvements
- Generates resume enhancement recommendations

---

## 💡 Project Recommendations

Instead of generic advice, the AI recommends projects that help candidates strengthen their resume for their chosen role.

Each recommendation includes:

- Project title
- Description
- Targeted skills
- Difficulty level

---

## 🎤 Interview Preparation

Automatically generates interview questions and concise answers.

Categories include:

- Technical
- Behavioral
- Situational

Difficulty levels:

- Easy
- Medium
- Hard

---

# 🏗 System Architecture

```text
                Resume (PDF/DOCX)
                        │
                        ▼
              Resume Text Extraction
                        │
                        ▼
             Information Extraction
       (Name, Email, Skills, Links)
                        │
                        ▼
           Skill Matching Engine
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
 ATS Skill Analysis             OpenRouter LLM
                                        │
                        ┌───────────────┴───────────────┐
                        ▼                               ▼
               Resume Suggestions           Interview Questions
                        │
                        ▼
                React Dashboard
```

---

# ⚙️ Tech Stack

## Frontend

- React
- Vite
- JavaScript
- CSS

---

## Backend

- FastAPI
- Python
- spaCy
- pdfminer
- python-docx

---

## AI

- OpenRouter API
- Large Language Models

---

## NLP

- spaCy
- Regex-based Information Extraction

---

# 📂 Project Structure

```
Smart-Resume-Analyzer/

│
├── backend/
│   ├── app.py
│   ├── ResumePar.py
│   ├── Interview_QA.py
│   └── Skillset.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── public/
│   └── package.json
│
└── requirements.txt
```

---

# 🔄 Workflow

```
Upload Resume
      │
      ▼
Extract Resume Text
      │
      ▼
Extract Candidate Details
      │
      ▼
Extract Skills
      │
      ▼
Compare with Job Role
      │
      ▼
Calculate Skill Match
      │
      ▼
Generate AI Recommendations
      │
      ▼
Generate Interview Questions
      │
      ▼
Display Results
```
---

# 📌 API Endpoints

## Get Available Roles

```
GET /api/job-roles
```

Response

```json
{
  "roles": [
    "AI Engineer",
    "Data Scientist",
    "Backend Developer"
  ]
}
```
---

## Analyze Resume

```
POST /api/analyse
```

Form Data

```
resume
job_role
job_description (optional)
```

Returns

- Candidate Details
- Skill Match
- Missing Skills
- Suggested Projects
- Interview Questions

---

# 📸 Application Screens

- Resume Upload
- Resume Analysis Dashboard
- Skill Match Overview
- Missing Skills
- Project Recommendations
- Interview Questions

---

# 🔑 Environment Variables

Create a `.env` file inside the backend directory.

```env
OPENROUTER_API_KEY=YOUR_API_KEY
```
---

# 🛠 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Smart-Resume-Analyzer.git
```
---

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```
---

## Frontend

```bash
cd frontend

npm install

npm run dev
```
---

# 🎯 Future Improvements

- Resume ATS Score
- Resume Formatting Suggestions
- Multiple Resume Comparison
- Company-specific Resume Analysis
- Resume Keyword Optimization
- Cover Letter Generator
- LinkedIn Profile Analyzer
- Resume Version Tracking
- Resume PDF Report
- Authentication
- Docker Deployment

---

# 💡 Key Highlights

- AI-powered Resume Analysis
- ATS-style Skill Matching
- Resume Parsing
- OpenRouter LLM Integration
- Personalized Interview Preparation
- Project Recommendation Engine
- FastAPI REST API
- React Dashboard

---

# 👨‍💻 Author

**Achal Basawa**

AI & ML Engineer

Focused on building practical Generative AI applications using FastAPI, LLMs, NLP, and Retrieval-Augmented Generation.

---

## ⭐ If you found this project useful, consider giving it a star!
