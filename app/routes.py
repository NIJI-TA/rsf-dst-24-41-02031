from app import app

from app import db
from app.forms import LoginForm, RegistrationForm # Берем наши формы как поля классов в файле forms
from app.models import User, Post

from flask import url_for, render_template, flash, request, redirect
from flask_login import current_user, login_user, logout_user


# Routes
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm() # Берем данные полученные из формы
    if form.validate_on_submit(): # Если все верно
        # Пытаемся найти пользователя (при таком запросе получим либо пользователя из БД, либо None)
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неправильное имя пользователя или пароль')
            return redirect(url_for('login')) # Повторно загружаем страницу авторизации
        login_user(user, form.remember_me.data) # Регистрируем пользователя с помощью функции из flask-login
        return redirect(url_for('index')) # Переходим на главную страницу
    
    return render_template('login.html', title='Вход', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегистрированы!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация', form=form)