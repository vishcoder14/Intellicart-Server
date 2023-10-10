from __main__ import fserver
import flask


@fserver.route('/')
def index():
    return flask.render_template('welcome_page.html')


@fserver.route('/api/jsonData', methods=['GET'])
def get_data_json():
    data = {'name': 'vishnu sukumar', 'age': 22}
    return flask.jsonify(data)


@fserver.route('/api/string', methods=['GET'])
def get_data_str():
    return "tNKX5o99REXiEK3g6QIs48WR1x82"
