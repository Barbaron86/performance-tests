from httpx import Client

def build_gateway_http_client() -> Client:
    return Client(base_url="http://localhost:8003", timeout=100)