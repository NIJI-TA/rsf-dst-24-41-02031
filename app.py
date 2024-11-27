from flask import Flask, url_for, render_template, flash, request, redirect
from forms import LoginForm # Берем наши формы как поля классов в файле forms
from config import Config # Берем нашу конфигурацию как класс из файла config.py 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user, login_user, logout_user


# Создание объекта-приложения как экземпляра класса Flask из пакета flask, и настройка конфигурации
app = Flask(__name__)
app.config.from_object(Config)

# Инициализация расширения LoginManager
login = LoginManager(app)

# Базы данных и миграции
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models # Импортируем модели для наших БД


# Настройка Flask Shell (для автоматической загрузки контекста приложения)
from app import app, db
from models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}



# Routes
@app.route("/")
def landing():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('landing'))
    
    form = LoginForm() # Берем данные полученные из формы
    if form.validate_on_submit(): # Если все верно
        # Пытаемся найти пользователя (при таком запросе получим либо пользователя из БД, либо None)
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or user.check_password(form.password.data):
            flash('Неправильное имя пользователя или пароль')
            return redirect(url_for('login')) # Повторно загружаем страницу авторизации
        login_user(user, form.remember_me.data) # Регистрируем пользователя с помощью функции из flask-login
        return redirect(url_for('landing')) # Переходим на главную страницу
    
    return render_template('login.html', title='Вход', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('landing'))



@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        pass
    return render_template('register.html')



if __name__ == "__main__":
    app.run(debug=True)

