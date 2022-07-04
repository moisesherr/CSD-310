from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.m44qnlx.mongodb.net/?retryWrites=true&w=majority&ssl=true"
client = MongoClient(url, tls=True, tlsAllowInvalidCertificates=True)
db = client.pytech
print(db.list_collection_names())