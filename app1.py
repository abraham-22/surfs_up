#  import the Flask dependency
from flask import Flask

# Create a New Flask App Instance using Dunder
app = Flask(__name__)

# Create Flask Routes and function.
@app.route('/')
def hello_world():
    return 'Hello world'
