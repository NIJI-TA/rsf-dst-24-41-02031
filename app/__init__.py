from flask import Flask

from config import Config # Берем нашу конфигурацию как класс из файла config.py 

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail


# Создание объекта-приложения как экземпляра класса Flask из пакета flask, и настройка конфигурации
app = Flask(__name__)
app.config.from_object(Config)

# Инициализация расширения LoginManager
login = LoginManager(app)

# Базы данных и миграции
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Создание экземпляра объекта класса Mail
mail = Mail(app)


from app import routes