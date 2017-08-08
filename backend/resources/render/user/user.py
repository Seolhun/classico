from flask import render_template
from flask_cors import cross_origin

from resources.render.render_url import cache
from setting.build_app import app
from setting.logging import logger


@cross_origin()
@cache.cached(timeout=60, key_prefix='home')
@app.route('/classico')
def classico_home():
    logger.info('-------------------------HERE------------------------------')
    return render_template('app.html')


@app.route('/')
def hello_world():
    logger.info('-------------------------HERE------------------------------')
    return 'Hello, World!'
