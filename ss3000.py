'''
Super Sprinter 3000
by night5word (Marcell Bán)
'''

from data_manager import save_data, load_data
from constants import STATUSES
from tools import generate_uniqe_id
from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/list', methods=['GET'])
def list_stories():
    data = sorted(load_data().values(), key=lambda x: x['title'])
    return render_template('list.html', stories=data)


@app.route('/story', methods=['GET', 'POST'])
def add_story():
    if request.method == 'GET':
        base_story = {
            'id': None,
            'title': '',
            'description': '',
            'accept': '',
            'business_value': 1000,
            'estimation': 2.5,
            'status': 'Planning'
        }
        base_status = dict(zip(STATUSES, [x == base_story['status'] for x in STATUSES]))
        # return empty form
        return render_template('form.html', edit=False, story=base_story, status=base_status)
    elif request.method == 'POST':
        data = load_data()
        newuid = generate_uniqe_id(data)
        # add new entry
        data[newuid] = {
            'id': newuid,
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'accept': request.form.get('accept'),
            'business_value': int(request.form.get('business_value')),
            'estimation': float(request.form.get('estimation')),
            'status': request.form.get('status')
        }
        save_data(data)
        # redirect to list page
        return redirect(url_for('list_stories'))


@app.route('/story/<int:story_id>', methods=['GET', 'POST'])
def modify_story(story_id):
    if request.method == 'GET':
        data = load_data()
        if data.get(story_id) is None:
            return redirect(url_for('add_story'))
        status = dict(zip(STATUSES, [x == data[story_id]['status'] for x in STATUSES]))
        return render_template('form.html', edit=True, story=data[story_id], status=status)
    elif request.method == 'POST':
        data = load_data()
        # update entry
        data[story_id] = {
            'id': story_id,
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'accept': request.form.get('accept'),
            'business_value': int(request.form.get('business_value')),
            'estimation': float(request.form.get('estimation')),
            'status': request.form.get('status')
        }
        save_data(data)
        return redirect(url_for('list_stories'))


@app.route('/deletestory/<int:story_id>', methods=['GET'])
def del_story(story_id):
    data = load_data()
    if data.get(story_id) is not None:
        del(data[story_id])
    save_data(data)
    return redirect(url_for('list_stories'))

if __name__ == '__main__':
    app.run(debug=True)
