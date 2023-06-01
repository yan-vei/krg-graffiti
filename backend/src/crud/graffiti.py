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


