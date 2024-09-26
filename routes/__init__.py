from flask import Flask

app = Flask(__name__)

from .labworks import labworks
from .square import square
from .tourist import tourist