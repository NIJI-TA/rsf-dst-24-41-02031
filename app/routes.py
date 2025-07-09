from app import application

from flask import render_template


# Routes
@application.route("/")
def index():
    return render_template("index.html", title="math-mech-space")


@application.route("/eng")
def index_eng():
    return render_template("index_eng.html", title="math-mech-space")


@application.route("/articles")
def articles():
    return render_template("articles.html", title="math-mech-space: Статьи")


@application.route("/articles/eng")
def articles_eng():
    return render_template("articles_eng.html", title="math-mech-space: Articles")


@application.route("/conferences")
def conferences():
    return render_template("conferences.html", title="math-mech-space: Конференции")


@application.route("/conferences/eng")
def conferences_eng():
    return render_template("conferences_eng.html", title="math-mech-space: Conferences")


@application.route("/news")
def news():
    return render_template("news.html", title="math-mech-space: Новости")


@application.route("/news/eng")
def news_eng():
    return render_template("news_eng.html", title="math-mech-space: News")


@application.route("/inventions")
def inventions():
    return render_template("inventions.html", title="math-mech-space: Изобретения")


@application.route("/inventions/eng")
def inventions_eng():
    return render_template("inventions_eng.html", title="math-mech-space: Inventions")
