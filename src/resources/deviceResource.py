from signal import default_int_handler
from flask_restful import Resource, reqparse
from src.models.deviceModel import DeviceModel


class Device(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="Name device IoT"
                        )
    parser.add_argument('ip',
                        type=str,
                        required=True,
                        help="IP address of the device"
                        )
    parser.add_argument('mask',
                        type=str,
                        required=True,
                        help="Type the mask of the Device's IP"
                        )
    parser.add_argument('gateway',
                        type=str,
                        required=True,
                        help="Gateway of the router"
                        )           

    def get(self, id):
        device = DeviceModel.find_by_id(id, name=None)
        if device:
            return device.json()
        return {"message": "Device not found"}, 404

    def post(self):
        data = Device.parser.parse_args()

        name = data["name"] 
        if DeviceModel.find_by_id(id=None, name=name):
            return {'message': "An device with name '{}' already exists.".format(name)}, 400
        
        device = DeviceModel(**data)

        try:
            device.save_to_db()
        except:
            return {"message": "An error ocurred inserting the device"}, 500

        return device.json(), 201
    
    def delete(self, id):
        device = DeviceModel.find_by_id(id, name=None)

        if device:
            device.delete_from_db()
            return {"message": "Device deleted"}
        return {"message": "Device not found"}, 404
    
    def put(self, id):
        device = DeviceModel.find_by_id(id, name=None)

        data = Device.parser.parse_args()

        if device:
            device.name = data["name"]
            device.ip = data["ip"]
            device.mask = data["mask"]
            device.gateway = data["gateway"]
        else:
            device = DeviceModel(**data)

        device.save_to_db()

        return device.json()


class Devices(Resource):
    def get(self):
        return {"Devices IoT": list(map(lambda x:x.json(), DeviceModel.query.all()))}




    