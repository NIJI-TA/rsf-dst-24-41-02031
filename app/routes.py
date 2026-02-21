from app import application

from flask import render_template


# Routes
@application.route("/")
def index():
    return render_template(
        "index.html",
        title="Методы искусственного интеллекта и магнитоэлектрические эффекты | math-mech-space.ru",
    )


@application.route("/eng")
def index_eng():
    return render_template(
        "index_eng.html",
        title="Methods of artificial intelligence and magneto-electric effects | math-mech-space.ru",
    )


@application.route("/articles")
def articles():
    return render_template("articles.html", title="Статьи | math-mech-space.ru")


@application.route("/articles/eng")
def articles_eng():
    return render_template("articles_eng.html", title="Articles | math-mech-space.ru")


@application.route("/conferences")
def conferences():
    return render_template("conferences.html", title="Конференции | math-mech-space.ru")


@application.route("/conferences/eng")
def conferences_eng():
    return render_template(
        "conferences_eng.html", title="Conferences | math-mech-space.ru"
    )


@application.route("/news")
def news():
    return render_template("news.html", title="Новости | math-mech-space.ru")


@application.route("/news/eng")
def news_eng():
    return render_template("news_eng.html", title="News | math-mech-space.ru")


@application.route("/inventions")
def inventions():
    return render_template("inventions.html", title="Изобретения | math-mech-space.ru")


@application.route("/inventions/eng")
def inventions_eng():
    return render_template(
        "inventions_eng.html", title="Inventions | math-mech-space.ru"
    )
