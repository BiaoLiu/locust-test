import random

from locust import TaskSet, task, HttpLocust

header = {
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NDU5NjQ4NTcsInNpZCI6Ik1UVTBOVGsyTkRnMU4zeEJkMUZCUVdjOVBYenRLY2dNUnprY2pXR0FnWEctbFpRaEVYNXRtZFZVck9KSzRyNmNCUDJpMHc9PSIsInVpZCI6MX0.m4FOOnHE2TokY69c66WO-vXwt-bvzGjKmpjF74uq3_s'
}


class WebsiteTasks(TaskSet):
    @task
    def recommend_list(self):
        pnos = ['GB0000068']
        pno = random.choice(pnos)
        url = "/products/{pno}/recommend".format(pno=pno)
        self.client.get(url, headers=header)

    @task
    def relation_list(self):
        mnos = ['FB00000810002', 'HA00000960001']
        mno = random.choice(mnos)
        url = "/models/{mno}/relation".format(mno=mno)
        self.client.get(url, headers=header)


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = 'http://localhost:9100'
    min_wait = 1000
    max_wait = 5000
