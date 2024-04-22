import bson
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import requests
import json
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from werkzeug.urls import url_quote_plus  # Importing the correct function


app = Flask(__name__)

# Global variable to store pet data
pets_data = [
    {'name': 'Buddy', 'breed': 'Labrador Retriever', 'age': 3},
    {'name': 'Max', 'breed': 'German Shepherd', 'age': 5},

]

walker_data = [
    {'name': 'Jack Fox', 'experience': '10 years', 'rating': 'High', 'location': 'london'},
    {'name': 'Lucy May', 'experience': '5 years', 'rating': 'Low', 'location': 'manchester'},
    {'name': 'Joe Buchanan', 'experience': '7 years', 'rating': 'Medium', 'location': 'birmingham'},
    {'name': 'Lily Rose', 'experience': '15 years', 'rating': 'High', 'location': 'wales'},

]


# Load environment variables from .env file
load_dotenv()

# MongoDB connection string
mongo_uri = os.getenv("CONNECTION_STRING")

# MongoDB API key
api_key = os.getenv("MONGODB_API_KEY")

# Connect to MongoDB
client = MongoClient(mongo_uri)

# Access the database
db = client['woof_walk']

# Access the collection
collection = db['pets']

# Define route handler function to fetch pets data from MongoDB API
@app.route('/get_pets', methods=['GET'])
def get_pets():
    # MongoDB API endpoint URL
    url = "https://eu-west-2.aws.data.mongodb-api.com/app/data-xpfztyu/endpoint/data/v1/action/findOne"
    
    # Payload for the API request
    payload = json.dumps({
        "collection": "pets",
        "database": "woof_walk",
        "dataSource": "Waqq--ly",
        "projection": {
            "_id": 1
        }
    })
    
    # Headers for the API request
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': os.environ.get('MONGODB_API_KEY')  # Use environment variable for API key
    }
    
    # Send POST request to MongoDB API
    response = requests.post(url, headers=headers, data=payload)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch pets data'}), 500

# Route for the initial form page
@app.route('/')
def index():
    return render_template('index.html')

# Route for Register Dog page
@app.route('/register_dog', methods=['GET', 'POST'])
def register_dog():
    if request.method == 'POST':
        # Fetch form data
        name = request.form['name']
        breed = request.form['breed']
        age = request.form['age']
        # Add pet data to the global list
        pets_data.append({'name': name, 'breed': breed, 'age': age})
        return render_template('Pages/registerdog.html', message="Dog registered successfully!")
    return render_template('Pages/registerdog.html')



# Route for search dogs page
@app.route('/search_dog')
def search_dog():
    # Render the search dog page with all registered dogs
    return render_template('Pages/searchdog.html', results=pets_data)

@app.route('/register_dog_walker', methods=['GET', 'POST'])
def register_dog_walker():
    if request.method == 'POST':
        # Fetch form data
        name = request.form['name']
        experience = request.form['experience']
        rating = request.form['rating']
        location = request.form['location']
        # Add dog walker data to the global list
        walker_data.append({'name': name, 'experience': experience, 'rating': rating, 'location': location})
        return render_template('Pages/registerdogwalker.html', message="Dog walker registered successfully!")
    return render_template('Pages/registerdogwalker.html')


@app.route('/search_dog_walker')
def search_dog_walker():
    # Render the search dog walker page with all registered dog walkers
    return render_template('Pages/searchdogwalker.html', results=walker_data)


if __name__ == '__main__':
    app.run(debug=True)