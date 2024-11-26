from flask import Flask, url_for, render_template, flash, request, redirect
from forms import LoginForm # Берем наши формы как поля классов в файле forms
from config import Config # Берем нашу конфигурацию как класс из файла config.py 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Дополнительные библиотеки
from werkzeug.security import generate_password_hash, check_password_hash # Генерация hash-а для паролей
# from FDataBase import FDataBase # Класс для работы с БД


# Создание объекта-приложения как экземпляра класса Flask из пакета flask, и настройка конфигурации
app = Flask(__name__)
app.config.from_object(Config)

# Базы данных и миграции
db = SQLAlchemy(app)
migrate = Migrate(app, db)


import models # Импортируем модели для наших БД

# def connect_db():
#     conn = sqlite3.connect(app.config['DATABASE'])
#     conn.row_factory = sqlite3.Row
#     return conn


# def create_db():
#     """Вспомогательная функция для создания таблиц БД"""
#     db = connect_db()
#     with app.open_resource('sq_db.sql', mode='r') as f:
#         db.cursor().executescript(f.read())
#     db.commit()
#     db.close()


# def get_db():
#     """Соединение с БД, если оно еще не установлено"""
#     if not hasattr(g, 'link_db'):
#         g.link_db = connect_db()
#     return g.link_db


# @app.teardown_appcontext
# def close_db(error):
#     """Закрываем соединение с БДб если оно было установлено"""
#     if hasattr(g, 'link_db'):
#         g.link_db.close()


# dbase = None


# @app.before_request
# def before_request():
#     """Установление соединения с БД перед выполнением запроса"""
#     global dbase
#     db = get_db()
#     dbase = FDataBase(db)


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

