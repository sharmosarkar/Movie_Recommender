import logging
from flask import request
from flask_restplus import Resource
from restplus import api
import Recommender

popularity_model, item_sim_model, users, items = Recommender.load_models()

log = logging.getLogger(__name__)
ns = api.namespace('recommendations', description='Movie Rocommendations for a specific user')

@ns.route('/<int:id>')
@api.response(404, 'User not found.')
class UserItem(Resource):
    def get(self, id):
        """
        Returns a list of Movie Recommendations for the user
        """
        return Recommender.predict_CF_item_sim(item_sim_model, id)
