from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Notification Microservice",
    description="A standalone service for handling emails and alerts.",
    version="1.0.0"
)

# Schema for the incoming data
class EmailRequest(BaseModel):
    student_email: str
    course_id: int

@app.post("/api/v1/notify/")
async def send_email_notification(request: EmailRequest):
    # In a real app, this would connect to an SMTP server (like SendGrid or AWS SES)
    print("\n" + "="*50)
    print(f"📧 [MICROSERVICE ACTIVATED]")
    print(f"📧 Sending Welcome Email to: {request.student_email}")
    print(f"📧 Enrolled in Course ID: {request.course_id}")
    print("="*50 + "\n")
    
    return {"status": "success", "message": "Email sent to student"}