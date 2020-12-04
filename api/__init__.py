from flask import Flask
import os
import markdown
app = Flask(__name__)

@app.route("/")
def index():
    # with open(os.path.dirname(app.root_path) +'\README.md', 'r') as file:
    #     content = file.read()
    #     return markdown.markdown(content)
    return 'Hello World'

@app.route("/add")
def index():
    # with open(os.path.dirname(app.root_path) +'\README.md', 'r') as file:
    #     content = file.read()
    #     return markdown.markdown(content)
    return 'add Hello World'