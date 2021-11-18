# Brittany Normandin, CSD 310, 11/17/2021
# Module 5.3 Assignment: PyTech: Collection Queries

from pymongo import MongoClient

uri="mongodb+srv://admin:admin@cluster0.9s1rm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# connect to MongoDB

client = MongoClient(uri,  tls=True, tlsAllowInvalidCertificates=True)

db = client.pytech

# Student 1 documents
sean = {
    "first_name": "Sean",
    "last_name": "Murphy",
    "student_id": "1007",
    "enrollments": [
        {
            "term": "Second",
            "start_date": "August 9th, 2021",
            "end_date": "October 11th, 2021",
            "gpa": "3.6",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development",
                    "instructor": "Professor Shelansky",
                    "grade": "A"
                },
                {
                    "course_id": "CSD320",
                    "description": "Java programming",
                    "instructor": "Professor Payne",
                    "grade": "B-"
                }
            ]
        }
    ]
}
# Student 2 documents
tamara = {
    "first_name": "Tamara",
    "last_name": "Furby",
    "student_id": "1008",
    "enrollments": [
        {
            "term": "Second",
            "start_date": "August 9th, 2021",
            "end_date": "October 11th, 2021",
            "gpa": "3.4",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development",
                    "instructor": "Professor Shelansky",
                    "grade": "B"
                },
                {
                    "course_id": "CSD320",
                    "description": "Java programming",
                    "instructor": "Professor Payne",
                    "grade": "C+"
                }
            ]
        }
    ]
}
#Student 3 documents
richard = {
    "first_name": "Richard",
    "last_name": "Rowe",
    "student_id": "1009",
    "enrollments": [
        {
            "term": "Second",
            "start_date": "August 9th, 2021",
            "end_date": "October 11th, 2021",
            "gpa": "3.9",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development",
                    "instructor": "Professor Shelansky",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Java programming",
                    "instructor": "Professor Payne",
                    "grade": "A-"
                }
            ]
        }
    ]
}   
# Collection of students
students = db.students
print("--Insert Student Records---")

sean_student_id = students.insert_one(sean).inserted_id
print(" Student record Sean Murphy id added to students collection " + str(sean_student_id))
tamara_student_id = students.insert_one(tamara).inserted_id
print(" Student record Tamara Furby id added to students collection " + str(tamara_student_id))
richard_student_id = students.insert_one(richard).inserted_id
print(" Student record Richard Rowe id added to students collection " + str(richard_student_id))