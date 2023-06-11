from sqlalchemy import Column, String, Integer, Boolean, Float
from marshmallow import Schema, fields
from backend.src.models.entity import Base


class Graffiti(Base):
    __tablename__ = "graffities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String, nullable=False)
    has_admin_checked = Column(Boolean, nullable=False, default=False)
    address = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    zip = Column(Integer)
    comment = Column(String)

    def __init__(self, image_url, address, longitude, latitude, zip, comment, has_admin_checked=False):
        self.image_url = image_url
        self.has_admin_checked = has_admin_checked
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.zip = zip
        self.comment = comment


class GraffitiSchema(Schema):
    id = fields.Number()
    image_url = fields.Str()
    address = fields.Str(allow_none=True)
    longitude = fields.Float(allow_none=True)
    latitude = fields.Float(allow_none=True)
    zip = fields.Number(allow_none=True)
    comment = fields.Str(allow_none=True)
