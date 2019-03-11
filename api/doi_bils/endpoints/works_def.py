import logging
import json
import requests, sys
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from flask_restplus import Resource
from flask_restplus import reqparse
from api.doi_bils.serializers import works as work
from api.doi_bils.parsers import doi_args
from api.works import get_all_works,get_work_by_id
from api.restplus import api


log = logging.getLogger(__name__)
ns = api.namespace('doi-bils/works', description='Operations related to works')


@ns.route('/all')
class WorkCollection(Resource):

    def get(self):
        """
        Returns a list of works
        """
        return get_all_works()

@api.expect(doi_args)
@ns.route('/single')
class SingleWork(Resource):

    def get(self):
        """
        Returns a single work object.
        """
        args = doi_args.parse_args(request)
        return get_work_by_id(args['doi'])
