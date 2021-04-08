from flask import Flask, redirect, url_for, render_template, request, jsonify, send_from_directory
import numpy as np
import os

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['JSON_SORT_KEYS'] = False


@app.route("/")
def home():
        return render_template("index.html")

@app.route("/files", methods=['GET'])
def get_thesis():
    '''
    Returns the file that is passed via the argument 'filename'
    '''
    print('Requesting file')
    if 'filename' in request.args:
        workingdir = os.path.abspath(os.getcwd())
        filepath = workingdir + '/static/files/'
        return send_from_directory(filepath, request.args['filename'])
    else:
        return 'File not found'

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == "__main__":
        app.run(host='127.0.0.1')
        

