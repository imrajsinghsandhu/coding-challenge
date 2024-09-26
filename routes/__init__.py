from flask import Flask

app = Flask(__name__)

from .square import square
from .tourist import tourist