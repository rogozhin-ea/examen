import json
import unittest
import requests

from flask import request


class TestAPI(unittest.TestCase):

    def test1(self):
        resp = requests.get("http://127.0.0.1:5000/")
        self.assertEqual(resp.status_code, 200)
        print("test1: OK")

    def test2(self):
        resp = requests.get("http://127.0.0.1:5000/class")
        self.assertEqual(resp.status_code, 200)
        print("test2: OK")

    def test3(self):
        resp = requests.post("http://127.0.0.1:5000/login")
        self.assertEqual(resp.status_code, 200)
        print("test3: OK")

    def test4(self):
        resp = requests.post("http://127.0.0.1:5000/login")
        self.assertEqual(resp.status_code, 200)
        print("test4: OK")


if __name__ == '__main__':
    tester = TestAPI()
    tester.test1()
    tester.test2()
    tester.test3()
    tester.test4()