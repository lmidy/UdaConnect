from app.udaconnect.models import Connection, Location, Person  # noqa
from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from app.connection.controllers import api as connection_api

    api.add_namespace(connection_api, path=f"/{root}")
ß