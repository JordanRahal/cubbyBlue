from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Cubs Fan'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Anthony Rizzo'}, 
            'body': 'Hey Chicago whaddaya say' 
        },
        { 
            'author': {'nickname': 'Joe Maddon'}, 
            'body': 'Cubs are gonna win today!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)