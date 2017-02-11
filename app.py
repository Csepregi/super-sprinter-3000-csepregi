from flask import Flask, render_template, request, redirect, url_for
from models import *
from build import *


app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request():
    #create db if needed and connect
    build_tables()

@app.teardown_request
def teardown_request(exception):
    #close the db connection
    db.close()


@app.route("/", methods=["GET", "POST"])
def list_stories():
    stories = UserStoryManager.select()
    return render_template("list.html", stories=stories)



if __name__ == "__main__":
    app.run(debug=True)
