from locust import task, HttpUser, SequentialTaskSet
from assertpy import assert_that


class MyCode(SequentialTaskSet):


    @task
    def get_Api(self):
        req = self.client.get("/api/v1/Activities")
        assert_that(req.status_code).is_equal_to(200)
        assert_that(req.json()[0]["id"]).is_type_of(int)

    @task
    def get_Api(self):
        payload = {
            "id": 0,
            "title": "Activity post",
            "dueDate": "2024-07-15T14:44:33.619Z",
            "completed": True
        }
        req = self.client.post("/api/v1/Activities", json=payload)
        assert_that(req.status_code).is_equal_to(200)
        assert_that(req.json()[0]["id"]).is_type_of(int)

    @task
    def get_Api(self):
        payload = {
            "title": "Activity edit post",
            "dueDate": "2024-07-15T14:44:33.619Z",
            "completed": False
        }
        req = self.client.put("/api/v1/Activities/3", json=payload)
        assert_that(req.status_code).is_equal_to(200)
        assert_that(req.json()[0]["id"]).is_type_of(int)

    @task
    def get_Api(self):

        req = self.client.delete("/api/v1/Activities/3",)
        assert_that(req.status_code).is_equal_to(200)

class setUpTest(HttpUser):
    host = "https://fakerestapi.azurewebsites.net"
    tasks = {MyCode}
