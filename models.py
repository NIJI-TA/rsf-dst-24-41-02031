from datetime import datetime, timezone
from app import db
from werkzeug.security import generate_password_hash, check_password_hash # Пока используем библиотеку для хэширования, позже, позможно, напишем свой модуль для хэширования паролей и других данных, если потребуется



class User(db.Model):
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
 
 
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    file_body = db.Column(db.String(140)) # Потом заменим на file_path = db.Column(db.String(255), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), index=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # user — это имя таблицы базы данных, которую Flask-SQLAlchemy автоматически устанавливает как имя класса модели, преобразованного в нижний регистр
    
    
    def __repr__(self):
        return '<Post {}>'.format(self.title)
    
    