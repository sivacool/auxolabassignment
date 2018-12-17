from flask import Flask, jsonify, request,Response
from json import dumps,loads
from multiprocessing import Value
from flask_mail import Mail,Message
from datetime import datetime

counter = Value('i', 0)

app = Flask(__name__)

mail = Mail(app)
app.config.from_pyfile('config.cfg')

@app.route('/tests', methods=['POST'])
def tests():
	starttime =datetime.now()
	welcome = "Hello "+request.get_json()['name']
	with counter.get_lock():
		counter.value += 1
	if counter.value % 1000 == 0:
		time_elapsed = datetime.now() - starttime
		app.logger.debug(time_elapsed)
		app.logger.debug("mailTiggered")
		msg = Message("Once reach thousands",sender= 'sivasivacsc@gmail.com',recipients=['sivasivacsc@gmail.com'])
		msg.body = "This testing one"
		app.logger.debug("!!!!!!!!!!!!!!!!!! Am Gonna send Email !!!!!!!!!!!!!")
		mail.send(msg)
		app.logger.debug("!!!!!!!!!!!!!!!!!! Am Gonna send Email !!!!!!!!!!!!!")
	starttime = datetime.now()
	return Response(dumps(welcome),mimetype='application/json')


if __name__ == '__main__':
	app.run()  