
from flask import Flask, url_for, render_template, request
from flask_admin import Admin
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# Add administrative views here

if __name__ == '__main__':
    app.run(debug=True)