import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages)
    
    # Configure the MongoDB connection
    client = MongoClient(os.environ.get("MONGO_URI"))
    
    # Use the specified database name from the environment variable
    db_name = os.environ.get("DB_NAME")
    if not db_name:
        raise ValueError("DB_NAME environment variable is not set")

    app.db = client[db_name]  # Access the database by name

    return app

# Create an instance of the app
app = create_app()

# Ensure the Flask app runs when the script is executed
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
