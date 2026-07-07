from locust import HttpUser, SequentialTaskSet, task, between


class CheckoutFlow(SequentialTaskSet):
    @task(3)
    def open_cart(self):
        self.client.get("/cart")

    @task(4)
    def checkout(self):
        self.client.post("/checkout")

    @task(3)
    def confirm(self):
        self.client.get("/order/confirm")


class CheckoutUser(HttpUser):
    host = "https://api.example.com"
    tasks = [CheckoutFlow]
    wait_time = between(2, 4)
