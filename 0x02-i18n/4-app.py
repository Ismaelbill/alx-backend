#!/usr/bin/env python3
""" Force locale with URL parameter """

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """class - configures available languages & timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    if locale provided,
    otherwise determine the best match with our supported languages
    """
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def home():
    """function returns a rendered template"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
