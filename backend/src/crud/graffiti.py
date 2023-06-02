from backend.src.models.entity import Session
from backend.src.models.graffiti import Graffiti, GraffitiSchema


def create_graffiti(image_url, address, longitude, latitude, zip, comment, has_admin_checked=False):
    graffiti = Graffiti(image_url=image_url, address=address, longitude=longitude, latitude=latitude, zip=zip,
                        comment=comment, has_admin_checked=has_admin_checked)

    session = Session()
    session.add(graffiti)
    session.commit()

    graffiti_obj = GraffitiSchema().dump(graffiti)
    session.close()

    return graffiti_obj


def get_graffities():
    session = Session()
    graffities_objs = session.query(Graffiti).filter_by().all()

    schema = GraffitiSchema(many=True)
    graffities = schema.dump(graffities_objs)

    session.close()

    return graffities


def get_graffiti(id):
    session = Session()
    graffiti_obj = session.query(Graffiti).filter_by(id=id).first()

    schema = GraffitiSchema()
    graffiti = schema.dump(graffiti_obj)

    session.close()

    return graffiti


def check_graffiti(id):
    session = Session()
    graffiti_obj = session.query(Graffiti).filter_by(id=id).update({'has_admin_checked': True})

    session.commit()
    session.close()

    return graffiti_obj