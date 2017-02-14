from flask import Flask, render_template, request, redirect, url_for, flash
from models import *
from build import *


app = Flask(__name__)
app.config.from_object(__name__)
'''
@app.before_request
def before_request():
    #create db if needed and connect
    build_tables()

@app.teardown_request
def teardown_request(exception):
    #close the db connection
    db.close()
'''

@app.route("/", methods=["GET", "POST"])
def list_stories():
    stories = UserStoryManager.select()
    return render_template("list.html", stories=stories)

"""
@app.route("/story", methods=['GET', 'POST'])
def show_create_story_form():
    return render_template('form.html', stories=UserStoryManager())
"""


@app.route("/story", methods=['GET', 'POST'])
def add_story(new=True):
    if request.method == 'GET':
        return render_template('form.html', new=True)
    else:
        UserStoryManager.create(title=request.form.get('title'),
                                    story=request.form.get('story'),
                                    criteria=request.form.get('criteria'),
                                    business_value=request.form.get('business_value'),
                                    estimation=request.form.get('estimation'),
                                    status=request.form.get('status'))
        return redirect(url_for("list_stories"))


@app.route("/edit/<story_id>", methods=['GET', 'POST'])
def edit_story(story_id, new=False):
    edit = UserStoryManager.select().where(UserStoryManager.id == story_id).get()
    if request.method == 'GET':
        return render_template('form.html',new=False, edit=edit)
    else:
        edit.title = request.form.get("title")
        edit.story = request.form.get("story")
        edit.criteria = request.form.get("criteria")
        edit.business_value = request.form.get("business_value")
        edit.estimation = request.form.get("estimation")
        edit.status = request.form.get("status")
        edit.save()
    return redirect(url_for("list_stories"))


@app.route('/delete/<story_id>', methods=['POST'])
def delete_story(story_id):
    story = UserStoryManager.select().where(UserStoryManager.id == story_id).get()
    story.delete_instance()
    story.save()
    return redirect(url_for('list_stories'))




if __name__ == "__main__":
    app.run(debug=True)
