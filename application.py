from logging import log
import os
from abbrefy import create_app

application = create_app()

# os.environ['ROOT_PATH'] = application.root_path
os.environ.setdefault('ROOT_PATH', application.root_path)

if __name__ == '__main__':
    if os.environ.get('ENVIRONMENT') == "development":
        application.run(debug=True, port=5000)
    else:
        application.run()
