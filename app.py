import logging
import socket
from flask import Flask, request
from routes.tourist import tourist_bp  # Import the tourist blueprint

# Create the Flask app here in app.py
app = Flask(__name__)

# Set up logging
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET'])
def default_route():
    logger.info("Starting application ...")
    return 'Python Template'

# Configure logger formatting
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Register the blueprint from tourist.py
app.register_blueprint(tourist_bp)

# Main entry point
if __name__ == "__main__":
    # Bind to an available port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    port = sock.getsockname()[1]
    sock.close()
    
    # Start the Flask application
    app.run(port=port)
