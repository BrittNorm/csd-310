# Brittany Normandin, CSD 310, 11/17/2021
# Module 6.3 Assignment Pytech: Deleting Documents

# Import MongoDB information
from pymongo import MongoClient
uri="mongodb+srv://admin:admin@cluster0.9s1rm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# connect to MongoDB
client = MongoClient(uri,  tls=True, tlsAllowInvalidCertificates=True)

# Pytech database and students
db = client.pytech
students = db.students

# Finding the collection of students
student_list = students.find({})
print("-- Displaying Student Information --")

# Loop and output
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + " \n First Name: " + doc["first_name"] + " \n Last name: " + doc["last_name"] + " \n ")

# Document test
test_doc = {
    "student_id": "1010",
    "first_name": "Margret",
    "last_name": "Fisher"
}
# Insert document into MongoDB
test_doc_id = students.insert_one(test_doc).inserted_id

# Printing statements
print(" \n --Insert Statements --")
print(" Student record inserted into students collections with student_id " + str(test_doc_id))

# Using find one method to find student 1010
students_test_doc = students.find_one({"student_id": "1010"})

# Results
print(" \n  -- Display Student Test Document -- ")
print("  Student ID: " + students_test_doc["student_id"] + "\n  First Name: " + students_test_doc["first_name"] + "\n  Last Name: " + students_test_doc["last_name"] + "\n")

# Delete and find all students
delete_student_test_doc = students.find({})
new_students_list = students.find({})

# Display message and loop
print(" \n  -- Displaying Student Documents from find() -- ")
for doc in new_students_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit program
input(" \n\n Press any key to end program")
