from flask_restful import reqparse, abort, Api, Resource

class DataBaseInit(Resource):
    def get(self):
        return {'hello': 'world'}