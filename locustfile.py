from locust import HttpLocust, TaskSet, task
from json import loads,dumps
class UserBehavior(TaskSet):
	@task
	def put_username(self):
		payload = dict(name= "Siva Ravi")
		headers = {'content-type':'application/json'}
		self.client.post("/username",data =dumps(payload),headers=headers)
class WebsiteUser(HttpLocust):
	task_set = UserBehavior