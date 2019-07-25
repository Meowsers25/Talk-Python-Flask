import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Trying Github"

app.run()