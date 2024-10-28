from flask import Flask, request, render_template, g
import sqlite3

app = Flask(__name__)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('users.db')
    return g.db

@app.teardown_appcontext
def close_db(error):
    if 'db' in g:
        g.db.close()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cur = get_db().execute(query)
    user = cur.fetchone()

    if user:
        return f"Welcome, {username}! Flag: CTF{{YOU_ARE_SO_GREAT}}"
    
    return "Invalid credentials!"

if __name__ == '__main__':
    app.run(debug=True)
