from flask import (
    request
)
from flask_restplus import Resource, reqparse
from api.works.serializers import works, works_list
from api.works.parsers import doi_args
from api.works.work import get_all_works,get_work_by_id
from api.restplus import api
import logging


ns = api.namespace('works', description='Operations related to works')


@ns.route('/all')
class WorkCollection(Resource):

    @api.marshal_with(works_list)
    def get(self):
        """
        Returns a list of works
        """
        return get_all_works()


@ns.route('/single')
class SingleWork(Resource):

    @api.expect(doi_args)
    @api.marshal_with(works)
    def get(self):
        """
        Returns a single work object.
        """
        args = doi_args.parse_args(request)
        return get_work_by_id(args['doi'])
