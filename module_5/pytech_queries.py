# Brittany Normandin, CSD 310, 11/17/2021
# Module 5.3 Assignment: PyTech: Collection Queries

from pymongo import MongoClient

uri="mongodb+srv://admin:admin@cluster0.9s1rm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# connect to MongoDB
client = MongoClient(uri,  tls=True, tlsAllowInvalidCertificates=True)

# Database and students list
db = client.pytech
students = db.students
student_list = students.find({})

# Collection Loop
print("-- Display Student Documents find() [all students] --")
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + " \n First name: " + doc["first_name"] + " \n Last name: " + doc["last_name"])
# Find Student
print("Finding documents for find_one() [single student]")
richard = students.find_one({"student_id": "1009"})
print(" \n Student ID: " + doc["student_id"] + " \n First name: " + doc["first_name"] + " \n Last name: " + doc["last_name"])
