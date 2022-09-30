from locust import HttpUser, task
from uuid import uuid4
from datetime import datetime
import random


# Create your tests here.

class LoadTestMeteringApi(HttpUser):
    @task
    def test_metering(self):
        self.client.post("server/metering", {
            "uniqueKey": str(uuid4()),
            "customerId": str(uuid4()),
            "clientId": str(uuid4()),
            "timestamp": str(datetime.today()),
            "bytes": random.randint(1, 10000)
        })
