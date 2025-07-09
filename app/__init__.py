from flask import Flask, request, render_template

# Создание объекта-приложения как экземпляра класса Flask из пакета flask, и настройка конфигурации
application = Flask(__name__)

CORRECTING_MODE = False  # Включить/выключить заглушку


@application.before_request
def check_for():
    if CORRECTING_MODE and not request.path.startswith("/static"):
        return render_template("correcting_page.html"), 503


from app import routes
