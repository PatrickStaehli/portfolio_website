from flask import Flask, redirect, url_for, render_template, request, jsonify
import numpy as np

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['JSON_SORT_KEYS'] = False


@app.route("/")
def home():
        return render_template("index.html")

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == "__main__":
        app.run(debug=True)
        

