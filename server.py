from flask import Flask, jsonify, request,Response
from json import dumps,loads
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
@app.route('/hello', methods=['POST'])
def hello():
	welcome = "Hello "+request.get_json()['name']
	return Response(dumps(welcome),mimetype='application/json')
if __name__ == '__main__':
	app.run(port=5001)  