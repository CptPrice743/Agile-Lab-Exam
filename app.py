from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    return jsonify(status='ok')

@app.route('/sum')
def sum_route():
    a = request.args.get('a')
    b = request.args.get('b')
    
    a_val = float(a)
    b_val = float(b)

    return jsonify(results=a_val + b_val)
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=False, use_reloader=False)