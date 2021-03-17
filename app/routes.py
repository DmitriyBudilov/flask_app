from flask import make_response, redirect, render_template
from app import app

@app.route('/set-cookie')
def set_cookie():
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "skyblue", 60*60)
    res.set_cookie("favorite-font", "san-serif", 60*60)
    return res

@app.route('/user/<int:id>')
def user_profile(id):
    return f'Profile page of user {id}'

@app.route('/books/<string:ganre>')
def books(ganre):
    res = make_response(f'All Books in {ganre} category')
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

@app.route('/')
def render_markdown():
    return "## Heading", 200, {'Content-Type': 'text/markdown'}

@app.route('/transfer/')
def transfer():
    return redirect("http://localhost:5000/login", code=301)

@app.route('/login/')
def login():
    return "<h2>Login</h2>"