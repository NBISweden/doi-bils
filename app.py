import os
import settings
import requests
import json
from api.works.work import get_all_works,get_work_by_id
from api.restplus import api
from api.works.namespace import ns
from gevent.pywsgi import WSGIServer
from certs.certs import generate_ssl_certs
from flask import (
    Blueprint, Flask, render_template, request, abort
)
import logging

log = logging.getLogger(__name__)

app = Flask(__name__)
api_blueprint = Blueprint('api', __name__, url_prefix='/api')
works_blueprint = Blueprint('works', __name__, url_prefix='/works')


@app.route('/')
def all_works():
    works = get_all_works()
    return render_template('index.html', works=works)


@works_blueprint.route('/')
def single_work():
    doi = request.args.get('doi')
    work = get_work_by_id(doi)
    if work:
        return render_template('landing_page.html', work=work)
    else:
        abort(404, 'Entry not found in the server')


def configure_app(flask_app):
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def start_app(flask_app):
    configure_app(flask_app)
    api.init_app(api_blueprint)
    api.add_namespace(ns)
    flask_app.register_blueprint(api_blueprint)
    flask_app.register_blueprint(works_blueprint)


def main():
    start_app(app)
    print('>>>>> Starting server at http://{}:{} <<<<<'.format(settings.HOST,settings.PORT))
    # Self generated certificates
    generate_ssl_certs(country='SE', country_code='22', location='Uppsala', org='NBIS', email='pepe@hotmail.com', org_unit="NBIS sysdevs", common_name="NBIS")
    # Start gevent WSGI server
    wsgi_server = WSGIServer((settings.HOST, settings.PORT), app, certfile=settings.CERT_FILE, keyfile=settings.KEY_FILE)
    wsgi_server.serve_forever()

if __name__ == "__main__":
    main()
