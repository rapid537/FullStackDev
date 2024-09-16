import waitress
from rm_pycache import rm_pycache

from bartend import app
from bartend import BASE_CONFIG


def run_development():
    """
    run the development server
    """
    rm_pycache(stdout=True)
    app.run(host=BASE_CONFIG.STUDIO_DOMAIN, port=BASE_CONFIG.SERVER_PORT)


def run_production():
    """
    run the production server
    """
    waitress.serve(app, host=BASE_CONFIG.STUDIO_DOMAIN, port=BASE_CONFIG.SERVER_PORT)


if __name__ == '__main__':
    if BASE_CONFIG.IS_PRODUCTION:
        run_production()

    if not BASE_CONFIG.IS_PRODUCTION:
        run_development()
