from flask_restplus import reqparse

doi_args = reqparse.RequestParser()
doi_args.add_argument('doi', required=True)
