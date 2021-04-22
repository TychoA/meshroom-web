# Include our application
from app import app
from flask import render_template, flash, request, redirect, url_for
from os import path
from werkzeug.utils import secure_filename

# Define a route which will capture all routes and link them back to index
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def index(path):

    # Return the index page. By default, Flask will look into a /templates folder
    return render_template('index.html')

# Define upload behavior
UPLOAD_FOLDER = path.join('model', 'input')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define a route which the client can post images to, note that after each meshroom process
# these images will be deleted
@app.route('/upload', methods=['POST'])
def upload():

    # check if the post request has the file part
    if 'input' not in request.files:
        flash('No file part')
        raise Exception("files could not be uploaded")

    # Iterate over all the files
    for file in request.files.getlist('input'):

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            raise Exception("file could not be uploaded")

        if file and 'image' in file.mimetype:
            filename = secure_filename(file.filename)
            file.save(path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            raise Exception("file could not be uploaded")

    # Everything has been uploaded
    return {}