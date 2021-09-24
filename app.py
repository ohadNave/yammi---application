from flask import Flask
from flask_restplus import Api
import logging

app = Flask(__name__)
api = Api(app = app, version = "1.0", title = "Yammi Application", catch_all_404s=True)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route('/')
def index():
    return "Record not found", 400


if __name__ == "__main__":
    app.run(debug=True)


from routes import orders