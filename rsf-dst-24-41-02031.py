from app import app



# Настройка Flask Shell (для автоматической загрузки контекста приложения)
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}