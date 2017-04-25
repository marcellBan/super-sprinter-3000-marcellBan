from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)


@app.route('/')
@app.route('/list')
def list_stories():
    # pass data
    return render_template('list.html')


@app.route('/story', methods=['GET', 'POST'])
def add_story():
    if request.method == 'GET':
        story = {
            "title": "",
            "description": "",
            "accept": "",
            "business_value": 1000,
            "estimation": 2.5,
            "status": {
                "Planning": True,
                "TODO": False,
                "In Progress": False,
                "Review": False,
                "Done": False
            }
        }
        # return empty form
        return render_template('form.html', edit=False, story=story)
    elif request.method == 'POST':
        # save data
        return 'not really sure where to go here'


@app.route('/story/<int:story_id>', methods=['GET', 'POST', 'DELETE'])
def modify_story(story_id):
    if request.method == 'GET':
        story = {
            "title": "hi",
            "description": "test",
            "accept": "whyyyy",
            "business_value": 300,
            "estimation": 4.5,
            "status": {
                "Planning": False,
                "TODO": False,
                "In Progress": True,
                "Review": False,
                "Done": False
            }
        }
        # return data
        return render_template('form.html', edit=True, story=story)
    # FIXME: should this use PUT?
    elif request.method == 'POST':
        # update data
        return 'not really sure where to go here'
    elif request.method == 'DELETE':
        # delete story
        return 'not really sure where to go here'

if __name__ == '__main__':
    app.run(debug=True)
