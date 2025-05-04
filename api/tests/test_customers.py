import unittest
from fastapi.testclient import TestClient
from api import main

client = TestClient(main.app)

class TestCustomerAPI(unittest.TestCase):

    def test_create_customer(self):
        data = {
            "name": "John Doe",
            "email": "John_Doe@example.com",
            "phone": "123-456-7890",
            "address": "123 Wall Street"
        }
        response = client.post("/customers", json=data)
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertIn("id", json_data)
        self.assertEqual(json_data["email"], data["email"])

    def test_get_all_customers(self):
        response = client.get("/customers")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_customer_by_id(self):
        data = {
            "name": "John Doe",
            "email": "John_Doe@example.com",
            "phone": "123-456-7890",
            "address": "123 Wall Street"
        }
        post_resp = client.post("/customers", json=data)
        customer_id = post_resp.json()["id"]

        get_resp = client.get(f"/customers/{customer_id}")
        self.assertEqual(get_resp.status_code, 200)
        self.assertEqual(get_resp.json()["id"], customer_id)

    def test_delete_customer(self):
        data = {
            "name": "John Doe",
            "email": "john_Doe@example.com",
            "phone": "123-456-7890",
            "address": "123 Wall Street"
        }
        post_resp = client.post("/customers", json=data)
        customer_id = post_resp.json()["id"]

        delete_resp = client.delete(f"/customers/{customer_id}")
        self.assertIn(delete_resp.status_code, [200, 204])

        get_resp = client.get(f"/customers/{customer_id}")
        self.assertEqual(get_resp.status_code, 404)

if __name__ == "__main__":
    unittest.main()
