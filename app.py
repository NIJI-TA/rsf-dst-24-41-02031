from flask import Flask, g, url_for, render_template, flash, request, redirect
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
from FDataBase import FDataBase 
from forms import LoginForm


# Конфигурация
DATABASE = '/tmp/app.db'
DEBUG = True
SECRET_KEY = 'sdlfhh5jhhj241jh25g1hk41gjk4'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'app.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    """Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    """Соединение с БД, если оно еще не установлено"""
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с БДб если оно было установлено"""
    if hasattr(g, 'link_db'):
        g.link_db.close()


dbase = None


@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@app.route("/")
def landing():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user')
        return redirect(url_for('landing'))
    return render_template('login.html', title='Вход', form=form)


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        hash = generate_password_hash(request.form['password'])
        res = dbase.addUser(request.form['username'], request.form['email'], hash)
        if res:
            flash("Вы успешно зарегистрированы", category="success")
            return redirect(url_for('login'))
        else:
            flash("Ошибка при добавлении в БД", category="error")

    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)

