def easy_blueprints(config):
    """
    register project packages here
    """

    # flake8: noqa: F401, F811
    from bartend.auth import routes, models

    if not config.IS_PRODUCTION:
        from bartend.tasks import cy_tasks


def error_handlers(app, jwt):
    """
    default server exceptions
    """

    @jwt.invalid_token_loader
    def jwt_unprocessable_entity(error):
        """
        jwt not present
        """
        return default_400()
    app.register_error_handler(422, jwt_unprocessable_entity)


    @jwt.unauthorized_loader
    def jwt_unauthorized(error):
        """
        jwt mismatch
        """
        return default_400()
    app.register_error_handler(401, jwt_unauthorized)


    @jwt.expired_token_loader
    def jwt_expired(error):
        """
        jwt expired
        """
        return default_400()
    app.register_error_handler(401, jwt_expired)


    from werkzeug.exceptions import HTTPException
    @app.errorhandler(HTTPException)
    def forbidden(error):
        """
        refusing action
        """
        return default_400()
    app.register_error_handler(403, forbidden)


def default_400():
    """
    default 400 handler
    """
    from dev.dev_session import clear_session_data
    from endpoint.response.studio_response import StudioResponse
    kwargs = dict(
        flash=dict(
            title='Session Expired',
            text='Please login to proceed',
            timer=3000,
        ),
        next='/auth/sign-in',
        status_code=202,
    )

    return StudioResponse(clear_session_data(), **kwargs)
