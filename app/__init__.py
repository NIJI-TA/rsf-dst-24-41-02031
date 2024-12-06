from flask import Flask

from config import Config # Берем нашу конфигурацию как класс из файла config.py 

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail


# Создание объекта-приложения как экземпляра класса Flask из пакета flask, и настройка конфигурации
application = Flask(__name__)
application.config.from_object(Config)

# Инициализация расширения LoginManager
login = LoginManager(application)

# Базы данных и миграции
db = SQLAlchemy(application)
migrate = Migrate(application, db)

# Создание экземпляра объекта класса Mail
mail = Mail(application)


from app import routes