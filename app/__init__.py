from flask import Flask

app = Flask(__name__)

# Import routes setelah inisialisasi app
from app import routes
