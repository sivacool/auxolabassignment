from flask import Flask, jsonify, request,Response
from json import dumps,loads
from multiprocessing import Value
from flask_mail import Mail,Message
from datetime import datetime
from requests import post,get
from subprocess import call
import os
counter = Value('i', 0)
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
mail = Mail(app)

@app.route('/tests', methods=['POST'])
def tests():
	data = request.get_json()
	with counter.get_lock():
		counter.value += 1
	app.logger.debug(counter.value)
	post(url = app.config['SERVER_URI']+'/hello', data = dumps(data),headers={'content-type':'application/json'})
	if counter.value % 1000 == 0:
		boolmail = mailTrigger(value=counter.value)
	return Response(dumps({"status":"sucess"}),mimetype='application/json')

def mailTrigger(value):
	msg = Message("Auxo Labs Load testing mail of "+value+"requests",sender= 'sivasivacsc@gmail.com',recipients=['sivasivacsc@gmail.com'])
	msg.body = "HI Auxo Labs PFA"
	msg.attach("log_distribution.csv","text/csv",log_distribution)
	msg.attach("log_requests.csv","text/csv",log_requests)
	app.logger.debug("!!!!!!!!!!!!!!!!!! Start sending Email !!!!!!!!!!!!!")
	mail.send(msg)
	app.logger.debug("!!!!!!!!!!!!!!!!!! Successfully sent Email !!!!!!!!!!!!!")
	return True


if __name__ == '__main__':
	os.system("locust -c 10 -r 5 -t 30s --no-web --host http://localhost:5000 --csv=log")
	app.run(port=5000)  