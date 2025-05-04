import unittest
from fastapi.testclient import TestClient
from api import main

client = TestClient(main.app)

class TestMenuItemAPI(unittest.TestCase):

    def test_get_menu_items(self):
        response = client.get("/menu")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_menu_item(self):
        data = {
            "name": "Test Burger",
            "price": 10.99,
            "calories": 777,
            "category": "Temp"
        }
        response = client.post("/menu", json=data)
        self.assertEqual(response.status_code, 200)
        json_resp = response.json()
        self.assertEqual(json_resp["name"], data["name"])
        self.assertEqual(json_resp["price"], data["price"])

    def test_update_menu_item(self):
        new_item = {
            "name": "Temp Item",
            "price": 5.00,
            "calories": 500,
            "category": "Temp"
        }
        post_resp = client.post("/menu", json=new_item)
        item_id = post_resp.json()["id"]

        update_data = {"name": "Updated item",
                       "price": 6.69,
                       "calories": 420,
                       "category": "Temp"
        }
        put_resp = client.put(f"/menu/{item_id}", json=update_data)
        self.assertEqual(put_resp.status_code, 200)
        self.assertEqual(put_resp.json()["price"], update_data["price"])

    def test_delete_menu_item(self):
        new_item = {
            "name": "Delete Me :D",
            "price": 4.44,
            "calories": 444,
            "category": "Test"
        }
        post_resp = client.post("/menu", json=new_item)
        item_id = post_resp.json()["id"]

        delete_resp = client.delete(f"/menu/{item_id}")
        self.assertEqual(delete_resp.status_code, 200)

        get_resp = client.get(f"/menu/{item_id}")
        self.assertEqual(get_resp.status_code, 404)

if __name__ == "__main__":
    unittest.main()
