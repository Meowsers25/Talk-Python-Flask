import flask

app = flask.Flask(__name__)
# adds this because dummy data relocated
# !moved again to views/home_views.py
# import services.package_service as package_service

# relocated dummy data to services/package_service.py

# relocated routes into views/home_views.py

def main():
    register_blueprints()
    app.run(debug=True) 

def register_blueprints():
    from views import home_views
    from views import package_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)

if __name__ == '__main__':
       main()