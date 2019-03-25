from flask_restplus import fields
from api.restplus import api

authors = api.model('authors', {
    'literal': fields.String(readOnly=True, description='Literal name'),
    'given': fields.String(readOnly=True, description='Given name'),
    'family': fields.String(readOnly=True, description='Family anme'),
})

works = api.model('works', {
    'title': fields.String(readOnly=True, description='Article title'),
    'authors': fields.List(fields.Nested(authors)),
    'description': fields.String(readOnly=True, description='Description of the article'),
    'year': fields.String(readOnly=True, description='Publication date of article'),
    'doi': fields.String(readOnly=True, description='Doi reference'),
    'access_constraints': fields.String(readOnly=True, description='Access constraints'),
})

works_list = api.inherit('works list', works, {
    'items': fields.List(fields.Nested(works))
})
