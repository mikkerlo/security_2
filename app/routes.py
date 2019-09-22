from app import app
from flask import request, render_template
import sqlite3


class User(object):
    def __init__(self, id_, login):
        self.id = id_
        self.login = login


@app.route('/')
def index():
    return render_template('main.jinja2')


@app.route('/users')
def users():
    conn = sqlite3.connect('main.db')
    data_cursor = conn.execute("SELECT id, login FROM users WHERE status=TRUE;").fetchall()
    user_data = [User(*i) for i in data_cursor]
    conn.close()
    return render_template('active_users.jinja2', users=user_data)


@app.route('/by-login')
def by_login():
    login = request.args.get('login')
    user_data = None
    if login is not None:
        conn = sqlite3.connect('main.db')
        data_cursor = conn.execute("SELECT id, login FROM users WHERE login = ?;", (login,)).fetchall()
        user_data = [User(*i) for i in data_cursor]
        conn.close()
    return render_template('by_login.jinja2', login=login, users=user_data)


@app.route('/by-id')
def by_id():
    id_ = request.args.get('id')
    user_data = None
    if id_ is not None:
        conn = sqlite3.connect('main.db')
        data_cursor = conn.execute("SELECT id, login FROM users WHERE id = ?;", (id_,)).fetchall()
        user_data = [User(*i) for i in data_cursor]
        conn.close()
    return render_template('by_id.jinja2', id_=id_, users=user_data)
