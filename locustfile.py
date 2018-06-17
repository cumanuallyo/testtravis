from locust import HttpLocust, TaskSet, task
import os

class UserBehavior(TaskSet):
    @task
    def index1(self):
        self.client.get(os.environ['E_URI'],name=os.environ['E_URI2'])

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = ''
    min_wait = 5000
    max_wait = 9000