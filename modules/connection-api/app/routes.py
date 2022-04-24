def register_routes(api, app, root="api"):
    from app.connection import register_routes as attach_connection

    # Add routes
    attach_connection(api, app)
