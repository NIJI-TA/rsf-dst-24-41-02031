from app.models import User

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email


class LoginForm(FlaskForm):
    username = StringField('Имя', render_kw={"class": "custom-input", "placeholder": "Введите имя"}, validators=[DataRequired()])
    password = PasswordField('Пароль', render_kw={"class": "custom-input", "placeholder": "Введите пароль"}, validators=[DataRequired()])
    remember_me = BooleanField('Запомнить', render_kw={"class": "custom-checkbox"})
    submit = SubmitField('Вход', render_kw={'class': 'login-btn'})
    

class RegistrationForm(FlaskForm):
    username = StringField('Имя', render_kw={"class": "custom-input", "placeholder": "Введите имя"}, validators=[DataRequired()])
    email = StringField('Почта', render_kw={"class": "custom-input", "placeholder": "Введите email"}, validators=[DataRequired(), Email(message='Неверный формат почты')])
    password = PasswordField('Пароль', render_kw={"class": "custom-input", "placeholder": "Придумайте пароль"}, validators=[DataRequired()])
    password2 = PasswordField('Повтор пароля', render_kw={"class": "custom-input", "placeholder": "Повторите пароль"}, validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться', render_kw={'class': 'login-btn'})

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Это имя пользователя уже используется')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Пользователь с такой почтой уже зарегистрирован')
        

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Почта', render_kw={"class": "custom-input", "placeholder": "Введите email"}, validators=[DataRequired(), Email(message='Неверный формат почты')])
    submit = SubmitField('Зпросить сброс пароля', render_kw={'class': 'login-btn'})
    
    

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Новый пароль', render_kw={"class": "custom-input", "placeholder": "Придумайте новый пароль"}, validators=[DataRequired()])
    password2 = PasswordField('Повтор нового пароля', render_kw={"class": "custom-input", "placeholder": "Повторите пароль"}, validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Сбросить пароль', render_kw={'class': 'login-btn'})