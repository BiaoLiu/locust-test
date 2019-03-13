from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):

    @task
    def recommend_list(self):
        header = {
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NDU5NjQ4NTcsInNpZCI6Ik1UVTBOVGsyTkRnMU4zeEJkMUZCUVdjOVBYenRLY2dNUnprY2pXR0FnWEctbFpRaEVYNXRtZFZVck9KSzRyNmNCUDJpMHc9PSIsInVpZCI6MX0.m4FOOnHE2TokY69c66WO-vXwt-bvzGjKmpjF74uq3_s'
        }
        self.client.get("/server/verify", headers=header)


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = 'http://localhost:8200'
    min_wait = 1000
    max_wait = 5000
