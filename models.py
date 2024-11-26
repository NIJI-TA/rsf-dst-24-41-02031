from datetime import datetime, timezone
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    file_body = db.Column(db.String(140)) # Потом заменим на file_path = db.Column(db.String(255), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), index=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # user — это имя таблицы базы данных, которую Flask-SQLAlchemy автоматически устанавливает как имя класса модели, преобразованного в нижний регистр
    
    def __repr__(self):
        return '<Post {}>'.format(self.title)
    
    