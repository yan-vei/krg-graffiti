from ..models.entity import Session
from ..models.graffiti import Graffiti, GraffitiSchema


def create_graffiti(image_url, address, longitude, latitude, zip, comment, has_admin_checked=False):
    graffiti = Graffiti(image_url=image_url, address=address, longitude=longitude, 
                        latitude=latitude, zip=zip, comment=comment, 
                        has_admin_checked=has_admin_checked)

    session = Session()
    session.add(graffiti)
    session.commit()

    graffiti_obj = GraffitiSchema().dump(graffiti)
    session.close()

    return graffiti_obj

  
def get_graffities(is_admin):
    session = Session()

    if is_admin:
        graffities_objs = session.query(Graffiti).filter_by().all()
    else:
        graffities_objs = session.query(Graffiti).filter_by(has_admin_checked=True).all()

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


def update_graffiti(id, update_obj):
    session = Session()
    graffiti_obj = session.query(Graffiti).filter_by(id=id).update(update_obj)

    session.commit()
    session.close()

    return graffiti_obj
