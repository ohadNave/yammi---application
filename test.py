from app import app
from utils import db_utils, test_db
import unittest
import json


class ApiTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.tester = app.test_client(self)

    # Check db is empty on first get request.
    def test_response(self):
        db_utils.db = []
        response = self.tester.get("/Orders/")
        status_code = response.status_code
        self.assertEqual(response.get_json(), "There is no orders to retrieve.")
        self.assertEqual(status_code, 200)


    # Check returned content type.
    def test_content_type(self):
        response = self.tester.get("/Orders/")
        self.assertEqual(response.content_type, "application/json")



    #Check post of a valid order returned content.
    def test_valid_content(self):
        post_response = self.tester.post("/Orders/", data = json.dumps(test_db.valid_order1, default=str), content_type='application/json')
        get_response = self.tester.get("/Orders/")
        self.assertEqual(post_response.status_code, 200)
        added_order_name = get_response.get_json()[0]['name']
        self.assertEqual(added_order_name, test_db.valid_order1['name'])


    #Check invalid order returned content.
    def test_invalid_content(self):
        post_response = self.tester.post("/Orders/", data = json.dumps(test_db.invalid_order1,  default=str), content_type='application/json')
        self.assertEqual(post_response.status_code, 400)

    
    #Check last day orders amount.
    def test_invalid_content(self):
        self.tester.post("/Orders/", data = json.dumps(test_db.valid_order1,  default=str), content_type='application/json')
        self.tester.post("/Orders/", data = json.dumps(test_db.valid_order2 ,  default=str), content_type='application/json')
        self.tester.post("/Orders/", data = json.dumps(test_db.valid_order3,  default=str), content_type='application/json')
        response = self.tester.get("/Orders/")
        self.assertEqual(len(response.get_json()), 2)


if __name__ == "__main__":
    print("Started Testing ... ")
    unittest.main()