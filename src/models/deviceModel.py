from db import db

class DeviceModel(db.Model):
    __tablename__ = "devices"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    ip = db.Column(db.String(20))
    mask = db.Column(db.String(20))
    gateway = db.Column(db.String(20))

    def __init__(self, name, ip, mask, gateway):
        self.name = name
        self.ip = ip
        self.mask = mask
        self.gateway = gateway

    def __repr__(self):
        return "<Device IoT %r>" % self.name

    def json(self):
        return {"id":self.id, "name":self.name, "ip":self.ip, "mask":self.mask, "gateway":self.gateway}

    @classmethod
    def find_by_id(cls, id, name):
        if id:
            return cls.query.filter_by(id=id).first()
        else:
            return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    
