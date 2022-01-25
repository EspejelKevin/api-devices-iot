from flask import Flask
from flask_restful import Api
from src.resources.deviceResource import Device, Devices
from db import db
    

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://wqfzqlzyoonvbu:389c6f6717bbb996f8bf7604dfa9cb22c8ec7c9e165a3698a78c9f8e57b5c177@ec2-54-161-189-150.compute-1.amazonaws.com:5432/dfv8v2skrl9rkf"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "development"
app.config['PROPAGATE_EXCEPTIONS'] = True

db.init_app(app)
api = Api(app)

api.add_resource(Device, "/api/device/iot/<int:id>", "/api/device/iot")
api.add_resource(Devices, "/api/devices/iot")


if __name__ == "__main__":
    app.run()
