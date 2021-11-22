# Brittany Normandin, CSD 310, 11/17/2021
# Module 6.2 Assignment Pytech: Updating Documents

# Import MongoDB information
from pymongo import MongoClient
uri="mongodb+srv://admin:admin@cluster0.9s1rm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# connect to MongoDB
client = MongoClient(uri,  tls=True, tlsAllowInvalidCertificates=True)

# Pytech database and students
db = client.pytech
students = db. students

# Finding the collection of students
student_list = students.find({})
print("-- Displaying Student Information --")

# Loop and output
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + " \n First Name: " + doc["first_name"] + " \n Last name: " + doc["last_name"] + " \n ")

# Update student 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Lopez"}})

# Look for the updated documented student
sean = students.find_one({"student_id": "1007"})

# Message display
print(" \n -- Displaying Student 1007 --")
print(" Student_ID " + sean["student_id"] + " \n First Name: " + sean["first_name"] + " \n Last name: " + sean["last_name"] + " \n ")

# End of program
input(" \n\n Press any key to End Program")
