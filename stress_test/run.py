from random import randint
from locust import HttpUser, between, task, tag

class FlaskUser(HttpUser):
    wait_time = between(1, 3)
    
    @tag('view mainpage')
    @task
    def view_main(self):
        self.client.get('/')

    @tag('view Calcs')
    @task
    def view_calcs(self):
        self.client.get('/calculations')

    @tag('compute values page')
    @task
    def compute_calculations(self):
        with self.client.post('/calculations', {'value': randint(1234567890, 123456789012345)}, catch_response=True) as response:
            if response.status_code > 300:
                response.failure()

