from app import app, db
from app import login # Необходимо для пользовательского загрузчика

from time import time
import jwt
from flask_login import UserMixin # mixin класс который реализует некоторые необходимые элементы для нашего класса User
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash # Пока используем библиотеку для хэширования, позже, позможно, напишем свой модуль для хэширования паролей и других данных, если потребуется


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic') # На более высоком уровне (то есть в самой БД этого видно не будет) также создается поле author для объекта класса Post (можно, например, вызвать post.author для некоторой post)

    # При вызове User.query.get('user.id') --> <User user.username>
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    # Устанавливаем пароль пользователю
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
      
    # Проверка пароля    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in}, app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)
      
 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    file_body = db.Column(db.String(140)) # Потом заменим на file_path = db.Column(db.String(255), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), index=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # user — это имя таблицы базы данных, которую Flask-SQLAlchemy автоматически устанавливает как имя класса модели, преобразованного в нижний регистр

    def __repr__(self):
        return '<Post {}>'.format(self.title)
    

# Регистрируем пользовательский загрузчик с помощью декоратора:
@login.user_loader
def load_user(id):
    return User.query.get(int(id)) # Идентификатор, который от flask-login передается в функцию является строкой, поэтому для нашей БД эту строку нужно перевести в целое число
    
    