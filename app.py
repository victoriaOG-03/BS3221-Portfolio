import os
from dotenv import load_dotenv
from flask import Flask
from pymongo import MongoClient

# Access to MongoDB Atlas Cluster
load_dotenv()
connection_string = os.environ.get("CONNECTION_STRING")
mongo_client = MongoClient(connection_string)

# Adding in the database and collections
database = mongo_client.get_database("bookshelf")
collection = database.get_collection("books")

# Inserting a book document
book = {"book": "Harry Potter", "pages": 800}
collection.insert_one(book)

# Instantiating new Flask app object
app = Flask(__name__)

# Route to the initial form page
@app.route('/')
def index():
    return "Hello!"

if __name__ == "__main__":
    app.run(debug=True)
