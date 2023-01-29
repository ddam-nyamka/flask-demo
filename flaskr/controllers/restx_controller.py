from flask import render_template, request
from flask_restx import Resource, fields

from flaskr import api

ns = api.namespace("api", description="Test api")

request_model = api.model(
    "TestRequest",
    {
        "text": fields.String(required=True),
    },
)


@ns.route("/")
class HelloWorld(Resource):
    def get(self):
        return render_template("index.html")

    @ns.expect(request_model, validate=True)
    def post(self):
        data = request.get_json()
        input_text = data.get("text")
        return {"success": f"Input text is {input_text}"}
