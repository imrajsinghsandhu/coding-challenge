from flask import Flask

app = Flask(__name__)

import routes.labworks
import routes.square
import routes.tourist