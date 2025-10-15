from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Dummy in-memory data store for prototype
sample_case = {
    "id": 1,
    "title": "Case 1: Chest Pain and Dyspnea",
    "symptoms": ["Chest pain", "Shortness of breath"],
    "vitals": {"BP": "130/85", "HR": 95, "Temp": 98.6},
    "history": "Patient with history of hypertension and smoking.",
    "specialties": ["Cardiology", "Pulmonology"],
    "clinical_questions": [
        "Describe onset and character of chest pain?",
        "Any known allergies?"
    ]
}

sample_responses = {
    "What is your pain level?": "The pain is moderate and worsens with exertion.",
    "Do you have any allergies?": "No known allergies."
}

# Models
class LoginRequest(BaseModel):
    student_name: str
    email: str
    password: str

class ChatRequest(BaseModel):
    student_id: int
    case_id: int
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/login")
def login(data: LoginRequest):
    # Prototype login: accept any input and return success
    return {"message": f"Welcome {data.student_name}!", "status": "success"}

@app.get("/case/{case_id}")
def get_case(case_id: int):
    # Return example case data regardless of ID
    return sample_case

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Return predefined response or default message
    reply = sample_responses.get(request.message, "Please ask another question about your condition.")
    return ChatResponse(response=reply)

@app.get("/feedback/{student_id}")
def get_feedback(student_id: int):
    # Return dummy progress and tips data
    return {
        "mastery_score": 75,
        "stress_level": "Medium",
        "learning_tips": [
            "Review cardiology module.",
            "Focus on symptom assessment techniques."
        ]
    }
