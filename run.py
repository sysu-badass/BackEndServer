from app import create_app
from config import config

if __name__ == '__main__':
    config_name = 'development'
    app = create_app(config[config_name])
    app.run(debug=True)
