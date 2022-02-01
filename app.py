from flask import Flask
from flask_restful import Api
from src.resources.deviceResource import Device, Devices
from db import db
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://fzcpptcdpeiuxh:5b0cfb537916c5e389fd1938aeec0277f1c35dcc14e20cdff7250e8be714ca17@ec2-34-194-171-47.compute-1.amazonaws.com:5432/d7fgnqa6hdktu8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "development"
app.config['PROPAGATE_EXCEPTIONS'] = True

CORS(app, resources={r"*": {"origins": "*"}})

db.init_app(app)
api = Api(app)

api.add_resource(Device, "/api/device/iot/<int:id>", "/api/device/iot")
api.add_resource(Devices, "/api/devices/iot")


if __name__ == "__main__":
    app.run()
