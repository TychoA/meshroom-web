# Include our application
from app import app
from flask import render_template

# Define a route which will capture all routes and link them back to index
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def index(path):

    # Return the index page. By default, Flask will look into a /templates folder
    return render_template('index.html')
