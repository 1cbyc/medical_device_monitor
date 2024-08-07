from . import db

class DeviceData(db.Model):
    __tablename__ = 'device_data'  # Renamed to be more descriptive
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    heart_rate = db.Column(db.Integer, nullable=False)
    device_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
