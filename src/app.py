from flask import Flask
from controllers.getController import caradhras
from config import *

app = Flask(__name__)
app.register_blueprint(caradhras, url_prefix='/')

if __name__ == '__main__':
    print('Flask is running')
    app.debug = True
    app.run()