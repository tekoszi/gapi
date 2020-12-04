from flask import Flask
import os
import markdown
app = Flask(__name__)


@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) +'/README.md', 'r') as file:
        content = file.read()
        return markdown.markdown(content)


@app.route("/create")
def create():
    # with open(os.path.dirname(app.root_path) +'\README.md', 'r') as file:
    #     content = file.read()
    #     return markdown.markdown(content)
    return 'add Hello World'


@app.route("/read")
def read():
    # with open(os.path.dirname(app.root_path) +'\README.md', 'r') as file:
    #     content = file.read()
    #     return markdown.markdown(content)
    return 'add Hello World'

@app.route("/update")
def update():
    # with open(os.path.dirname(app.root_path) +'\README.md', 'r') as file:
    #     content = file.read()
    #     return markdown.markdown(content)
    return 'add Hello World'


@app.route("/delete")
def delete():
    # with open(os.path.dirname(app.root_path) +'\README.md', 'r') as file:
    #     content = file.read()
    #     return markdown.markdown(content)
    return 'add Hello World'