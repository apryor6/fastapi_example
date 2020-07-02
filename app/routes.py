def register_routes(app, root="api"):
    from app.widget import register_routes as attach_widget
    from app.fizz import register_routes as attach_fizz

    # Add routes
    attach_widget(app)
    attach_fizz(app)
