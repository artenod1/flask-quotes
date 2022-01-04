from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from quotes import Quote, app

api = Api(app)

resource_fields = {
	'quote_id': fields.Integer,
	'quote': fields.String,
	'quote_origin': fields.String,
	'date_posted': fields.String
}

class QuoteRef(Resource):
    @marshal_with(fields=resource_fields)
    def get(self):
        result = Quote.query.all()
        if not result:
            abort(404, message="Could not find quotes")
        return result

api.add_resource(QuoteRef, "/api")