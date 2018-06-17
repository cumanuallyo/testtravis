from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def index1(self):
        self.client.get("https://google.com/",name="https://google.com/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = ''
    min_wait = 5000
    max_wait = 9000