from flask import Flask, jsonify, request,Response
from json import dumps,loads
app = Flask(__name__)
testing_types = list(dict(name='unit testing',description='testing individual units of source code'))
@app.route('/')
def test():
	app.logger.debug("PerilWise")
	return Response (dumps(dict(status=True)),mimetype='application/json')
@app.route('/tests', methods=['GET','POST'])
def tests():
	if request.method == 'GET':
		app.logger.debug("PerilWise")
		return Response(dumps(testing_types), mimetype='application/json')
	elif request.method == 'POST':
		testing_types.append(request.get_json())
		return '', 204

if __name__ == '__main__':
	app.run(debug=True)  