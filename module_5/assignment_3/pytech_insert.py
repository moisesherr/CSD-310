from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.m44qnlx.mongodb.net/?retryWrites=true&w=majority&ssl=true"
client = MongoClient(url, tls=True, tlsAllowInvalidCertificates=True)
db = client.pytech
student1 = {"student_id": "1007", "first_name": "Jack", "last_name": "Smith"}
student2 = {"student_id": "1008", "first_name": "Susie", "last_name": "Apples"}
student3 = {"student_id": "1009", "first_name": "Rick", "last_name": "Max"}
student1_id = db.students.insert_one(student1).inserted_id
student2_id = db.students.insert_one(student2).inserted_id
student3_id = db.students.insert_one(student3).inserted_id
print(f"Inserted student record {student1['first_name']} {student1['last_name']} into the students collection with document_id {student1_id}")
print(f"Inserted student record {student2['first_name']} {student2['last_name']} into the students collection with document_id {student2_id}")
print(f"Inserted student record {student3['first_name']} {student3['last_name']} into the students collection with document_id {student3_id}")
