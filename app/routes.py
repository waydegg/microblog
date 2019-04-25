from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Wayde'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'What a great day outside!'
        },
        {
            'author': {'username': 'Dude'},
            'body': 'Wheres my car?'
        }
    ]


    return render_template('index.html', user=user, posts=posts)
