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
@app.route('/username', methods=['POST'])
def username():
	data = request.get_json()
	with counter.get_lock():
		counter.value += 1
	app.logger.debug(counter.value)
	post(url = app.config['SERVER_URI']+'/hello', data = dumps(data),headers={'content-type':'application/json'})
	if counter.value % 1000 == 0:
		boolmail = mailTrigger(value=counter.value)
	return Response(dumps({"status":"sucess"}),mimetype='application/json')

def mailTrigger(value):
	msg = Message("Auxo Labs Load testing mail of "+str(value)+" requests",sender= app.config['MAIL_USERNAME'],recipients=[app.config['MAIL_USERNAME']])
	msg.body = "HI Auxo Labs PFA"
	app.logger.debug(os.listdir())
	log_distribution = open('log_distribution.csv','rb')
	log_requests = open('log_requests.csv','rb')
	msg.attach(filename = "log_distribution.csv",content_type = "text/csv",data = log_distribution.read())
	msg.attach(filename = "log_requests.csv",content_type = "text/csv",data = log_requests.read())
	app.logger.debug("!!!!!!!!!!!!!!!!!! Start sending Email !!!!!!!!!!!!!")
	mail.send(msg)
	app.logger.debug("!!!!!!!!!!!!!!!!!! Successfully sent Email !!!!!!!!!!!!!")
	return True


if __name__ == '__main__':
	# os.system("locust -c 10 -r 5 -t 30s --no-web --host http://localhost:5000 --csv=log")
	app.run(port=5000)  