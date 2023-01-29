from flask import Flask

# from flask_restx import Api

app = Flask(__name__)
# api = Api(app, doc="/docs", version="1.0", title="Demo API", description="Demo system")


from flaskr.controllers import controller  # noqa: E402,F403,F401
