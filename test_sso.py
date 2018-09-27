from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):

    @task
    def index(self):
        header = {
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MzgwMzg3NzgsInNpZCI6Ik1UVXpPREF6T0RjM09IeEJkMUZCVFdjOVBYeUlxalhtUENmYXNnSS1abDdpYXZDWGVfSmxFbnh1UTc5ZTVicVh5dDhSMXc9PSIsInVpZCI6MjV9.rg1oyANCulwE7Bxv9GifSGBEZh-ESduntnkVsAJ2Mx0'
        }
        self.client.get("/server/verify", headers=header)


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = 'http://localhost:8200'
    min_wait = 1000
    max_wait = 5000
