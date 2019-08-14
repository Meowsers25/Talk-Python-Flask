import flask
import services.package_service as package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')

@blueprint.route('/project/<package_name>')
def package_details(package_name: str):
    # test_packages = package_service.get_latest_packages()

    return flask.render_template('packages/details.html')

    # return "Package details for {}".format(package_name)