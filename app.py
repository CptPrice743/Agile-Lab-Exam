from flask_api import FlaskAPI
from flask import request, jsonify

app = FlaskAPI(__name__)


@app.route('/status')
def status():
    return jsonify(status='ok')


@app.route('/sum')
def sum_route():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        a_val = float(a)
        b_val = float(b)
    except (TypeError, ValueError):
        return jsonify(error='invalid input'), 400
    return jsonify(result=a_val + b_val)


@app.route('/shutdown', methods=['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        return 'Not running with the Werkzeug Server', 500
    func()
    return 'Server shutting down...'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=False, use_reloader=False)
