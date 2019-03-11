from flask_restplus import fields
from api.restplus import api

works = api.model('works', {
    'title': fields.String(readOnly=True, description='Article title'),
    'author': fields.String(readOnly=True, description='Article authors'),
    'description': fields.String(readOnly=True, description='Description of the article'),
    'published': fields.String(readOnly=True, description='Publication date of article'),
    'doi': fields.String(readOnly=True, description='doi reference'),
    'license': fields.String(readOnly=True, description='privileges'),
})
