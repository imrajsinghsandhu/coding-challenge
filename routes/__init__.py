from flask import Flask
from routes.tourist import tourist_bp  # Import the tourist blueprint

# Initialize the Flask app
app = Flask(__name__)

# Register the tourist blueprint
app.register_blueprint(tourist_bp)
