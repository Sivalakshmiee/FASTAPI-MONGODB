from pymongo import MongoClient

connection_string = "mongodb+srv://sivalakshmie2002:SOhXVxzHl8mXCX9p@project-cluster.t95v6qd.mongodb.net/?retryWrites=true&w=majority&appName=Project-cluster"


client = MongoClient(connection_string)

db = client.get_database('Product')

print(db)

collection = db.get_collection('Product')