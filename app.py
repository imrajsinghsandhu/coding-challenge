import logging
import socket
from flask import request
from routes import app  # Importing the app from the routes folder

logger = logging.getLogger(__name__)

@app.route('/', methods=['GET'])
def default_route():
    logging.info("Starting application ...")
    return 'Python Template'

# Configure logger formatting
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Main entry point
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    port = sock.getsockname()[1]
    sock.close()
    app.run(port=port)
