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
	print(f"Document ID: {doc['_id']}")
	print()

result = db.students.delete_one({'student_id': 1010})

print("-- DISPLAYING DELETED STUDENTS DOCUMENTS FROM find() QUERY --")

docs = db.students.find({})
for doc in docs:
	print(f"Student ID: {doc['student_id']}")
	print(f"First Name: {doc['first_name']}")
	print(f"Last Name: {doc['last_name']}")
	print(f"Document ID: {doc['_id']}")
	print()

##result = db.students.insert_one({'student_id': 1010, 'first_name':"Rick", 'last_name': "Deckard"})
