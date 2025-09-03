from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Student Information API")

@app.get("/", response_class=HTMLResponse)
def intro():
    return """
    <h2>Welcome to the Student Information API!</h2>
    <p>
        This service is designed to provide basic student details,
        including their <b>Name</b>, <b>ID</b>, and <b>Field of Study</b>.
    </p>
    <p>
        Use the <code>/student</code> endpoint to retrieve a student's information.
    </p>
    """

@app.get("/student")
def student():
    return {
        "Name": "Shameer Sajjad Ahmed",
        "ID": "F2023266578",
        "Field of Study": "Computer Science"
    }
