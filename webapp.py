#!/usr/bin/python3
import projects_class
import storage
import uuid
from flask import Flask, render_template, url_for, jsonify, request, abort
from flask_cors import CORS

'''
Create flask instance and apply CORS
'''
app = Flask(__name__)
CORS(app)

'''
Disable strict slashes for all routes
'''
app.url_map.strict_slashes = False

@app.route('/')
def main_page():
    '''
    serves main page
    '''
    return render_template('index.html', cache_id=uuid.uuid4())

@app.route('/api/project/all', methods=['GET'])
def all_projects():
    '''
    GET route to return JSON of 
    '''
    my_dict = {}
    project_list = storage.storage_instance.grab_all()
    for project in project_list:
        my_dict['{}'.format(project.project_id)] = project.to_dict()
    return jsonify(my_dict)

@app.teardown_appcontext
def teardown_db(exception):
    """
    A teardown function that is to be called after each request
    """
    storage.storage_instance.close()


@app.errorhandler(404)
def not_found_error(error):
    """
    404 gif page
    """
    return render_template('404.html', cache_id=uuid.uuid4())