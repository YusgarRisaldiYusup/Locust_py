from locust import task, HttpUser
from assertpy import assert_that


class MyCode(HttpUser):
    host = "https://fakerestapi.azurewebsites.net"

    @task
    def get_Api(self):
        req = self.client.get("/api/v1/Activities")
        assert_that(req.status_code).is_equal_to(200)
        assert_that(req.json()[0]["id"]).is_type_of(int)


