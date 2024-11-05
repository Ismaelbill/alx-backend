#!/usr/bin/env python3
""" Force locale with URL parameter """

from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """class - configures available languages & timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    returns a user dictionary or None
    """
    id = request.args.get('login_as')
    if id:
        return users.get(int(id), None)


@app.before_request
def before_request():
    """
    finds a user if any, and set it
    as a global on flask.g.user"""
    dct = get_user()
    if dct:
        g.user = dct


@babel.localeselector
def get_locale():
    """
    if locale provided,
    otherwise determine the best match with our supported languages
    """
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale

    head_loc = request.headers.get('locale', '')
    if head_loc in Config.LANGUAGES:
        return head_loc
    if g.user and g.user['locale'] in Config.LANGUAGES:
        return g.user['locale']
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def home():
    """function returns a rendered template"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(debug=True)
