# Dependencies
from flask import Flask, render_template, jsonify, request

# Define the application and port
# Flask accepts a static folder parameter in which the static js and css is located
# You can refer to it using the static_url_path parameter which is the href
# used in templates, e.g. static_url_path = '/app' can be referred to as /app/main.js
app = Flask(__name__, static_folder='app', static_url_path='/app')
port = 8000

# Define a route which will capture all routes and link them back to index
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def index(path):

    # Return the index page. By default, Flask will look into a /templates folder
    return render_template('index.html')

# When this script is run directly, start the flask application
if __name__ == "__main__":
    app.run(port=port)
