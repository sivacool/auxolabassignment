from flask import Flask, jsonify, request,Response
from json import dumps,loads
from multiprocessing import Value

counter = Value('i', 0)

app = Flask(__name__)

@app.route('/tests', methods=['POST'])
def tests():
		welcome = "Hello "+request.get_json()['name']
		with counter.get_lock():
			counter.value += 1
		app.logger.debug(counter.value)
		# if counter.value >=1000:
		# 	app.logger.debug("mailtrigger")
		return Response(dumps(welcome),mimetype='application/json')

if __name__ == '__main__':
	app.run(debug=True)  