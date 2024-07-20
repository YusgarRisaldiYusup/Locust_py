from locust import task, HttpUser
from assertpy import assert_that


class MyCode(HttpUser):
    host = "https://fakerestapi.azurewebsites.net"

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


