from framework.api.client import APIClient

client = APIClient("https://jsonplaceholder.typicode.com")

data = {
    "name": "Shirley",
    "email": "shirley@example.com"
}

response = client.post("/users", data)

print(response.status_code)
print(response.json())