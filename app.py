import logging
import socket

from routes import app

logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def default_route():
    logging.info("Starting application ...")
    print("GYATTTT requesttt")
    return 'Python Template'


logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    port = sock.getsockname()[1]
    sock.close()
    app.run(port=port)
