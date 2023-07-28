import flask
from flask_restful import Api
from resource.user import Users, SingleUser
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from model import db

# Flask setting
app = flask.Flask(__name__)

# Flask restful setting
api = Api(app)


app.config["DEBUG"] = True # Able to reload flask without exit the process
app.config["JWT_SECRET_KEY"] = "secret_key" #JWT token setting 


# DB setting
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@127.0.0.1:10100/demo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_pre_ping": True,
    "pool_recycle": 60,
    "pool_timeout": 300,
    "pool_size": 20,
}

# Swagger setting
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Coscup demo project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        # securityDefinitions=security_definitions, # Able to add Jwt token in header in Swagger
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

# URL(router)
api.add_resource(Users, "/users")
docs.register(Users)

api.add_resource(SingleUser, "/user/<int:id>")
docs.register(SingleUser)


if __name__ == '__main__':
    db.init_app(app)
    db.app = app
    app.run(host='127.0.0.1', port=10009)
