import flask

app = flask.Flask(__name__)

def get_latest_packages():
    return [
        {'name': 'Flask', 'version': '1.2.3'},
        {'name': 'SQL', 'version': '2.2.0'},
        {'name': 'Passlib', 'version': '1.0.0'},
    ]

@app.route('/')
def index():
    test_packages = get_latest_packages()
    return flask.render_template('index.html', packages=test_packages)

if __name__ == "__main__":
    app.run(debug=True)