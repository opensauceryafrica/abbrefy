import os
from abbrefy import create_app

application = create_app()

if __name__ == '__main__':
    if os.environ.get('ENVIRONMENT') == "development":
        application.run(debug=True, port=5000)
    else:
        application.run()
