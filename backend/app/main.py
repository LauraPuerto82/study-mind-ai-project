from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="StudyMind API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/hello/student")
def hello_student():
    return {"message": "Hello, student! 🎓 Let's study together."}


@app.get("/api/v1/hello/parent")
def hello_parent():
    return {"message": "Hello, parent! 👋 Welcome to StudyMind."}
