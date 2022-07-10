from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.m44qnlx.mongodb.net/?retryWrites=true&w=majority&ssl=true"
client = MongoClient(url, tls=True, tlsAllowInvalidCertificates=True)
db = client.pytech
docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
	print(f"Student ID: {doc['student_id']}")
	print(f"First Name: {doc['first_name']}")
	print(f"Last Name: {doc['last_name']}")
	print()

result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Mouse"}})
result = db.students.update_one({"student_id": "1008"}, {"$set": {"last_name": "Cat"}})
result = db.students.update_one({"student_id": "1009"}, {"$set": {"last_name": "Dog"}})

print("-- DISPLAYING UPDATED STUDENT DOCUMENT FROM find_one() QUERY --")
doc = db.students.find_one({"student_id": "1007"})

print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")
print()
