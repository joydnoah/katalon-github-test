from flask_restful import Resource
from flask import render_template, make_response
from controllers.template_database_controller import TemplateDatabaserController

class CheckResource(Resource):
    """
    Check API Endpoints
    """
    def get(self):
        """
        Return code to identify status of the api
        :return response: JSON. Ie, {}
        """
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("welcome_page.html"),200,headers)