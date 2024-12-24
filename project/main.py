
from fastapi import FastAPI

app = FastAPI()

students = [
    {
        'name': 'Eslam',
        'age': 28,
    },
    {
        'name': 'Ahmed',
        'age': 22,
    },
    {
        'name': 'Aya',
        'age': 26,
    },
    {
        'name': 'Nour',
        'age': 16,
    },
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/students')
def get_all_students():
    return students

@app.get('/student/{id}')
def get_student_by_id(id:int):
    
    if id < 0 or id >= len(students):
        return {
            'message': f'Student with id {id} not found',
            'students': students,
        }, 404
    
    return students[id]


@app.delete('/student/{id}')
def delete_student_by_id(id: int):
    if id < 0 or id >= len(students): 
        return {
            'message': f'Student with id {id} not found',
            'students': students,
        }, 404
    
    student = students.pop(id)  
    return {
        'message': f'Student {student["name"]} is deleted',
        'students': students,
    }

@app.post('/student/create')
def create_student(student:dict):
    students.append(student)
    return {
        'message' : " student added",
        'Students' : students
    }
    
    
@app.post('/student/update')
def update_student(id:int,student:dict):
    student_info = students[id]
    student_info['name'] = student['name']
    return {
        'message' : " student updated ",
        'Students' : students
    }