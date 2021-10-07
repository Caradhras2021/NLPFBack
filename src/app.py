from flask import Flask
from controllers.getController import caradhras
from config import *
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(caradhras, url_prefix='/')
CORS(app, resources=r'/*', headers='Content-Type')

if __name__ == '__main__':
    print('Flask is running')
    app.debug = True
    app.run()