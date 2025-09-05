from fastapi import FastAPI, Path, HTTPException, Query
import json 
from fastapi.responses import HTMLResponse

# Create FastAPI instance
app = FastAPI(title="Student Data API")


# Helper function to load student data from JSON file

def load_data():
    with open('Task2/students.json', 'r') as s:
        data = json.load(s)
    return data


# Root endpoint - returns HTML welcome page

@app.get("/", response_class=HTMLResponse)
def intro():
    return """
    <h2>Welcome to the Student Information API</h2>
    <p>
        This service is designed to provide basic student details,
    </p>
    <p>
        Use the <code>/view</code> endpoint to retrieve a student's information.
    </p>
    """


# Endpoint: View all students

@app.get("/view")
def view_students():
    data = load_data()
    return data 


# Endpoint: Fetch student by ID

@app.get("/student/{id}")
def get_specific_record(id: str = Path(..., description="ID of the student")):
    data = load_data()
    students = data["students"] 
    
    # Search through list of students
    for student in students:
        if student["id"].lower() == id.lower():  # case-insensitive match
            return student
    
    # If no match found, return 404 error
    raise HTTPException(status_code=404, detail="Student not found")


# Endpoint: Sort students by CGPA (ascending/descending)

@app.get("/sorting")
def sorting(
    sortby: str = Query(..., description="Sort on the basis of CGPA"), 
    orderby: str = Query('asc', description="Choose between asc and desc")
):
    # Validate sort field (only CGPA is allowed for now)
    if sortby.lower() != "cgpa":
        raise HTTPException(status_code=400, detail='Choose the right field for sorting')

    # Validate order direction
    if orderby not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail='Choose between asc and desc')

    data = load_data()

    # Perform sorting based on CGPA and order
    if orderby == 'desc':
        return sorted(data["students"], key=lambda x: x["CGPA"], reverse=True)
    
    return sorted(data["students"], key=lambda x: x["CGPA"], reverse=False)
